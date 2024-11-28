from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from items import items
from admin import admin
import uvicorn

app = FastAPI()


app.include_router(items)
app.include_router(admin)


origins = ['http://localhost:5173', 'https://localhost:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)