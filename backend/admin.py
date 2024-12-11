from fastapi import APIRouter
from pydantic import BaseModel
from Auth import Auth


import db


class AuthModel(BaseModel):
    username: str
    password: str


class DeleteItem(BaseModel):
    name: str
    token: str


class AddItem(BaseModel):
    name: str
    img: str
    desc: list
    price: str
    token: str


admin = APIRouter(tags=["admin"])
security = Auth(open("secret_key.txt", "r", encoding="utf-8").read().strip())


@admin.post("/auth/")
async def auth(inp: AuthModel):
    try:
        if db.auth(inp.username, inp.password):
            token = security.create_token()
            return token
        else:
            return "false"
    except Exception:
        return "false"


@admin.delete("/delete/")
async def delete(inp: DeleteItem):
    try:
        if security.verify_token(inp.token):
            db.delete_item(inp.name)
            return "true"
        return "false"
    except Exception:
        return "false"


@admin.post("/add/")
async def add_item(inp: AddItem):
    if security.verify_token(inp.token):
        desc = [i["name"] for i in inp.desc]
        price = int(inp.price)
        try:
            db.create_item(inp.name, inp.img, desc, price)
            return "true"
        except Exception:
            return "false"
    return "false"