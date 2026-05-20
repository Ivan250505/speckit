from sqlalchemy.orm import Session
from .. import models


def list_products(db: Session, search: str = None, category: str = None):
    query = db.query(models.Producto)
    if search:
        query = query.filter(models.Producto.nombre.contains(search))
    if category:
        query = query.join(models.Categoria).filter(models.Categoria.nombre == category)
    return query.all()


def get_product(db: Session, product_id: int):
    return db.query(models.Producto).filter(models.Producto.id == product_id).first()


def create_product(db: Session, payload: dict):
    prod = models.Producto(**payload)
    db.add(prod)
    db.commit()
    db.refresh(prod)
    return prod


def update_product(db: Session, product, updates: dict):
    for k, v in updates.items():
        setattr(product, k, v)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product):
    db.delete(product)
    db.commit()
