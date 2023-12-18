from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, joinedload, load_only, subqueryload
from sqlalchemy.sql import text

from app.crm import crm, enums, models, schemas
from app.crm.schemas import ContactAddress
# from app.sales import crud as sales_crud
# from app.sales import deps
from fastapi import HTTPException


def get_contact(db: Session, contact_id: int):
    contact = (
        db.query(models.Contact)
        .options(
            joinedload(models.Contact.company).joinedload(
                models.Contact.trades),
            joinedload(models.Contact.address_field),
            joinedload(models.Contact.trades),
        )
        .get(contact_id)
    )

    if contact is None:
        return contact

    if contact.company is None and len(contact.super_contacts) > 0:
        contact.company = contact.super_contacts[0]

    return contact


def get_persons(db: Session, country_id: int, skip: int = 0, limit: int = 100):
    persons = (
        db.query(models.Contact)
        .options(subqueryload(models.Contact.trades))
        .filter(
            models.Contact.country_id == country_id,
            models.Contact.contact_type == enums.ContactTypes.person,
        )
    )
    return persons.offset(skip).limit(limit).all()


def create_person(db: Session, person: schemas.Person):
    db_item = models.Contact(
        **person.dict(
            exclude={
                "name",
                "trades",
                "address_field",
                "company_name",
                "has_parent_company",
            }
        ),
        name=person.last_name + ", " + person.first_name,
    )
    for new_address in person.address_field:
        db_item.address_field.append(
            models.Address(
                **new_address.dict(exclude={"contact_id", "translations"}))
        )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    person.id = db_item.id

    if person.company_id != person.id:
        db_item.company_id = person.company_id

        next_db = crm.get_db()
        create_relationship(next_db, person.company_id, person.id)

    update_company_trade_types(db, db_item.id, person.trades)
    db.refresh(db_item)
    return person


def update_person(db: Session, contact_id: int, person: schemas.Person):
    db_item = get_contact(db, contact_id)

    if db_item is None:
        return None

    db_item.name = person.last_name + ", " + person.first_name
    db_item.first_name = person.first_name
    db_item.last_name = person.last_name
    db_item.role = person.role
    db_item.address = person.address
    db_item.main_telephone = person.main_telephone
    db_item.direct_telephone = person.direct_telephone
    db_item.mobile_phone = person.mobile_phone
    db_item.email = person.email
    db_item.direct_email = person.direct_email
    db_item.tax_id = person.tax_id
    db_item.discount = person.discount
    db_item.note = person.note
    db_item.payment_terms = person.payment_terms
    db_item.payment_status = person.payment_status
    db_item.image = person.image

    if person.company_id != contact_id:
        db_item.company_id = person.company_id

        next_db = crm.get_db()
        create_relationship(next_db, person.company_id, contact_id)

    db.query(models.Address).filter(
        models.Address.contact_id == contact_id).delete()
    for new_address in person.address_field:
        db_item.address_field.append(
            models.Address(
                **new_address.dict(exclude={"contact_id", "translations"}))
        )

    db.commit()
    db.refresh(db_item)
    return db_item


def update_person_photo(db: Session, contact_id: int, img: str):
    db_item = get_contact(db, contact_id)

    if db_item is None:
        return db_item

    db_item.image = img
    db.commit()
    db.refresh(db_item)
    return db_item


async def delete_contact(db: Session, contact_id: int):
    # try:
    #     sales_db_generator = deps.get_db()
    #     sales_db: Session = next(sales_db_generator)
    #     transactions = sales_crud.get_transactions_by_customer_id(
    #         sales_db, contact_id)
    #     if len(transactions) > 0:
    #         raise IntegrityError(None, None, None)

    db_item = get_contact(db, contact_id)

    if db_item is None:
        return None

    db.delete(db_item)
    db.commit()

    return contact_id
    # except IntegrityError:
    #     raise HTTPException(status_code=405, detail="Dependency error occurs")


def get_companies(db: Session, country_id: int, skip: int = 0, limit: int = 100):
    companies = db.query(models.Contact).filter(
        models.Contact.country_id == country_id)
    companies = companies.filter(
        models.Contact.contact_type == enums.ContactTypes.company
    )
    return companies.offset(skip).limit(limit).all()


def create_company(db: Session, company: schemas.Company):
    db_item = models.Contact(
        **company.dict(
            exclude={
                "trades",
                "address_field",
                "company_name",
                "has_parent_company",
                "persons",
            }
        )
    )
    for new_address in company.address_field:
        db_item.address_field.append(
            models.Address(
                **new_address.dict(exclude={"contact_id", "translations"}))
        )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    company.id = db_item.id

    if company.company_id != company.id:
        db_item.company_id = company.company_id

        next_db = crm.get_db()
        create_relationship(next_db, company.company_id, company.id)

    update_company_trade_types(db, db_item.id, company.trades)
    db.refresh(db_item)
    return db_item


