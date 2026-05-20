import csv
import io
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from models import Producto, Categoria
from schemas import Producto as ProductoSchema, ProductoCreate, ProductoUpdate, ProductoSummary

router = APIRouter(prefix="/api/v1/products", tags=["productos"])

@router.get("/summary", response_model=ProductoSummary)
def get_producto_summary(db: Session = Depends(get_db)):
    total_count = db.query(func.count(Producto.id)).scalar() or 0
    total_value = db.query(func.sum(Producto.precio * Producto.cantidad)).scalar() or 0
    low_stock_count = db.query(func.count(Producto.id)).filter(Producto.cantidad < 5).scalar() or 0

    return {
        "total_count": total_count,
        "total_value": total_value,
        "low_stock_count": low_stock_count
    }

@router.get("/export")
def export_productos(db: Session = Depends(get_db)):
    productos = db.query(Producto).all()

    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["id", "nombre", "descripcion", "precio", "cantidad", "categoria", "creado_at", "actualizado_at"])
    for p in productos:
        writer.writerow([
            p.id,
            p.nombre,
            p.descripcion or "",
            p.precio,
            p.cantidad,
            p.categoria.nombre if p.categoria else "",
            p.creado_at.isoformat() if p.creado_at else "",
            p.actualizado_at.isoformat() if p.actualizado_at else "",
        ])
    buffer.seek(0)

    filename = f"productos_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
    return StreamingResponse(
        iter([buffer.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )

@router.get("/", response_model=list[ProductoSchema])
def list_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    productos = db.query(Producto).offset(skip).limit(limit).all()
    return productos

@router.get("/{producto_id}", response_model=ProductoSchema)
def get_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/", response_model=ProductoSchema)
def create_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.id == producto.categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=400, detail="Categoría no encontrada")

    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.put("/{producto_id}", response_model=ProductoSchema)
def update_producto(producto_id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    update_data = producto.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_producto, field, value)

    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.delete("/{producto_id}")
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(db_producto)
    db.commit()
    return {"message": "Producto eliminado"}
