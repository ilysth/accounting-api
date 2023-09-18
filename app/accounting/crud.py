from sqlalchemy.orm import Session
from app.accounting import schemas, models
from fastapi import HTTPException, status
from datetime import datetime, timedelta

def get_frames(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    charts_db = db.query(models.Frame)
    
    sortable_columns = {
        "id": models.Frame.id,
    }

    sort = (
        sortable_columns.get("id").asc()
        if sort_direction == "desc"
        else sortable_columns.get("id").desc()
    )

    filtered_result = charts_db.order_by(
        sort).offset(skip).limit(limit).all()
    return filtered_result

def create_frame(db: Session, frame: schemas.FrameCreate):
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
        db_frame.account_code = frame.account_code

        db.commit()
        db.refresh(db_frame)
        return db_frame
 
def delete_frame(db: Session, id: int):
    db_frame = db.query(models.Frame).get(id)
    chart = db.query(models.Chart).filter(models.Chart.frame_id == id).first()

    if chart is not None:
        raise HTTPException(status_code=404, detail="Cannot be deleted. Account Frames have sub-accounts in use.")

    if db_frame is None:
        raise HTTPException(status_code=404, detail="Account Frame not found.")

    if db_frame is not None:
        db.delete(db_frame)
        db.commit()
        return db_frame
    
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

def create_chart(db: Session, chart: schemas.ChartCreate):
    frame = db.query(models.Frame).filter(models.Frame.id == chart.frame_id).first()

    if not frame:
        raise HTTPException(status_code=404, detail="Account Frame does not exist.")

    db_chart = models.Chart(**chart.dict())
    db.add(db_chart)
    db.commit()
    db.refresh(db_chart)
    return db_chart

def update_chart(db: Session, id: int, chart: schemas.ChartCreate):
    db_chart = db.query(models.Chart).get(id)

    if db_chart is None:
        raise HTTPException(status_code=404, detail="Account Name not found.")

    if db_chart is not None:
        db_chart.name = chart.name
        db_chart.account_type = chart.account_type
        db_chart.account_code = chart.account_code

        db.commit()
        db.refresh(db_chart)
        return db_chart
 
def delete_chart(db: Session, id: int):
    # todo: check account if in use in in credit and debit table, if exist dont let to delete account
    db_chart = db.query(models.Chart).get(id)

    if db_chart is None:
        raise HTTPException(status_code=404, detail="Account Name not found.")

    if db_chart is not None:
        db.delete(db_chart)
        db.commit()
        return db_chart

def get_companies(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    charts_db = db.query(models.Company)
    
    sortable_columns = {
        "id": models.Company.id,
    }

    sort = (
        sortable_columns.get("id").asc()
        if sort_direction == "desc"
        else sortable_columns.get("id").desc()
    )

    filtered_result = charts_db.order_by(
        sort).offset(skip).limit(limit).all()
    return filtered_result

def create_company(db: Session, company: schemas.CompanyCreate):
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
        db_company.company_code = company.company_code

        db.commit()
        db.refresh(db_company)
        return db_company
 
def delete_company(db: Session, id: int):
    db_company = db.query(models.Company).get(id)
    department = db.query(models.Department).filter(models.Department.company_id == id).first()

    if department is not None:
        raise HTTPException(status_code=404, detail="Cannot be deleted. Company have departments in use.")

    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found.")

    if db_company is not None:
        db.delete(db_company)
        db.commit()
        return db_company

def get_departments(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    charts_db = db.query(models.Department)
    
    sortable_columns = {
        "id": models.Department.id,
    }

    sort = (
        sortable_columns.get("id").asc()
        if sort_direction == "desc"
        else sortable_columns.get("id").desc()
    )

    filtered_result = charts_db.order_by(
        sort).offset(skip).limit(limit).all()
    return filtered_result
   
def create_department(db: Session, department: schemas.DepartmentCreate):
    company = db.query(models.Company).filter(models.Company.id == department.company_id).first()

    if not company:
        raise HTTPException(status_code=404, detail="Company dont exist.")
    
    db_dept = models.Department(**department.dict())
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

def update_department(db: Session, id: int, department: schemas.DepartmentCreate):
    db_dept = db.query(models.Department).get(id)

    if db_dept is None:
        raise HTTPException(status_code=404, detail="Department not found.")

    if db_dept is not None:
        db_dept.name = department.name
        db_dept.dept_code = department.dept_code

        db.commit()
        db.refresh(db_dept)
        return db_dept
 
def delete_department(db: Session, id: int):
    db_dept = db.query(models.Department).get(id)

    if db_dept is None:
        raise HTTPException(status_code=404, detail="Department not found.")

    if db_dept is not None:
        db.delete(db_dept)
        db.commit()
        return db_dept
         
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

def import_journal_from_csv(db: Session, csv_journal: schemas.JournalCreate):
    new_journal = models.Journal(
        date=csv_journal.date,
        supplier_id=csv_journal.supplier_id,
        debit_acct_id=csv_journal.debit_acct_id,
        credit_acct_id=csv_journal.credit_acct_id,
        debit_particulars=csv_journal.debit_particulars,
        credit_particulars=csv_journal.credit_particulars,
        debit=csv_journal.debit,
        credit=csv_journal.credit,
        is_supplier=csv_journal.is_supplier,
    )

    db.add(new_journal)
    db.commit()
    db.refresh(new_journal)

    return new_journal

def create_journal(db: Session, journal : schemas.JournalCreate):
    db_journal = models.Journal(**journal .dict())
    db.add(db_journal)
    db.commit()
    db.refresh(db_journal )
    return db_journal 

def update_journal(db: Session, id: int, journal: schemas.JournalCreate):
    db_journal = db.query(models.Journal).get(id)

    if db_journal is None:
        raise HTTPException(status_code=404, detail="Journal Entry not found.")

    if db_journal is not None:
        db_journal.date = journal.date
        db_journal.supplier_id = journal.supplier_id
        db_journal.reference_no = journal.reference_no
        db_journal.debit_acct_id = journal.debit_acct_id
        db_journal.credit_acct_id = journal.credit_acct_id
        db_journal.debit_particulars = journal.debit_particulars
        db_journal.credit_particulars = journal.credit_particulars
        db_journal.debit = journal.debit
        db_journal.credit = journal.credit
        db_journal.notes = journal.notes
        db_journal.is_supplier = journal.is_supplier

        db.commit()
        db.refresh(db_journal)
        return db_journal
    
def delete_journal(db: Session, id: int):
    db_journal = db.query(models.Journal).get(id)

    if db_journal is None:
        raise HTTPException(status_code=404, detail="Journal Entry not found.")

    if db_journal is not None:
        db.delete(db_journal)
        db.commit()
        return db_journal

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

def create_supplier(db: Session, supplier : schemas.SupplierCreate):
    db_supplier = models.Supplier(**supplier .dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier 

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

def delete_supplier(db: Session, id: int):
    db_supplier = db.query(models.Supplier).get(id)

    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found.")

    if db_supplier is not None:
        db.delete(db_supplier)
        db.commit()
        return db_supplier
    
def get_latest_debit_balance(db: Session):
    balance_debit_db = db.query(models.Debit).order_by(models.Debit.created_at.desc()).first()

    if balance_debit_db is None:
        raise HTTPException(status_code=404, detail="Not found.")

    return balance_debit_db
   
def create_debit(db: Session, debit: schemas.DebitCreate):
    db_debit = models.Debit(**debit.dict())
    db.add(db_debit)
    db.commit()
    db.refresh(db_debit)
    return db_debit
    
def get_latest_credit_balance(db: Session):
    balance_credit_db = db.query(models.Credit).order_by(models.Credit.created_at.desc()).first()

    if balance_credit_db is None:
        raise HTTPException(status_code=404, detail="Not found.")
 
    return balance_credit_db

def create_credit(db: Session, credit: schemas.CreditCreate):
    db_credit = models.Credit(**credit.dict())
    db.add(db_credit)
    db.commit()
    db.refresh(db_credit)
    return db_credit