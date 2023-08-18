from sqlalchemy.orm import Session
from app.accounting import schemas, models
from fastapi import HTTPException, status
from datetime import datetime, timedelta

#### CHART OF ACCOUNT RESOURCES

# Get All Chart of Account
def get_charts(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    charts_db = db.query(models.Chart)
    
    sortable_columns = {
        "id": models.Chart.id,
    }

    sort = (
        sortable_columns.get("id").asc()
        if sort_direction == "desc"
        else sortable_columns.get("id").desc()
    )

    filtered_result = charts_db.order_by(
        sort).offset(skip).limit(limit).all()
    return filtered_result

# Create Chart of Account
def create_chart(db: Session, chart: schemas.ChartCreate):
    db_chart = models.Chart(**chart.dict())
    db.add(db_chart)
    db.commit()
    db.refresh(db_chart)
    return db_chart

# Update Chart of Account
def update_chart(db: Session, id: int, chart: schemas.ChartCreate):
    db_chart = db.query(models.Chart).get(id)

    if db_chart is None:
        raise HTTPException(status_code=404, detail="Chart of Account not found.")

    if db_chart is not None:
        db_chart.account_name = chart.account_name
        db_chart.account_type = chart.account_type
        db_chart.report_type = chart.report_type

        db.commit()
        db.refresh(db_chart)
        return db_chart
    
# Delete Chart of Account
def delete_chart(db: Session, id: int):
    db_chart = db.query(models.Chart).get(id)
    
    if db_chart is None:
        raise HTTPException(status_code=404, detail="Chart of Account not found.")

    if db_chart is not None:
        db.delete(db_chart)
        db.commit()
        return db_chart
    
#### JOURNAL ENTRY RESOURCES

# Get All Journal Entries
def get_journals(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    journals_db = db.query(models.Journal)
    
    sortable_columns = {
        "id": models.Journal.id,
    }

    sort = (
        sortable_columns.get("id").asc()
        if sort_direction == "desc"
        else sortable_columns.get("id").desc()
    )

    filtered_result = journals_db.order_by(
        sort).offset(skip).limit(limit).all()
    return filtered_result   

def get_journals_by_filter(db: Session, from_date: str, to_date: str, account_id: int = 0, supplier_id: int = 0, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    journals_db = db.query(models.Journal)

    sortable_columns = {
        "id": models.Journal.id,
    }

    sort = (
        sortable_columns.get("id").asc()
        if sort_direction == "desc"
        else sortable_columns.get("id").desc()
    )

    if from_date == to_date:
        # Filter for a single day
        date = datetime.strptime(from_date, "%Y-%m-%d").date()
        next_day = date + timedelta(days=1)
        filtered_result = journals_db.filter(
            models.Journal.date >= date,
            models.Journal.date < next_day
        ).order_by(sort).offset(skip).limit(limit).all()
    else:
        # Filter for a date range
        from_date = datetime.strptime(from_date, "%Y-%m-%d")
        to_date = datetime.strptime(to_date, "%Y-%m-%d")

        filtered_result = journals_db.filter(
            models.Journal.date >= from_date,
            models.Journal.date <= to_date + timedelta(days=1)  # Adjusted the filter condition
        ).order_by(sort).offset(skip).limit(limit).all()

    # Filtered by account name
    if not account_id == 0:
        filtered_result = [result for result in filtered_result if result.debit_acct_id == account_id or result.credit_acct_id == account_id]
    
    if not supplier_id == 0:
        filtered_result = [result for result in filtered_result if result.supplier_id == supplier_id]

    return filtered_result

def insert_journal_from_csv(db: Session, csv_journal: schemas.CSVJournal):
    journal = (
        db.query(models.Journal)
        .filter(
            models.Journal.date == csv_journal.date,
        )
        .all()
    )
    if journal:
        journal_id = update_journal(db=db, id=journal[0].id, journal=csv_journal).id
    else:
        journal_id = create_journal(db=db, journal=csv_journal).id

    return journal_id

def import_journals(db: Session, csv_journal: list[schemas.CSVJournal]):
    for journal in csv_journal:
       insert_journal_from_csv(db=db, csv_journal=journal)

    raise HTTPException(status_code=status.HTTP_201_CREATED)

# Create Journal Entry
def create_journal(db: Session, journal : schemas.JournalCreate):
    db_journal = models.Journal(**journal .dict())
    db.add(db_journal)
    db.commit()
    db.refresh(db_journal )
    return db_journal 

# Update Journal Entry
def update_journal(db: Session, id: int, journal: schemas.JournalCreate):
    db_journal = db.query(models.Journal).get(id)

    if db_journal is None:
        raise HTTPException(status_code=404, detail="Journal Entry not found.")

    if db_journal is not None:
        db_journal.date = journal.date
        db_journal.supplier_id = journal.supplier_id
        db_journal.document_no = journal.document_no
        db_journal.debit_acct_id = journal.debit_acct_id
        db_journal.credit_acct_id = journal.credit_acct_id
        db_journal.debit = journal.debit
        db_journal.credit = journal.credit
        db_journal.notes = journal.notes
        db_journal.is_supplier = journal.is_supplier

        db.commit()
        db.refresh(db_journal)
        return db_journal
    
# Delete Journal Entry
def delete_journal(db: Session, id: int):
    db_journal = db.query(models.Journal).get(id)

    if db_journal is None:
        raise HTTPException(status_code=404, detail="Journal Entry not found.")

    if db_journal is not None:
        db.delete(db_journal)
        db.commit()
        return db_journal
    
#### SUPPLIER RESOURCES

# Get All Suppliers
def get_suppliers(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    supplier_db = db.query(models.Supplier)
    
    sortable_columns = {
        "id": models.Supplier.id,
    }

    sort = (
        sortable_columns.get("id").asc()
        if sort_direction == "desc"
        else sortable_columns.get("id").desc()
    )

    filtered_result = supplier_db.order_by(
        sort).offset(skip).limit(limit).all()
    return filtered_result

# Create Supplier
def create_supplier(db: Session, supplier : schemas.SupplierCreate):
    db_supplier = models.Supplier(**supplier .dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier 

# Update Supplier
def update_supplier(db: Session, id: int, supplier: schemas.SupplierCreate):
    db_supplier = db.query(models.Supplier).get(id)

    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found.")

    if db_supplier is not None:
        db_supplier.business_type = supplier.business_type
        db_supplier.first_name = supplier.first_name
        db_supplier.last_name = supplier.last_name
        db_supplier.email = supplier.email
        db_supplier.contact_number = supplier.contact_number
        db_supplier.tel_number = supplier.tel_number
        db_supplier.address = supplier.address
        db_supplier.tin = supplier.tin
        db_supplier.sec_registration = supplier.sec
        db_supplier.dti_registration = supplier.dti

        db.commit()
        db.refresh(db_supplier)
        return db_supplier
    
# Delete Supplier
def delete_supplier(db: Session, id: int):
    db_supplier = db.query(models.Supplier).get(id)

    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found.")

    if db_supplier is not None:
        db.delete(db_supplier)
        db.commit()
        return db_supplier
    
# Get Latest Balance Debit
def get_latest_debit_balance(db: Session):
    balance_debit_db = db.query(models.Debit).order_by(models.Debit.created_at.desc()).first()

    if balance_debit_db is None:
        raise HTTPException(status_code=404, detail="Not found.")

    return balance_debit_db
   
# Create Debit Balance
def create_debit(db: Session, debit: schemas.DebitCreate):
    db_debit = models.Debit(**debit.dict())
    db.add(db_debit)
    db.commit()
    db.refresh(db_debit)
    return db_debit
    
# Get Latest Balance Credit
def get_latest_credit_balance(db: Session):
    balance_credit_db = db.query(models.Credit).order_by(models.Credit.created_at.desc()).first()

    if balance_credit_db is None:
        raise HTTPException(status_code=404, detail="Not found.")
 
    return balance_credit_db

# Create Credit Balance
def create_credit(db: Session, credit: schemas.CreditCreate):
    db_credit = models.Credit(**credit.dict())
    db.add(db_credit)
    db.commit()
    db.refresh(db_credit)
    return db_credit