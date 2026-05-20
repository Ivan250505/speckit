from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List
from fastapi.responses import StreamingResponse
import csv
import io

from ...db import get_db
from ... import models, schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.ProductoOut])
def list_products(search: str = None, category: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Producto)
    if search:
        query = query.filter(models.Producto.nombre.contains(search))
    if category:
        query = query.join(models.Categoria).filter(models.Categoria.nombre == category)
    return query.all()


@router.get("/summary")
def product_summary(db: Session = Depends(get_db)):
    total_count = db.query(func.count(models.Producto.id)).scalar() or 0
    total_value = db.query(func.coalesce(func.sum(models.Producto.cantidad * models.Producto.precio), 0)).scalar() or 0
    low_stock_count = db.query(func.count(models.Producto.id)).filter(models.Producto.cantidad < 5).scalar() or 0
    return {
        "total_count": total_count,
        "total_value": float(total_value),
        "low_stock_count": low_stock_count,
    }


@router.post("/", response_model=schemas.ProductoOut, status_code=201)
def create_product(payload: schemas.ProductoCreate, db: Session = Depends(get_db)):
    prod = models.Producto(**payload.dict(exclude_none=True))
    db.add(prod)
    db.commit()
    db.refresh(prod)
    return prod


@router.get("/{product_id}", response_model=schemas.ProductoOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    prod = db.query(models.Producto).filter(models.Producto.id == product_id).first()
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    return prod


@router.put("/{product_id}", response_model=schemas.ProductoOut)
def update_product(product_id: int, payload: schemas.ProductoUpdate, db: Session = Depends(get_db)):
    prod = db.query(models.Producto).filter(models.Producto.id == product_id).first()
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    for k, v in payload.dict(exclude_none=True).items():
        setattr(prod, k, v)
    db.add(prod)
    db.commit()
    db.refresh(prod)
    return prod


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    prod = db.query(models.Producto).filter(models.Producto.id == product_id).first()
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(prod)
    db.commit()
    return


@router.get("/export")
def export_products(search: str = None, category: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Producto)
    if search:
        query = query.filter(models.Producto.nombre.contains(search))
    if category:
        query = query.join(models.Categoria).filter(models.Categoria.nombre == category)

    products = query.all()

    def iter_csv():
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["id", "nombre", "categoria", "cantidad", "precio", "descripcion", "valor_total"])
        yield output.getvalue()
        output.seek(0)
        output.truncate(0)
        for p in products:
            categoria = p.categoria.nombre if p.categoria else ""
            valor = float(p.cantidad) * float(p.precio)
            writer.writerow([p.id, p.nombre, categoria, p.cantidad, float(p.precio), p.descripcion or "", f"{valor:.2f}"])
            yield output.getvalue()
            output.seek(0)
            output.truncate(0)

    headers = {"Content-Disposition": "attachment; filename=inventory.csv"}
    return StreamingResponse(iter_csv(), media_type="text/csv; charset=utf-8", headers=headers)
