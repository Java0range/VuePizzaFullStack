from fastapi import APIRouter
from pydantic import BaseModel

import db


class Auth(BaseModel):
    username: str
    password: str


admin = APIRouter(tags=["admin"])


@admin.post("/auth/")
async def auth(inp: Auth):
    try:
        if db.auth(inp.username, inp.password):
            return {"msg": "true"}
        else:
            return {"msg": "false"}
    except Exception:
        return {"msg": "false"}