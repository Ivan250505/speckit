# Implementation Plan: Gestión de Inventario

**Branch**: `001-ecommerce-api` | **Date**: 2026-05-17 | **Spec**: [specs/001-gestion-inventario/spec.md](specs/001-gestion-inventario/spec.md#L1)

**Input**: Feature specification from `specs/001-gestion-inventario/spec.md`

## Summary

Implementar una aplicación web local (backend + frontend) para gestión de inventario.
Backend: FastAPI + SQLAlchemy sobre SQLite, expositor de endpoints REST para CRUD, búsqueda/filtrado y exportación CSV.
Frontend: React (Vite) con Tailwind CSS, tabla principal con búsqueda/filtros, alertas visuales para stock < 5, panel resumen y exportación CSV.

## Technical Context

**Language/Version**: Python 3.11 (backend), Node 18+ (frontend)

**Primary Dependencies**: FastAPI, SQLAlchemy (1.4+/ORM), Alembic (migrations optional), Uvicorn; React 18, Vite, Tailwind CSS v3, Axios (or Fetch).

**Storage**: SQLite (local file) via SQLAlchemy

**Testing**: `pytest` for backend unit/integration tests; `playwright` or `vitest` for frontend tests; basic end-to-end checks via scripted requests.

**Target Platform**: Local development and lightweight deployment (single-process server). No Docker in v1.

**Project Type**: Web application (separated `backend/` and `frontend/`).

**Performance Goals**: Responsive UI interactions (<200ms UI ops) for datasets up to a few thousand products; API p95 <200ms for typical queries on local SQLite.

**Constraints**: Use SQLite for v1 (single-file DB); avoid heavyweight infra and skip Docker for now; ensure UTF-8 CSV export.

**Scale/Scope**: MVP for single-team use; expected concurrent users: small (<=50), dataset: <=100k rows (SQLite limits acceptable for MVP).

## Constitution Check

Constitution file contains placeholders; no gating rules enforced. No violations detected.

## Project Structure

Documentation and artifacts for this feature:

```
specs/001-gestion-inventario/
├── spec.md
├── plan.md            # (this file)
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── api.md
├── checklists/
└── tasks.md           # generated later
```

Source layout (selected):

```
backend/
├── app/
│   ├── main.py           # FastAPI app
│   ├── api/
│   │   └── v1/
│   ├── models.py         # SQLAlchemy models
│   ├── db.py             # session, engine, utils
│   └── services/         # business logic
└── tests/

frontend/
├── package.json
├── src/
│   ├── main.jsx
+│   ├── App.jsx
│   ├── components/
│   │   ├── ProductsTable.jsx
│   │   └── ProductForm.jsx
│   └── services/api.js
└── vite.config.js
```

**Structure Decision**: Use a two-project layout (`backend/` + `frontend/`) for clear separation of concerns and easy local development. Backend will serve a JSON API; frontend is a separate static client.

## Phase 0: Research (completed)

- See `research.md` for decisions and alternatives (FastAPI, SQLAlchemy, React/Vite, Tailwind).

## Frontend Redesign: Scope & Deliverables

Decision constraint: Mantener el backend FastAPI + SQLite existente sin cambios; todo el trabajo queda en el frontend.

Deliverables:

- Página de inicio (dashboard) con métricas clave y accesos rápidos a acciones comunes (crear producto, exportar CSV).
- Navegación principal con íconos y etiquetas en español (sidebar o topbar según resolución).
- Biblioteca de componentes reutilizables en `frontend/src/components/`: tarjetas (`Card`), tabla (`Table`), modal de formulario (`ModalForm`), barra de búsqueda (`SearchBar`), sistema de notificaciones (`Toast`).
- Sistema de notificaciones para feedback de usuario (éxito, error, información) con accesibilidad básica.
- Paleta de colores consistente y profesional (definida en `frontend/src/styles/colors.js` o Tailwind config) y tokens de espaciado/typography.
- Diseño responsivo orientado a escritorio y tablet (mobile-first degradable) y pruebas de puntos de ruptura principales.
- Documentación de diseño y ejemplos de uso para cada componente (Storybook opcional en v2).

Acceptance criteria for redesign:

- El dashboard muestra: total de productos, valor total del inventario y contador de productos con stock < 5.
- La navegación está en español y tiene iconografía legible; los elementos principales deben ser: Inicio, Productos, Categorías, Exportar.
- El modal de formulario permite crear/editar productos con validaciones y feedback de error.
- Las notificaciones aparecen en la esquina superior derecha y desaparecen tras 4s o por acción del usuario.
- La paleta de colores y estilos están centralizados y aplicados a todos los componentes.

## Phase 1.5: Frontend Redesign (new)

**Purpose**: Implementar el rediseño solicitado, manteniendo el backend sin cambios.

Key tasks (high-level):

1. Diseñar paleta de colores y tokens (variables Tailwind / CSS custom properties).
2. Crear componentes reutilizables: `Card`, `Table`, `ModalForm`, `SearchBar`, `Toast`.
3. Implementar página `Dashboard` (métricas + accesos rápidos) y `ProductsPage` usando nuevos componentes.
4. Añadir navegación traducida y accesible con iconos SVG.
5. Integrar notificaciones y estados de UI (loading, empty, error).
6. Probar diseño en desktop/tablet y ajustar breakpoints.

## Next Steps (updated)

1. Ejecutar las tareas de rediseño frontend listadas en `tasks.md` (sección Frontend Redesign).
2. Implementar y probar UI frente al backend existente (endpoints actuales no cambian).
3. Revisar y validar accesibilidad y usabilidad con un par de pruebas manuales en escritorio/tablet.
4. Opcional: añadir Storybook y pruebas visuales en una iteración posterior.
## Phase 1: Design & Contracts (deliverables)

- `data-model.md` — entities, fields, validation rules, SQLAlchemy snippets.
- `contracts/api.md` — REST endpoint definitions, request/response schemas, example cURL.
- `quickstart.md` — minimal local dev run instructions (no Docker).

## Next Steps

1. Review `research.md`, `data-model.md` and `contracts/api.md`.
2. If approved, generate `tasks.md` (implementation tasks) and start backend scaffolding.

