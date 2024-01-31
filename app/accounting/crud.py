from datetime import timedelta, datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from app.accounting import schemas, models
from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError


def get_frames(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    frame_db = db.query(models.Frame)

    sortable_columns = {
        "name": models.Frame.name,
    }

    sort = (
        sortable_columns.get("name").asc()
        if sort_direction == "desc"
        else sortable_columns.get("name").desc()
    )

    filtered_result = frame_db.order_by(
        sort).offset(skip).limit(limit).all()
    return filtered_result


def create_frame(db: Session, frame: schemas.FrameCreate):
    code = db.query(models.Frame).filter(
        models.Frame.code == frame.code, models.Frame.is_deleted == 0).first()
    if code:
        raise HTTPException(
            status_code=404, detail="Code already exist.")

    db_frame = models.Frame(**frame.dict())
    db.add(db_frame)
    db.commit()
    db.refresh(db_frame)
    return db_frame


def update_frame(db: Session, id: int, frame: schemas.FrameCreate):
    db_frame = db.query(models.Frame).get(id)

    if db_frame is None:
        raise HTTPException(status_code=404, detail="Account Frame not found.")

    if db_frame is not None:
        db_frame.name = frame.name
        db_frame.report_type = frame.report_type
        db_frame.code = frame.code

        db.commit()
        db.refresh(db_frame)
        return db_frame


def delete_frame(db: Session, id: int):
    chart = db.query(models.Chart).filter(models.Chart.frame_id == id).first()

    if chart is not None:
        transactions = db.query(models.Transaction).filter(
            models.Transaction.chart_id == chart.id).first()
        if transactions:
            raise HTTPException(
                status_code=404, detail="Cannot be deleted. Frame have chart/s in use.")
        else:
            charts = db.query(models.Chart).filter(
                models.Chart.frame_id == id).all()

            for cht in charts:
                delete_chart(db=db, id=cht.id)

    db_frame = db.query(models.Frame).get(id)

    if db_frame is None:
        raise HTTPException(status_code=404, detail="Account Frame not found.")

    if db_frame is not None:
        db_frame.name = db_frame.name
        db_frame.report_type = db_frame.report_type
        db_frame.code = db_frame.code
        db_frame.is_deleted = 1

        db.commit()
        db.refresh(db_frame)
        return db_frame


def get_charts(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 500):
    charts_db = db.query(models.Chart)

    sortable_columns = {
        "name": models.Chart.name,
    }

    sort = (
        sortable_columns.get("name").asc()
        if sort_direction == "desc"
        else sortable_columns.get("name").desc()
    )

    filtered_result = charts_db.order_by(
        sort).offset(skip).limit(limit).all()
    return filtered_result


def get_charts_by_frame(db: Session, frame_id: int, sort_direction: str = "desc"):
    sortable_columns = {
        "name": models.Chart.name,
    }

    sort = (
        sortable_columns.get("name").asc()
        if sort_direction == "desc"
        else sortable_columns.get("name").desc()
    )

    charts_db = db.query(models.Chart).filter(
        models.Chart.frame_id == frame_id).order_by(sort).all()

    return charts_db


def create_chart(db: Session, chart: schemas.ChartCreate):
    frame = db.query(models.Frame).filter(
        models.Frame.id == chart.frame_id).first()

    if not frame:
        raise HTTPException(
            status_code=404, detail="Account Frame does not exist.")

    code = db.query(models.Chart).filter(
        models.Chart.frame_id == chart.frame_id, models.Chart.code == chart.code, models.Chart.is_deleted == 0).first()
    if code:
        raise HTTPException(
            status_code=404, detail="Code already exist.")

    db_chart = models.Chart(**chart.dict())
    db.add(db_chart)
    db.commit()
    db.refresh(db_chart)
    return db_chart


def update_chart(db: Session, id: int, chart: schemas.ChartCreate):
    db_chart = db.query(models.Chart).get(id)

    if db_chart is None:
        raise HTTPException(status_code=404, detail="Accounts not found.")

    if db_chart is not None:
        db_chart.frame_id = chart.frame_id
        db_chart.name = chart.name
        db_chart.account_type = chart.account_type
        db_chart.code = chart.code

        db.commit()
        db.refresh(db_chart)
        return db_chart


def delete_chart(db: Session, id: int):
    transaction = db.query(models.Transaction).filter(
        models.Transaction.chart_id == id).first()

    if transaction is not None:
        raise HTTPException(
            status_code=404, detail="Cannot be deleted. Account in use.")

    db_chart = db.query(models.Chart).get(id)

    if db_chart is None:
        raise HTTPException(status_code=404, detail="Account not found.")

    if db_chart is not None:
        db_chart.frame_id = db_chart.frame_id
        db_chart.name = db_chart.name
        db_chart.account_type = db_chart.account_type
        db_chart.code = db_chart.code
        db_chart.is_deleted = 1

        db.commit()
        db.refresh(db_chart)
        return db_chart


def get_companies(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    charts_db = db.query(models.Company)

    sortable_columns = {
        "code": models.Company.code,
    }

    sort = (
        sortable_columns.get("code").asc()
        if sort_direction == "desc"
        else sortable_columns.get("code").desc()
    )

    filtered_result = charts_db.order_by(
        sort).offset(skip).limit(limit).all()
    return filtered_result


def create_company(db: Session, company: schemas.CompanyCreate):
    code = db.query(models.Company).filter(
        models.Company.code == company.code, models.Company.is_deleted == 0).first()
    if code:
        raise HTTPException(
            status_code=404, detail="Code already exist.")

    db_company = models.Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def update_company(db: Session, id: int, company: schemas.CompanyCreate):
    db_company = db.query(models.Company).get(id)

    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found.")

    if db_company is not None:
        db_company.name = company.name
        db_company.code = company.code

        db.commit()
        db.refresh(db_company)
        return db_company


def delete_company(db: Session, id: int):
    transaction = db.query(models.Transaction).filter(
        models.Journal.company_id == id).first()

    if transaction is not None:
        raise HTTPException(
            status_code=404, detail="Cannot be deleted. Company have transaction/s.")

    departments = db.query(models.Department).filter(
        models.Department.company_id == id).all()

    if departments is not None:
        journals = db.query(models.Journal).filter(
            models.Journal.department_id == id).first()
        if journals:
            raise HTTPException(
                status_code=404, detail="Cannot be deleted. Company have departments in use.")
        else:
            for dept in departments:
                delete_department(db=db, id=dept.id)

    db_company = db.query(models.Company).get(id)

    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found.")

    if db_company is not None:
        db_company.name = db_company.name
        db_company.code = db_company.code
        db_company.is_deleted = 1

        db.commit()
        db.refresh(db_company)
        return db_company


def get_departments(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    charts_db = db.query(models.Department)

    sortable_columns = {
        "code": models.Department.code,
    }

    sort = (
        sortable_columns.get("code").asc()
        if sort_direction == "desc"
        else sortable_columns.get("code").desc()
    )

    filtered_result = charts_db.order_by(
        sort).offset(skip).limit(limit).all()
    return filtered_result


def get_departments_by_company(db: Session, company_id: int):
    departments_db = db.query(models.Department).filter(
        models.Department.company_id == company_id).all()

    return departments_db


def create_department(db: Session, department: schemas.DepartmentCreate):
    company = db.query(models.Company).filter(
        models.Company.id == department.company_id).first()

    if not company:
        raise HTTPException(status_code=404, detail="Company dont exist.")

    code = db.query(models.Department).filter(
        models.Department.company_id == department.company_id, models.Department.code == department.code, models.Department.is_deleted == 0).first()
    if code:
        raise HTTPException(
            status_code=404, detail="Code already exist.")

    db_dept = models.Department(**department.dict())
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept


def update_department(db: Session, id: int, department: schemas.DepartmentCreate):
    db_dept = db.query(models.Department).get(id)
    company = db.query(models.Company).filter(
        models.Company.id == department.company_id).first()

    if not company:
        raise HTTPException(status_code=404, detail="Company dont exist.")

    if db_dept is None:
        raise HTTPException(status_code=404, detail="Department not found.")

    if db_dept is not None:
        db_dept.company_id = department.company_id
        db_dept.name = department.name
        db_dept.code = department.code

        db.commit()
        db.refresh(db_dept)
        return db_dept


def delete_department(db: Session, id: int):
    transaction = db.query(models.Transaction).filter(
        models.Journal.department_id == id).first()

    if transaction is not None:
        raise HTTPException(
            status_code=404, detail="Cannot be deleted. Department have transaction/s.")

    db_dept = db.query(models.Department).get(id)

    if db_dept is None:
        raise HTTPException(status_code=404, detail="Department not found.")

    if db_dept is not None:
        db_dept.name = db_dept.name
        db_dept.code = db_dept.code
        db_dept.is_deleted = 1

        db.commit()
        db.refresh(db_dept)
        return db_dept


def get_transactions(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    transaction_db = db.query(models.Transaction)

    sortable_columns = {
        "id": models.Transaction.id,
    }

    sort = (
        sortable_columns.get("id").asc()
        if sort_direction == "desc"
        else sortable_columns.get("id").desc()
    )

    filtered_result = transaction_db.order_by(
        sort).offset(skip).limit(limit).all()
    return filtered_result


def create_transaction(db: Session, journal_id: int, transaction_data: schemas.TransactionCreate):
    transaction_data_dict = transaction_data.dict(exclude={"journal_id"})
    transaction = models.Transaction(
        journal_id=journal_id, **transaction_data_dict)
    db.add(transaction)
    return transaction


def update_transaction(db: Session, id: int, transaction: schemas.TransactionCreate):
    chart = db.query(models.Chart).filter(
        models.Chart.id == transaction.chart_id).first()
    if not chart:
        raise HTTPException(
            status_code=404, detail="Chart of Account doesn't exist.")

    db_transaction = db.query(models.Transaction).get(id)

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found.")

    if db_transaction is not None:
        db_transaction.chart_id = transaction.chart_id
        db_transaction.amount = transaction.amount
        db_transaction.particulars = transaction.particulars
        db_transaction.is_type = transaction.is_type

        db.commit()
        db.refresh(db_transaction)
        return db_transaction


def delete_transaction(db: Session, id: int):
    db_transaction = db.query(models.Transaction).get(id)

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found.")

    if db_transaction is not None:
        db.delete(db_transaction)
        db.commit()
        return db_transaction


def get_journals_by_id(db: Session, id: int):
    journal_db = db.query(models.Journal).get(id)

    return journal_db


def get_all_journals_and_transactions(db: Session):
    journals = db.query(models.Journal).all()

    sortable_columns = {
        "is_type": models.Transaction.is_type,
    }

    sort = (
        sortable_columns.get("is_type").asc()
    )

    journal_list = []
    for journal in journals:
        transactions = db.query(models.Transaction).filter(
            models.Transaction.journal_id == journal.id).order_by(sort).all()

        journal_data = {
            "id": journal.id,
            "supplier_id": journal.supplier_id,
            "company_id": journal.company_id,
            "department_id": journal.department_id,
            "notes": journal.notes,
            "reference_no": journal.reference_no,
            "date": journal.date.strftime("%Y-%m-%d %H:%M:%S"),
            "is_supplier": journal.is_supplier,
            "transactions": [
                {
                    "id": transaction.id,
                    "chart_id": transaction.chart_id,
                    "amount": str(transaction.amount),
                    "particulars": transaction.particulars,
                    "is_type": transaction.is_type,
                }
                for transaction in transactions
            ],
        }
        journal_list.append(journal_data)

    return journal_list


def create_journal(db: Session, journal: schemas.JournalCreate):
    company = db.query(models.Company).filter(
        models.Company.id == journal.company_id).first()
    if not company:
        raise HTTPException(
            status_code=404, detail="Company doesn't exist.")

    if journal.department_id:
        department = db.query(models.Department).filter(
            models.Department.id == journal.department_id).first()
        if not department:
            raise HTTPException(
                status_code=404, detail="Department doesn't exist.")

    journal_db = models.Journal(**journal.dict(exclude={"transactions"}))
    db.add(journal_db)
    db.commit()
    db.refresh(journal_db)
    return journal_db


def create_journal_and_transactions(
    journal: schemas.JournalCreate,
    db: Session,
):

    journal_db = create_journal(db, journal)
    db.add(journal_db)

    transactions = []
    for data in journal.transactions:
        transaction = create_transaction(db, journal_db.id, data)
        transactions.append(transaction)

    db.add_all(transactions)
    db.commit()
    return journal


def update_journal_and_transactions(
    id: int,
    journal: schemas.Journal,
    db: Session,
):

    journal_db = update_journal(db, id, journal=journal)
    db.add(journal_db)

    existing_transactions = db.query(models.Transaction).filter(
        models.Transaction.journal_id == id).all()

    transactions = []
    for data in journal.transactions:
        if data.id:
            transaction = update_transaction(db, data.id, data)
        else:
            # transactions_db = db.query(models.Transaction).filter(
            #     models.Transaction.journal_id == id).all()

            # if transactions_db:
            #     delete_transactions_by_journal_id(db=db, id=id)

            transaction = create_transaction(db, id, data)

        transactions.append(transaction)

    for existing_transaction in existing_transactions:
        if existing_transaction.id not in [data.id for data in journal.transactions]:
            db.delete(existing_transaction)

    db.add_all(transactions)
    db.commit()

    return journal


def update_journal(db: Session, id: int, journal: schemas.JournalCreate):
    journal_db = db.query(models.Journal).get(id)

    if journal_db is None:
        raise HTTPException(status_code=404, detail="Journal Entry not found.")

    company = db.query(models.Company).filter(
        models.Company.id == journal.company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company doesn't exist.")

    if journal.department_id:
        department = db.query(models.Department).filter(
            models.Department.id == journal.department_id).first()
        if not department:
            raise HTTPException(
                status_code=404, detail="Department doesn't exist.")

    if journal_db:
        journal_db.supplier_id = journal.supplier_id
        journal_db.company_id = journal.company_id
        journal_db.department_id = journal.department_id
        journal_db.reference_no = journal.reference_no
        journal_db.date = journal.date
        journal_db.notes = journal.notes
        journal_db.is_supplier = journal.is_supplier

        db.commit()
        db.refresh(journal_db)
        return journal_db


def delete_transactions_by_journal_id(db: Session, id: int):
    transactions_db = db.query(models.Transaction).filter(
        models.Transaction.journal_id == id).all()

    if transactions_db is None:
        raise HTTPException(status_code=404, detail="No transaction found.")

    if transactions_db:
        for transaction in transactions_db:
            db.delete(transaction)

        db.commit()


def delete_journal(db: Session, id: int):
    journal_db = db.query(models.Journal).get(id)

    if journal_db is None:
        raise HTTPException(status_code=404, detail="Journal Entry not found.")

    if journal_db is not None:
        db.delete(journal_db)
        db.commit()
        return journal_db


def get_journals_by_frame(db: Session, from_date: str, to_date: str, frame_id: int = 0, chart_id: int = 0, company_ids: List[int] = None, department_ids: List[int] = None, supplier_id: int = 0):
    frames = db.query(models.Frame).options(joinedload(
        models.Frame.charts).joinedload(models.Chart.transaction)).all()

    if not from_date or not to_date:
        raise HTTPException(
            status_code=404, detail="Both from_date and to_date must be provided and not empty.")

     # Validate date format
    try:
        from_date = datetime.strptime(from_date, '%Y-%m-%d')
        to_date = datetime.strptime(to_date, '%Y-%m-%d')
    except ValueError:
        raise HTTPException(
            status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD' format.")

    frames = [{
        "id": frame.id,
        "name": frame.name,
        "report_type": frame.report_type,
        "code": frame.code,
        "created_at": frame.created_at,
        "is_deleted": frame.is_deleted,
        "parent_id": 0,
        "sub_accounts": [{
            "id": chart.id,
            "name": chart.name,
            "account_type": chart.account_type,
            "code": chart.code,
            "created_at": chart.created_at,
            "parent_id": chart.frame_id,
            "transactions": [{
                "id": transaction.id,
                "company_id": transaction.journal.company_id,
                "department_id": transaction.journal.department_id,
                "supplier_id": transaction.journal.supplier_id,
                "particulars": transaction.particulars,
                "reference_no": transaction.journal.reference_no,
                "date": transaction.journal.date,
                "notes": transaction.journal.notes,
                "is_supplier": transaction.journal.is_supplier,
                "amount": transaction.amount,
                "is_type": transaction.is_type,
            } for transaction in chart.transaction if transaction.journal is not None and
                ((not company_ids or transaction.journal.company_id in company_ids) and
                 (not department_ids or transaction.journal.department_id in department_ids) and
                 (supplier_id == 0 or transaction.journal.supplier_id == supplier_id) and
                 (from_date <= transaction.journal.date <= to_date + timedelta(days=1)))]

        } for chart in frame.charts if ((chart_id == 0 or chart.id == chart_id))]
    } for frame in frames if ((frame_id == 0 or frame.id == frame_id))]

    return frames


def insert_journal_from_csv(db: Session, csv_journal: schemas.JournalCreate):

    journal = (
        db.query(models.Journal)
        .filter(models.Journal.reference_no == csv_journal.reference_no)
        .first()
    )

    if journal:
        db_journal = update_journal_and_transactions(
            db=db, id=journal.id, journal=csv_journal)
    else:
        db_journal = create_journal_and_transactions(
            db=db, journal=csv_journal)

    return db_journal


def import_journals(db: Session, csv_journals: list[schemas.JournalCreate]) -> None:
    for journal in csv_journals:
        insert_journal_from_csv(db=db, csv_journal=journal)

# # Generate Invoice Number Only for QR Bill Generation Process in Billing


# def create_invoice_number(db: Session, invoice: schemas.InvoiceCreate):
#     # from xojo: 2023-03-13 03:36:22
#     # disallow duplicate invoice number
#     try:
#         db_invoice = models.Invoice(
#             project_id=invoice.project_id,
#             client_id=invoice.client_id,
#             invoice_number=generate_invoice_number_for_qrbill(
#                 invoice.invoice_date, invoice.client_id, invoice.project_id
#             ),
#             amount=0,
#             qr_reference_number="",
#             invoice_date=invoice.invoice_date,
#             invoice_due_date=invoice.invoice_due_date,
#             invoice_status="",
#         )

#         db.add(db_invoice)
#         db.commit()
#         db.refresh(db_invoice)

#         return db_invoice

#     except IntegrityError:
#         db.rollback()
#         raise HTTPException(
#             status_code=409, detail="Invoice number already exists.")

#     # Invoice Number Generator


# def generate_invoice_number_for_qrbill(
#     invoice_date: str = "", client_id: int = 0, project_id: int = 0
# ):
#     invoice_number = 0

#     # year = str(datetime.today().year)
#     # month = str(datetime.today().strftime("%m"))
#     # day = str(datetime.today().strftime("%d"))
#     # hour = str(datetime.today().strftime("%H"))
#     # minutes = str(datetime.today().strftime("%M"))
#     # seconds = str(datetime.today().strftime("%S"))
#     # mseconds = str(datetime.today().strftime("%f"))

#     # date = year + month + day
#     # dtime = hour + minutes + seconds #+ mseconds

#     str_client_id = str(client_id)
#     str_project_id = str(project_id)

#     inv_client_id = ""
#     for i in range(4 - len(str_client_id)):
#         inv_client_id = inv_client_id + "0"

#     inv_project_id = ""
#     for i in range(3 - len(str_project_id)):
#         inv_project_id = inv_project_id + "0"

#     # invoice_number = date + dtime + "-" + inv_client_id + str_client_id + "-" + inv_project_id + str_project_id

#     invoice_date = str(invoice_date).replace("-", "")
#     invoice_date = str(invoice_date).replace(" ", "")
#     invoice_date = str(invoice_date).replace(":", "")
#     # invoice_date = invoice_date.replace(",", "")

#     invoice_number = (
#         invoice_date
#         + "-"
#         + inv_client_id
#         + str_client_id
#         + "-"
#         + inv_project_id
#         + str_project_id
#     )

#     return invoice_number
# def get_suppliers(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
#     supplier_db = db.query(models.Supplier)

#     sortable_columns = {
#         "id": models.Supplier.id,
#     }

#     sort = (
#         sortable_columns.get("id").asc()
#         if sort_direction == "desc"
#         else sortable_columns.get("id").desc()
#     )

#     filtered_result = supplier_db.order_by(
#         sort).offset(skip).limit(limit).all()
#     return filtered_result


# def create_supplier(db: Session, supplier: schemas.SupplierCreate):
#     db_supplier = models.Supplier(**supplier .dict())
#     db.add(db_supplier)
#     db.commit()
#     db.refresh(db_supplier)
#     return db_supplier


# def update_supplier(db: Session, id: int, supplier: schemas.SupplierCreate):
#     db_supplier = db.query(models.Supplier).get(id)

#     if db_supplier is None:
#         raise HTTPException(status_code=404, detail="Supplier not found.")

#     if db_supplier is not None:
#         db_supplier.business_type = supplier.business_type
#         db_supplier.first_name = supplier.first_name
#         db_supplier.last_name = supplier.last_name
#         db_supplier.email = supplier.email
#         db_supplier.contact_number = supplier.contact_number
#         db_supplier.tel_number = supplier.tel_number
#         db_supplier.address = supplier.address
#         db_supplier.tin = supplier.tin
#         db_supplier.sec_registration = supplier.sec
#         db_supplier.dti_registration = supplier.dti

#         db.commit()
#         db.refresh(db_supplier)
#         return db_supplier


# def delete_supplier(db: Session, id: int):
#     db_supplier = db.query(models.Supplier).get(id)

#     if db_supplier is None:
#         raise HTTPException(status_code=404, detail="Supplier not found.")

#     if db_supplier is not None:
#         db.delete(db_supplier)
#         db.commit()
#         return db_supplier

# def get_latest_debit_balance(db: Session):
#     balance_debit_db = db.query(models.Debit).order_by(models.Debit.created_at.desc()).first()

#     if balance_debit_db is None:
#         raise HTTPException(status_code=404, detail="Not found.")

#     return balance_debit_db

# def create_debit(db: Session, debit: schemas.DebitCreate):
#     db_debit = models.Debit(**debit.dict())
#     db.add(db_debit)
#     db.commit()
#     db.refresh(db_debit)
#     return db_debit

# def get_latest_credit_balance(db: Session):
#     balance_credit_db = db.query(models.Credit).order_by(models.Credit.created_at.desc()).first()

#     if balance_credit_db is None:
#         raise HTTPException(status_code=404, detail="Not found.")

#     return balance_credit_db

# def create_credit(db: Session, credit: schemas.CreditCreate):
#     db_credit = models.Credit(**credit.dict())
#     db.add(db_credit)
#     db.commit()
#     db.refresh(db_credit)
#     return db_credit
