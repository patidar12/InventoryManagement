from fastapi import APIRouter

from app.api.supplier.view import router

supplier_router = APIRouter()
supplier_router.include_router(router)
