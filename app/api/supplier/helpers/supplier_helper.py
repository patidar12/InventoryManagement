from app.database.models import Supplier as SupplierModel
from app.database.validators import SupplierCreate as SupplierCreateSchema
from app.database import get_db


class SupplierRepository:
    def __init__(self, db):
        self.db = db

    def create_supplier(self, supplier: SupplierCreateSchema) -> SupplierModel:
        new_supplier: SupplierModel = SupplierModel(**supplier.dict())
        self.db.add(new_supplier)
        self.db.commit()
        self.db.refresh(new_supplier)
        return new_supplier

    def get_supplier(self, supplier_id: int) -> SupplierModel:
        return self.db.query(SupplierModel).filter(SupplierModel.id == supplier_id).first()