def update_company(db: Session, contact_id: int, company: schemas.Company):
    db_item = get_contact(db, contact_id)

    if db_item is None:
        return None

    db_item.name = company.name
    db_item.industry = company.industry
    db_item.address = company.address
    db_item.main_telephone = company.main_telephone
    db_item.direct_telephone = company.direct_telephone
    db_item.mobile_phone = company.mobile_phone
    db_item.email = company.email
    db_item.direct_email = company.direct_email
    db_item.business_hours = company.business_hours
    db_item.tax_id = company.tax_id
    db_item.is_supplier = company.is_supplier
    db_item.discount = company.discount
    db_item.note = company.note
    db_item.payment_terms = company.payment_terms
    db_item.payment_status = company.payment_status
    db_item.shop_url = company.shop_url
    db_item.image = company.image

    db.query(models.Address).filter(
        models.Address.contact_id == contact_id).delete()
    for new_address in company.address_field:
        db_item.address_field.append(
            models.Address(
                **new_address.dict(exclude={"contact_id", "translations"}))
        )

    if company.company_id != contact_id:
        db_item.company_id = company.company_id

        next_db = crm.get_db()
        create_relationship(next_db, company.company_id, contact_id)

    db.commit()
    db.refresh(db_item)
    return db_item


def update_company_photo(db: Session, contact_id: int, img: str):
    db_item = get_contact(db, contact_id)

    if db_item is None:
        return db_item

    db_item.image = img
    db.commit()
    db.refresh(db_item)
    return db_item


def get_company_trade_types(db: Session, contact_id: int):
    contact = db.query(models.Contact).get(contact_id)
    return contact.trades


def get_company_sub_contacts(db: Session, contact_id: int):
    company = db.query(models.Contact).get(contact_id)
    return company.sub_contacts


def update_company_trade_types(
    db: Session, contact_id: int, trade_types: list[schemas.TradeType]
):
    contact = db.query(models.Contact).get(contact_id)
    contact.trades.clear()
    db.commit()

    for new_trade in trade_types:
        try:
            db.execute(
                models.contact_trades.insert(),
                params={"company_id": contact_id,
                        "trade_type_id": new_trade.id},
            )
        except IntegrityError:
            continue

    db.commit()
    return trade_types


def get_trade_types(db: Session):
    return db.query(models.TradeType).all()


