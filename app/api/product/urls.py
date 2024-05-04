from fastapi import APIRouter

from app.api.product.view import router

product_router = APIRouter()
product_router.include_router(router)
