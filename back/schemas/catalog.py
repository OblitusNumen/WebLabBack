import uuid
from typing import Any

from pydantic import BaseModel

from database.models.good import Good


class Card(BaseModel):
    id: uuid.UUID
    img: str
    price: float
    discount: float
    stock: int
    name: str

    def __init__(self, good: Good, /, **data: Any):
        super().__init__(**data)
        self.id = good.id
        self.img = good.img
        self.price = good.price
        self.discount = good.discount
        self.stock = good.stock
        self.name = good.name


class CartItem(BaseModel):
    id: uuid.UUID
    count: int


class Cart(BaseModel):
    contents: list[CartItem]
