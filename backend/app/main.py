from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db import engine, Base, SessionLocal
from .api.v1 import products, categories
from . import models

app = FastAPI(title="Inventario API", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        existing_categories = {c.nombre: c for c in db.query(models.Categoria).all()}
        if db.query(models.Producto).count() == 0:
            if not existing_categories:
                categories = [
                    models.Categoria(nombre="Bebidas"),
                    models.Categoria(nombre="Alimentos"),
                    models.Categoria(nombre="Limpieza"),
                    models.Categoria(nombre="Electrónica"),
                ]
                db.add_all(categories)
                db.commit()
                existing_categories = {c.nombre: c for c in db.query(models.Categoria).all()}

            products = [
                models.Producto(
                    nombre="Agua mineral",
                    categoria_id=existing_categories["Bebidas"].id,
                    cantidad=24,
                    precio=1.50,
                    descripcion="Botella 500ml",
                ),
                models.Producto(
                    nombre="Jugo de naranja",
                    categoria_id=existing_categories["Bebidas"].id,
                    cantidad=12,
                    precio=2.20,
                    descripcion="Caja 1L",
                ),
                models.Producto(
                    nombre="Pan integral",
                    categoria_id=existing_categories["Alimentos"].id,
                    cantidad=18,
                    precio=1.25,
                    descripcion="Paquete de 500g",
                ),
                models.Producto(
                    nombre="Aceite de oliva",
                    categoria_id=existing_categories["Alimentos"].id,
                    cantidad=8,
                    precio=6.80,
                    descripcion="Botella 750ml",
                ),
                models.Producto(
                    nombre="Detergente líquido",
                    categoria_id=existing_categories["Limpieza"].id,
                    cantidad=6,
                    precio=3.10,
                    descripcion="1L para ropa blanca",
                ),
                models.Producto(
                    nombre="Toallas húmedas",
                    categoria_id=existing_categories["Limpieza"].id,
                    cantidad=10,
                    precio=2.90,
                    descripcion="Paquete de 72 unidades",
                ),
                models.Producto(
                    nombre="Auriculares inalámbricos",
                    categoria_id=existing_categories["Electrónica"].id,
                    cantidad=3,
                    precio=29.99,
                    descripcion="Bluetooth con micrófono",
                ),
                models.Producto(
                    nombre="Cargador USB-C",
                    categoria_id=existing_categories["Electrónica"].id,
                    cantidad=7,
                    precio=14.50,
                    descripcion="Carga rápida 65W",
                ),
            ]
            db.add_all(products)
            db.commit()


app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
app.include_router(categories.router, prefix="/api/v1/categories", tags=["categories"])
