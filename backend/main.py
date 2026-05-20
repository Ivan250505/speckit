from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import products, categories

# Crear las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventario API",
    description="API para gestionar inventario de productos",
    version="0.1.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(products.router)
app.include_router(categories.router)

@app.get("/")
def root():
    return {"message": "Inventario API", "version": "0.1.0"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
