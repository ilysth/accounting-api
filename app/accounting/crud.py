from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.functions import func
from app.accounting import crud, schemas, models
from fastapi import HTTPException
from typing import List

from typing import List
from sqlalchemy.sql import func

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
        db_journal.debit_account_type = journal.debit_account_type
        db_journal.credit_account_type = journal.credit_account_type
        db_journal.debit = journal.debit
        db_journal.credit = journal.credit
        db_journal.notes = journal.notes

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
    