def create_trade_type(db: Session, trade_type: schemas.TradeTypeBase):
    db_item = models.TradeType(**trade_type.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_trade_type(db: Session, trade_type_id: int, trade_type: schemas.TradeType):
    db_item = db.query(models.TradeType).get(trade_type_id)

    if db_item is None:
        return db_item

    db_item.abbr = trade_type.abbr
    db_item.description = trade_type.description
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_trade_type(db: Session, trade_type_id: int):
    db_item = db.query(models.TradeType).get(trade_type_id)

    if db_item is None:
        return db_item

    db.delete(db_item)
    db.commit()
    return db_item


def get_contacts(
    db: Session,
    country_id: int,
    contact_ids: list[int],
    offset: int = 0,
    limit: int = 500,
    sort_column: str = "id",
    sort_direction: str = "desc",
):
    if contact_ids is not None:
        return db.query(models.Contact).filter(models.Contact.id.in_(contact_ids)).all()

    fields = ["id", "name", "email", "address",
              "main_telephone", "contact_type"]
    contacts = (
        db.query(models.Contact)
        # todo: solve this issue ORM problem
        # .options(load_only(*fields), joinedload(models.Contact.sub_contacts))
        .filter(models.Contact.country_id == country_id)
    )

    sortable_columns = {
        "id": models.Contact.id,
        "name": models.Contact.name,
        "email": models.Contact.email,
        "address": models.Contact.address,
        "main_telephone": models.Contact.main_telephone,
    }

    sort = (
        sortable_columns.get(sort_column).desc()
        if sort_direction == "desc"
        else sortable_columns.get(sort_column).asc()
    )

    filtered_contacts = contacts.order_by(
        sort).offset(offset).limit(limit).all()

    contacts_to_return = []
    for filtered_contact in filtered_contacts:
        if filtered_contact.company_id is not None:
            affiliated_company = db.query(models.Contact).get(
                filtered_contact.company_id
            )
            filtered_contact.company_name = affiliated_company.name
        contacts_to_return.append(filtered_contact)
    return contacts_to_return


def search_contact(
    db: Session,
    contact_type: str,
    filters: str,
    query: str,
    country: int,
    offset: int = 0,
    limit: int = 1,
    sort_column: str = "id",
    sort_direction: str = "asc",
):
    fields = [
        "id",
        "name",
        "email",
        "address",
        "direct_email",
        "direct_telephone",
        "discount",
        "main_telephone",
        "contact_type",
        "company_id",
        "first_name",
        "last_name",
    ]
    contacts = (
        db.query(models.Contact)
        .options(
            # todo: solve this issue ORM problem
            #     load_only(*fields),
            #     joinedload(models.Contact.sub_contacts).joinedload(
            #         models.Contact.address_field
            # )
            joinedload(models.Contact.payment_term),
            joinedload(models.Contact.address_field),
            joinedload(models.Contact.trades),
        )
        .filter(models.Contact.country_id == country)
    )

    if contact_type == "company" or contact_type == "person":
        contacts = contacts.filter(models.Contact.contact_type == contact_type)
    elif contact_type == "supplier":
        contacts = (
            db.query(models.Contact)
            .options(
                # todo: solve this issue ORM problem
                # load_only(*fields),
                # joinedload(models.Contact.sub_contacts).joinedload(
                #     models.Contact.address_field
                # ),
                joinedload(models.Contact.payment_term),
                joinedload(models.Contact.address_field),
                joinedload(models.Contact.trades),
            )
            .filter(models.Contact.is_supplier == 1)
        )

    sortable_columns = {
        "id": models.Contact.id,
        "name": models.Contact.name,
        "email": models.Contact.email,
        "direct_email": models.Contact.direct_email,
        "direct_telephone": models.Contact.direct_telephone,
        "address": models.Contact.address,
        "main_telephone": models.Contact.main_telephone,
    }

    if sort_direction == "desc":
        sort = sortable_columns.get(sort_column).desc()
    else:
        sort = sortable_columns.get(sort_column).asc()

    if query is None:
        if limit > 0:
            filtered_contacts = (
                contacts.order_by(sort).offset(offset).limit(limit).all()
            )
        else:
            filtered_contacts = contacts.order_by(sort).all()
    else:
        # 	We declared lists to be passed later to the query filter as *args
        criteria = []
        criterion_name = models.Contact.name.like(f"%{query}%")
        criterion_email = models.Contact.email.like(f"%{query}%")
        criterion_contact = models.Contact.main_telephone.like(f"%{query}%")
        criterion_address = models.Contact.address.like(f"%{query}%")

        # 	if a filter is matches we will add it to the main criterion
        filters = filters.split("+")
        if "name" in filters:
            criteria.append(criterion_name)
        if "email" in filters:
            criteria.append(criterion_email)
        if "contact" in filters:
            criteria.append(criterion_contact)
        if "address" in filters:
            criteria.append(criterion_address)

        if limit > 0:
            filtered_contacts = (
                contacts.filter(or_(*criteria))
                .order_by(sort)
                .offset(offset)
                .limit(limit)
                .all()
            )
        else:
            filtered_contacts = contacts.filter(
                or_(*criteria)).order_by(sort).all()

    for filtered_contact in filtered_contacts:
        if filtered_contact.company_id is not None:
            affiliated_company = db.query(models.Contact).get(
                filtered_contact.company_id
            )
            filtered_contact.company_name = affiliated_company.name
        yield filtered_contact


def get_note(db: Session, contact_id: int, contact_type: str):
    rtf_data = (
        db.query(models.Contact.note).filter(
            models.Contact.id == contact_id).scalar()
    )
    return {"rtf_data": rtf_data}


def update_note(
    db: Session, note: schemas.ContactNotes, contact_id: int, contact_type: str
):
    db_item = db.query(models.Contact).get(contact_id)

    if db_item is None:
        return db_item

    db_item.note = note.rtf_data
    db.commit()
    db.refresh(db_item)
    return db_item


def create_relationship(db: Session, empr_id: int, empe_id: int):
    try:
        sql = "INSERT INTO crm_employee_employer_relationships VALUES (:empr_id, :empe_id)"
        db.execute(text(sql), {"empr_id": empr_id, "empe_id": empe_id})
        db.commit()
    except IntegrityError:
        db.rollback()


def get_relationship_employers(db: Session, empe_id: int):
    employee = db.query(models.Contact).get(empe_id)
    return employee.super_contacts


def get_relationship_employees(db: Session, empr_id: int):
    employee = db.query(models.Contact).get(empr_id)
    return employee.sub_contacts


def delete_relationship(db: Session, empr_id: int, empe_id: int):
    sql = "DELETE FROM crm_employee_employer_relationships WHERE empr_id= :empr_id AND empe_id= :empe_id"
    db.execute(text(sql), {"empr_id": empr_id, "empe_id": empe_id})
    db.commit()


def insert_file(db: Session, attached_file: schemas.AttachedFileCreate):
    db_item = models.AttachedFile(**attached_file.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_file(db: Session, contact_id: int, attached_file: schemas.AttachedFile):
    db_item = db.query(models.AttachedFile).get(attached_file.id)
    db_item.subject = attached_file.subject
    db.commit()
    return db_item


def read_files(db: Session, contact_id: int):
    db_item = (
        db.query(models.AttachedFile)
        .filter(models.AttachedFile.contact_id == contact_id)
        .all()
    )
    return db_item


def delete_file(db: Session, id: int):
    db_item = db.query(models.AttachedFile).get(id)

    if db_item is None:
        return db_item

    db.delete(db_item)
    db.commit()
    return db_item


def create_relationship_from_csv(db: Session, company_id: int, person_id: int):
    employees = get_relationship_employees(db=db, empr_id=company_id)
    employee_id_list = []
    for employee in employees:
        employee_id_list.append(employee.id)

    if person_id not in employee_id_list:
        create_relationship(db=db, empr_id=company_id, empe_id=person_id)


def insert_company_from_csv(db: Session, csv_contact: schemas.CSVContacts):
    company = (
        db.query(models.Contact)
        .filter(
            models.Contact.contact_type == enums.ContactTypes.company,
            models.Contact.country_id == csv_contact.country_id,
            models.Contact.name == csv_contact.name,
        )
        .all()
    )
    if company:
        company_id = update_company(
            db=db, contact_id=company[0].id, company=csv_contact
        ).id
    else:
        company_id = create_company(db=db, company=csv_contact).id

    if csv_contact.persons:
        for person in csv_contact.persons:
            person_id = insert_person_from_csv(db, person)
            create_relationship(db, company_id, person_id)


def insert_person_from_csv(db: Session, csv_contact: schemas.CSVContacts):
    person = (
        db.query(models.Contact)
        .filter(
            models.Contact.contact_type == enums.ContactTypes.person,
            models.Contact.country_id == csv_contact.country_id,
            models.Contact.name == csv_contact.name,
        )
        .all()
    )
    if person:
        person_id = update_person(
            db=db, contact_id=person[0].id, person=csv_contact).id
    else:
        person_id = create_person(db=db, person=csv_contact).id

    return person_id


def import_contacts(db: Session, csv_contacts: list[schemas.CSVContacts]) -> None:
    for contact in csv_contacts:
        if contact.contact_type == enums.ContactTypes.person:
            insert_person_from_csv(db=db, csv_contact=contact)
        else:
            insert_company_from_csv(db=db, csv_contact=contact)


def create_shop_account(db: Session, shop_account: schemas.ShopAccountCreate):
    shop_account_model = models.ShopAccount(**shop_account.dict())
    db.add(shop_account_model)
    db.commit()
    db.refresh(shop_account_model)

    return shop_account_model


def update_shop_account(
    db: Session, shop_account_id: int, shop_account: schemas.ShopAccount
):
    shop_account_model = db.query(models.ShopAccount).get(shop_account_id)

    if shop_account_model is None:
        return

    shop_account_model = models.ShopAccount(**shop_account.dict())
    db.commit()
    db.refresh(shop_account_model)

    return shop_account_model


def delete_shop_account(db: Session, shop_account_id: int):
    shop_account_model = db.query(models.ShopAccount).get(shop_account_id)

    if shop_account_model is None:
        return

    db.delete(shop_account_model)
    db.commit()


def get_contact_shop_accounts(db: Session, user_id: int, contact_id):
    shop_accounts = (
        db.query(models.ShopAccount)
        .filter(
            or_(
                models.ShopAccount.contact_id == contact_id,
                models.ShopAccount.user_id == user_id,
                models.ShopAccount.is_global == 1,
            )
        )
        .all()
    )

    return shop_accounts


def update_contact_address(db: Session, contact_id: int, address: ContactAddress):
    contact = db.query(models.Contact).get(contact_id)

    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")

    contact.address = address.crm_format
    db.query(models.Address).filter(
        models.Address.contact_id == contact_id).delete()
    contact_address = models.Address(**address.dict(exclude={"translations"}))
    contact.address_field.append(contact_address)
    db.commit()
