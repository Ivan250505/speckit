from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int
    
    class Config:
        from_attributes = True

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    cantidad: int
    categoria_id: int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    cantidad: Optional[int] = None
    categoria_id: Optional[int] = None

class Producto(ProductoBase):
    id: int
    creado_at: datetime
    actualizado_at: datetime
    categoria: Categoria
    
    class Config:
        from_attributes = True

class ProductoSummary(BaseModel):
    total_count: int
    total_value: float
    low_stock_count: int
