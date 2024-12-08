import random
import shutil
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
import db


files = APIRouter(tags=["files"])


def create_signature():
    lst = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return "".join(random.choices(lst, k=20))


@files.post("/upload")
async def upload_file(upload_file: UploadFile = File(...)):
    upload_file.filename = f"{len(db.get_items('name')) + 1}.{upload_file.filename.split('.')[1]}"
    path = f"pizzas/{upload_file.filename}"
    with open(path, "wb+") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return f"/{path}"


@files.get("/pizzas/{file_name}", response_class=FileResponse)
async def download_file(file_name: str):
    path = f"pizzas/{file_name}"
    return path