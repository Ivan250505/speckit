from pathlib import Path
from decimal import Decimal

from database import engine, SessionLocal, Base
import models

CATEGORIES = [
    "Electrónica",
    "Ropa",
    "Alimentos",
    "Hogar",
]

PRODUCTS = [
    {
        "nombre": "Televisor LED 55\"",
        "categoria": "Electrónica",
        "cantidad": 14,
        "precio": Decimal("259999.00"),
        "descripcion": "Televisor 55 pulgadas con resolución 4K y Smart TV.",
    },
    {
        "nombre": "Celular Android",
        "categoria": "Electrónica",
        "cantidad": 4,
        "precio": Decimal("149999.00"),
        "descripcion": "Smartphone con cámara triple y batería de larga duración.",
    },
    {
        "nombre": "Teclado mecánico",
        "categoria": "Electrónica",
        "cantidad": 22,
        "precio": Decimal("54999.00"),
        "descripcion": "Teclado retroiluminado para oficina y gaming.",
    },
    {
        "nombre": "Camiseta básica",
        "categoria": "Ropa",
        "cantidad": 18,
        "precio": Decimal("12999.00"),
        "descripcion": "Camiseta algodón unisex, disponible en varios colores.",
    },
    {
        "nombre": "Jeans azul",
        "categoria": "Ropa",
        "cantidad": 3,
        "precio": Decimal("34999.00"),
        "descripcion": "Pantalón denim para uso diario con corte cómodo.",
    },
    {
        "nombre": "Chaqueta de invierno",
        "categoria": "Ropa",
        "cantidad": 6,
        "precio": Decimal("89999.00"),
        "descripcion": "Chaqueta térmica con capucha para clima frío.",
    },
    {
        "nombre": "Aceite de oliva extra virgen",
        "categoria": "Alimentos",
        "cantidad": 12,
        "precio": Decimal("17999.00"),
        "descripcion": "Botella de 750 ml, ideal para cocina saludable.",
    },
    {
        "nombre": "Café molido premium",
        "categoria": "Alimentos",
        "cantidad": 2,
        "precio": Decimal("21999.00"),
        "descripcion": "Café 100% arábica con aroma intenso.",
    },
    {
        "nombre": "Limpiador multiuso",
        "categoria": "Hogar",
        "cantidad": 10,
        "precio": Decimal("7999.00"),
        "descripcion": "Limpia superficies sin dejar residuos.",
    },
    {
        "nombre": "Juego de sábanas",
        "categoria": "Hogar",
        "cantidad": 1,
        "precio": Decimal("45999.00"),
        "descripcion": "Sábanas 100% algodón para cama matrimonial.",
    },
]


def seed_database():
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        categories = {}
        for name in CATEGORIES:
            category = db.query(models.Categoria).filter(models.Categoria.nombre == name).first()
            if not category:
                category = models.Categoria(nombre=name)
                db.add(category)
        db.commit()

        categories = {c.nombre: c for c in db.query(models.Categoria).all()}

        existing_products = {p.nombre for p in db.query(models.Producto).all()}
        for item in PRODUCTS:
            if item["nombre"] in existing_products:
                continue
            product = models.Producto(
                nombre=item["nombre"],
                categoria_id=categories[item["categoria"]].id,
                cantidad=item["cantidad"],
                precio=float(item["precio"]),
                descripcion=item["descripcion"],
            )
            db.add(product)
        db.commit()

        print("✓ Base de datos poblada con 4 categorías y 10 productos.")
        count_cats = db.query(models.Categoria).count()
        count_prods = db.query(models.Producto).count()
        print(f"  Categorías: {count_cats}")
        print(f"  Productos: {count_prods}")


if __name__ == '__main__':
    seed_database()
