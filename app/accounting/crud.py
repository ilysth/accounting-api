from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.functions import func
from app.accounting import crud, schemas, models
from fastapi import HTTPException

from typing import List
from sqlalchemy.sql import func

# Get All Chart of Account
def get_charts(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    charts_db = db.query(models.Chart)
    
    sortable_columns = {
        "id": models.Chart.id,
    }

    sort = (
        sortable_columns.get("id").desc()
        if sort_direction == "desc"
        else sortable_columns.get("id").asc()
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

# Update Task
def update_chart(db: Session, id: int, chart: schemas.ChartCreate):
    db_chart = db.query(models.Chart).get(id)

    if db_chart is None:
        raise HTTPException(status_code=404, detail="Chart not found.")

    if db_chart is not None:
        db_chart.description = chart.description
        db_chart.account_type = chart.account_type
        db_chart.report_type = chart.report_type

        db.commit()
        db.refresh(db_chart)
        return db_chart
    
# Delete Chart of Account
def delete_chart(db: Session, id: int):
    chart_item = db.query(models.Chart).get(id)

    if chart_item is None:
        raise HTTPException(status_code=404, detail="Chart of Account not found.")

    if chart_item is not None:
        db.delete(chart_item)
        db.commit()
        return chart_item