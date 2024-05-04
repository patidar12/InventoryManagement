from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.database.validators import Supplier as SupplierSchema, SupplierCreate as SupplierCreateSchema
from app.api.supplier.helpers import SupplierRepository
from app.database import get_db

router = APIRouter(prefix="/suppliers")

@router.post("/", response_model=SupplierSchema, status_code=status.HTTP_201_CREATED)
def create_supplier(supplier: SupplierCreateSchema, db = Depends(get_db)):
    supplier_repository = SupplierRepository(db)
    return supplier_repository.create_supplier(supplier)


@router.get("/{supplier_id}", response_model=SupplierSchema)
def get_supplier(supplier_id: int, db = Depends(get_db)):
    supplier_repository = SupplierRepository(db)
    supplier = supplier_repository.get_supplier(supplier_id)
    if not supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    return supplier

