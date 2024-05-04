from typing import Optional
from pydantic import BaseModel
from app.database.validators.suppliers import Supplier

class ProductBase(BaseModel):
    name: str
    supplier_id: int
    price: float
    stock_quantity: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    supplier: Optional[Supplier] = None
    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    stock_quantity: Optional[int] = None
