from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool
    quantity: int
    description: str
