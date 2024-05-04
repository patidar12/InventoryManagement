from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response

from app.database.validators import (
    ProductCreate as ProductCreateSchema,
    ProductUpdate as ProductUpdateSchema,
    Product as ProductSchema
)
from app.api.product.helpers import ProductRepository
from app.database import get_db

router = APIRouter(prefix="/products")

@router.post("/", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreateSchema, db = Depends(get_db)):
    product_repository = ProductRepository(db)
    product, message = product_repository.create_product(product)
    if not product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)
    return product


@router.get("/{product_id}", response_model=ProductSchema)
def get_product(product_id: int, db = Depends(get_db)):
    product_repository = ProductRepository(db)
    product = product_repository.get_product(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@router.get("/", response_model=List[ProductSchema])
def list_products(supplier_id: int = None, min_price: float = None, max_price: float = None, db = Depends(get_db)):
    product_repository = ProductRepository(db)
    return product_repository.list_products(supplier_id, min_price, max_price)


@router.put("/{product_id}", response_model=ProductSchema)
def update_product(product_id: int, product_update: ProductUpdateSchema, db = Depends(get_db)):
    product_repository = ProductRepository(db)
    product = product_repository.update_product(product_id, product_update)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db = Depends(get_db)):
    product_repository = ProductRepository(db)
    product = product_repository.delete_product(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")