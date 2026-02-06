from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    email: str
    password: str
    age: int
    roll_no: int

@app.get("/")
def read_root():
    return {"Hello": "World"}

