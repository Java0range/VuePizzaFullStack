from fastapi import APIRouter
from pydantic import BaseModel
import db


class OrderItem(BaseModel):
    items: list
    total_price: int


items = APIRouter(tags=["items"])


@items.get("/items/{sort}")
async def get_items(sort: str):
    try:
        items = db.get_items(sort)
        return items
    except Exception:
        return {"msg": "error"}


@items.post("/orders")
async def create_order(inp: OrderItem):
    try:
        db.create_order(inp.items, inp.total_price)
        return {"msg": "success"}
    except Exception:
        return {"msg": "error"}