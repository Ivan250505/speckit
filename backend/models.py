from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, index=True)
    
    productos = relationship("Producto", back_populates="categoria")

class Producto(Base):
    __tablename__ = "productos"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), index=True)
    descripcion = Column(String(500))
    precio = Column(Float)
    cantidad = Column(Integer)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    creado_at = Column(DateTime, default=datetime.utcnow)
    actualizado_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    categoria = relationship("Categoria", back_populates="productos")
