from fastapi import APIRouter
from pydantic import BaseModel

import db


class Auth(BaseModel):
    username: str
    password: str


class DeleteItem(BaseModel):
    name: str


class AddItem(BaseModel):
    name: str
    img: str
    desc: list
    price: str


admin = APIRouter(tags=["admin"])


@admin.post("/auth/")
async def auth(inp: Auth):
    try:
        if db.auth(inp.username, inp.password):
            return "true"
        else:
            return "false"
    except Exception:
        return "false"


@admin.delete("/delete/")
async def delete(inp: DeleteItem):
    try:
        db.delete_item(inp.name)
        return "true"
    except Exception:
        return "false"


@admin.post("/add/")
async def add_item(inp: AddItem):
    desc = [i["name"] for i in inp.desc]
    price = int(inp.price)
    try:
        db.create_item(inp.name, inp.img, desc, price)
        return "true"
    except Exception:
        return "false"