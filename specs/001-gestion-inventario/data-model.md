# Data Model

Entities:

- Producto
  - id: Integer, PK
  - nombre: String (required)
  - categoria_id: Integer, FK -> Categoría
  - cantidad: Integer (>= 0)
  - precio: Decimal (>= 0.00)
  - descripcion: Text (optional)
  - creado_at: datetime
  - actualizado_at: datetime

- Categoría
  - id: Integer, PK
  - nombre: String (required, unique)

Validation rules:
- `cantidad` debe ser entero >= 0
- `precio` debe ser decimal con 2 decimales, >= 0
- `nombre` no vacío

SQLAlchemy model snippets (example):

```py
from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    categoria = relationship('Categoria')
    cantidad = Column(Integer, nullable=False, default=0)
    precio = Column(Numeric(10,2), nullable=False, default=0.00)
    descripcion = Column(Text)
    creado_at = Column(DateTime, default=datetime.utcnow)
    actualizado_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```
