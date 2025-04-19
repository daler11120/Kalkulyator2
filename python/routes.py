from fastapi import APIRouter
from .models import Item
from .database import SessionLocal

router = APIRouter()

@router.get("/items/")
def read_items():
    db = SessionLocal()
    items = db.query(Item).all()
    return items
