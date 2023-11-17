from datetime import timedelta, datetime
from sqlalchemy.orm import Session
from app.inventory import schemas, models
from fastapi import HTTPException
from sqlalchemy.orm import joinedload

def get_items(db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    items_db = db.query(models.Item)
    
    sortable_columns = {
        "id": models.Item.id,
    }

    sort = (
        sortable_columns.get("id").asc()
        if sort_direction == "desc"
        else sortable_columns.get("id").desc()
    )

    filtered_result = items_db.order_by(
        sort).offset(skip).limit(limit).all()
    return filtered_result

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, id: int, item: schemas.ItemCreate):
    db_item = db.query(models.Item).get(id)

    if db_item is None:
      raise HTTPException(status_code=404, detail="Inventory item not found.")

    if db_item is not None:
      db_item.description = item.description
      db_item.uom1 = item.uom1
      db_item.uom2 = item.uom2
      db_item.uom3 = item.uom3
      db_item.conversion = item.conversion
      db_item.default_coa = item.default_coa
      db_item.nominated_supplier = item.nominated_supplier
      db_item.last_vendor = item.last_vendor
      db_item.ave_cost = item.ave_cost
      db_item.highest_price = item.highest_price
      db_item.lowest_price = item.lowest_price
      db_item.is_vatable = item.is_vatable
      db_item.is_deleted = db_item.is_deleted
      db_item.added_by = db_item.added_by

      db.commit()
      db.refresh(db_item)
      return db_item

# def delete_item(db: Session, id: int, item: schemas.ItemCreate):
#     db_item = db.query(models.Item).get(id)

#     if db_item is None:
#       raise HTTPException(status_code=404, detail="Inventory item not found.")

#     if db_item is not None:
#       db_item.description = item.description
#       db_item.uom1 = item.uom1
#       db_item.uom2 = item.uom2
#       db_item.uom3 = item.uom3
#       db_item.conversion = item.conversion
#       db_item.default_coa = item.default_coa
#       db_item.nominated_supplier = item.nominated_supplier
#       db_item.last_vendor = item.last_vendor
#       db_item.ave_cost = item.ave_cost
#       db_item.highest_price = item.highest_price
#       db_item.lowest_price = item.lowest_price
#       db_item.is_vatable = item.is_vatable
#       db_item.is_deleted = db_item.is_deleted
#       db_item.added_by = db_item.added_by

#       db.commit()
#       db.refresh(db_item)
#       return db_item

def delete_item(id: int, db: Session):
    db_item = db.query(models.Item).get(id)
    if db_item is None:
      raise HTTPException(status_code=404, detail="Inventory item not found.")

    db_item.description = db_item.description
    db_item.uom1 = db_item.uom1
    db_item.uom2 = db_item.uom2
    db_item.uom3 = db_item.uom3
    db_item.conversion = db_item.conversion
    db_item.default_coa = db_item.default_coa
    db_item.nominated_supplier = db_item.nominated_supplier
    db_item.last_vendor = db_item.last_vendor
    db_item.ave_cost = db_item.ave_cost
    db_item.highest_price = db_item.highest_price
    db_item.lowest_price = db_item.lowest_price
    db_item.is_vatable = db_item.is_vatable
    db_item.is_deleted = 1
    db_item.added_by = db_item.added_by
    db.commit()

# def delete_item(id: int, db: Session):
#   db_item = db.query(models.Item).get(id)
#   if db_item is not None:
#       db_item.is_deleted = 1
#       db.commit()