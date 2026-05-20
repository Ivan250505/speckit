from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base


class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)


class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False, index=True)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    categoria = relationship('Categoria')
    cantidad = Column(Integer, nullable=False, default=0)
    precio = Column(Numeric(10, 2), nullable=False, default=0.00)
    descripcion = Column(Text)
    creado_at = Column(DateTime, default=datetime.utcnow)
    actualizado_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
