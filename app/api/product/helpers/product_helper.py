from app.database.models import (
    Product as ProductModel,
)
from app.database.validators import (
    ProductCreate as ProductCreateSchema,
    ProductUpdate as ProductUpdateSchema
)

from app.api.supplier.helpers import SupplierRepository

from app.database import get_db

class ProductRepository:
    def __init__(self, db):
        self.db = db

    def create_product(self, product: ProductCreateSchema) -> ProductModel:
        # verify supplier
        print("product data: ", product)
        supplier_id = product.supplier_id
        supplier = SupplierRepository(self.db).get_supplier(supplier_id=supplier_id)
        if not supplier:
            return None, f"Suplier with id: {supplier_id} not present."
        new_product: ProductModel = ProductModel(**product.dict())
        # self.db.add(new_product)
        # self.db.commit()
        # self.db.refresh(new_product)
        new_product.insert_one(self.db)
        return new_product, ""

    def get_product(self, product_id: int) -> ProductModel:
        return self.db.query(ProductModel).filter(ProductModel.id == product_id).first()

    def list_products(self, supplier_id: int = None, min_price: float = None, max_price: float = None):
        query = self.db.query(ProductModel)
        filters = []
        if supplier_id:
            filters.append(ProductModel.supplier_id == supplier_id)
        if min_price is not None:
            filters.append(ProductModel.price >= min_price)
        if max_price is not None:
            filters.append(ProductModel.price <= max_price)
        if filters:
            query = query.filter(*filters) 
        return query.all()

    def update_product(self, product_id: int, product_update: ProductUpdateSchema) -> ProductModel:
        product: ProductModel = self.get_product(product_id)
        if not product:
            return None, "Product not found"

        # Update product attributes based on provided data
        for field, value in product_update.dict().items():
            if value is not None:
                setattr(product, field, value)

        self.db.commit()
        self.db.refresh(product)
        return product

    def delete_product(self, product_id: int) -> None:
        product: ProductModel = self.get_product(product_id)
        if not product:
            return None
        self.db.delete(product)
        self.db.commit()
        return product
