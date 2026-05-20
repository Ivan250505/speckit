from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class CategoriaOut(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True


class ProductoBase(BaseModel):
    nombre: str = Field(...)
    categoria_id: Optional[int]
    cantidad: int = Field(0, ge=0)
    precio: float = Field(0.0, ge=0.0)
    descripcion: Optional[str] = None


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(BaseModel):
    nombre: Optional[str]
    categoria_id: Optional[int]
    cantidad: Optional[int]
    precio: Optional[float]
    descripcion: Optional[str]


class ProductoOut(ProductoBase):
    id: int
    categoria: Optional[CategoriaOut]
    creado_at: Optional[datetime]
    actualizado_at: Optional[datetime]

    class Config:
        orm_mode = True
