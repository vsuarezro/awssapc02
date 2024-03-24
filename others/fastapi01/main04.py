from typing import Optional, Annotated

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

fake_secret_token = "mysupersecrettoken"

fake_db = {
    "name1": {
        "name": "name1",
        "description": "description of the name1",
        "price": 100.0,
        "tax": 10.0,
    },
    "name2": {
        "name": "name2",
        "description": "description of the name2",
        "price": 50.0,
        "tax": 5.0,
    },
}


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items", response_model=Item)
async def create_items(item: Item, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.name in fake_db:
        raise HTTPException(status_doce=400, detail="Item already exists in the DB")
    fake_db[item.name] = item
    return item


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_doce=400, detail="Item not found")
    return fake_db.get(item_id)


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
