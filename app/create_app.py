from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.product.urls import product_router
from app.api.supplier.urls import supplier_router


def attach_middleware(app: FastAPI):
    origins = ["http://localhost:3000"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

async def create_app():
    app = FastAPI()
    attach_middleware(app)
    app.include_router(product_router)
    app.include_router(supplier_router)
    @app.on_event("startup")
    async def init_database():
        from app.database import BaseModel, engine
        BaseModel.metadata.create_all(bind=engine)  # Create tables if not exist

    @app.api_route("/_healtz")
    async def health_check():
        return {"ok": "ok"}
    return app
