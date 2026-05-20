# Research: Elecciones técnicas para Gestión de Inventario

Decision: FastAPI + SQLAlchemy + SQLite para backend; React (Vite) + Tailwind CSS para frontend.

Rationale:
- FastAPI: permite construir APIs REST rápidas con validación automática (Pydantic) y buena documentación OpenAPI integrada.
- SQLAlchemy: ORM maduro y compatible con SQLite; facilita modelos y migraciones si se usa Alembic.
- SQLite: sencillo, zero-config y suficiente para MVP local; evita infra adicional.
- React + Vite: arranque rápido, soporte moderno y ecosistema amplio.
- Tailwind CSS: rápida composición de UI moderna y responsiva sin escribir CSS extenso.

Alternatives considered:
- Django REST Framework: ofrecía más "batteries included" pero mayor sobrecarga para un API sencillo.
- Prisma (Node) o TypeORM: alternativas para JS/TS backend si se hubiera elegido Node en servidor.
- Postgres en vez de SQLite: más robusto para producción, pero añade complejidad de despliegue; considerar para v2.

Decision consequences / notes:
- No Docker en v1: facilita inicio local, pero complica reproducibilidad en entornos heterogéneos.
- Elegir Alembic para migraciones es opcional; para MVP puede iniciarse con esquema sincronizado por SQLAlchemy.
