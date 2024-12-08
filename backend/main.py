from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from items import items
from admin import admin
from files import files
import uvicorn

app = FastAPI()


app.include_router(items)
app.include_router(admin)
app.include_router(files)


origins = ['http://192.168.0.15:5173', "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)