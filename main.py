from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class param1(BaseModel):
    id: int
    data: list

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/tests/{order_no}")
def get_order_data(order_no:str , param1: param1) -> param1:
    if type(order_no) == str:
        data = [1,2,3,4,5,6]
    else:
        data = []
    return {"data": data}