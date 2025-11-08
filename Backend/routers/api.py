from fastapi import APIRouter
from typing import Union

router= APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}