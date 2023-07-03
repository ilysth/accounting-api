from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.functions import func
from app.accounting import crud, schemas, models
from fastapi import HTTPException
from typing import List
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

def get_journals_by_date(db: Session, from_date: str, to_date: str, account_name: str = "All", sort_direction: str = "desc", skip: int = 0, limit: int = 100):
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

    if account_name == "All":
        return filtered_result
    else:
        # Filtered by account name
        # im trying to do a one liner here "the commented code below" but it dont give me the filtered result i want
        # filtered_result = [result for result in filtered_result if result.debit_account_name or result.credit_account_name == account_name]
        filtered_result_c = [filtered_result for filtered_result in filtered_result if filtered_result.credit_account_name == account_name]
        filtered_result_d = [filtered_result for filtered_result in filtered_result if filtered_result.debit_account_name == account_name]
        
        filtered_result = filtered_result_c + filtered_result_d

        return filtered_result

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
        db_journal.supplier_name = journal.supplier_name
        db_journal.document_no = journal.document_no
        db_journal.debit_account_name = journal.debit_account_name
        db_journal.credit_account_name = journal.credit_account_name
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
        db_supplier.sec_registration = supplier.sec_registration
        db_supplier.dti_registration = supplier.dti_registration

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