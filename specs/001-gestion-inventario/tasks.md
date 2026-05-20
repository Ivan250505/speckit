# Tasks: Gestión de Inventario

**Input**: Design docs from `specs/001-gestion-inventario/` (spec.md, data-model.md, contracts/api.md)

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project folders `backend/` and `frontend/` per plan (specs/001-gestion-inventario/plan.md)
- [ ] T002 Initialize Python virtualenv and base files in `backend/` (`backend/.venv`, `backend/requirements.txt`, `backend/README.md`)
- [ ] T003 Initialize Node project in `frontend/` (`frontend/package.json`, `frontend/README.md`) and add Vite + React dev deps
- [ ] T004 [P] Add `.gitignore` and basic repo configs at repo root (`.gitignore`, `.editorconfig`)
- [ ] T005 [P] Add initial `backend/app/main.py` (FastAPI app starter) and `frontend/src/main.jsx` (Vite entry)
- [ ] T006 [P] Add `frontend/tailwind.config.cjs` and base Tailwind setup (`frontend/postcss.config.cjs`, `frontend/src/index.css`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infra that MUST be complete before user stories

- [ ] T007 Setup SQLAlchemy engine and session in `backend/app/db.py` and local SQLite file `backend/instance/inventory.db`
- [ ] T008 [P] Create base models file `backend/app/models.py` with `Categoria` and `Producto` skeletons (see data-model.md)
- [ ] T009 Create Pydantic schemas in `backend/app/schemas.py` for Product and Category
- [ ] T010 Implement migrations or DB init script `backend/scripts/init_db.py` to create tables and optional seed data
- [ ] T011 Implement API routing structure `backend/app/api/v1/__init__.py` and include router in `backend/app/main.py`
- [ ] T012 [P] Add CORS, logging and basic error-handling middleware in `backend/app/main.py`
- [ ] T013 Create frontend API service `frontend/src/services/api.js` with base `fetch`/`axios` wrapper and config (baseURL `/api/v1`)
- [ ] T014 [P] Add ESLint/Prettier and black/isort configurations for frontend/backend (`.eslintrc`, `pyproject.toml`)

**Checkpoint**: Foundational phase complete — user stories may start

---

## Phase 3: User Story 1 - Gestionar productos (Priority: P1) 🎯 MVP

**Goal**: Full CRUD for products with persistence and a working frontend UI to create/edit/delete/view products

**Independent Test**: Create a product via frontend form, verify it appears in the table, edit quantity and delete; check CSV export includes the created product.

### Implementation

- [ ] T015 [P] [US1] Implement `Categoria` SQLAlchemy model in `backend/app/models.py`
- [ ] T016 [P] [US1] Implement `Producto` SQLAlchemy model in `backend/app/models.py` (fields: nombre, categoria_id, cantidad, precio, descripcion, creado_at, actualizado_at)
- [ ] T017 [US1] Create CRUD service functions in `backend/app/services/product_service.py` (create, list, get, update, delete)
- [ ] T018 [US1] Add Pydantic request/response models in `backend/app/schemas.py` and use them in endpoints
- [ ] T019 [US1] Implement REST endpoints in `backend/app/api/v1/products.py`:
  - `GET /products`, `POST /products`, `GET /products/{id}`, `PUT /products/{id}`, `DELETE /products/{id}`
- [ ] T020 [US1] Add CSV export endpoint in `backend/app/api/v1/products.py` `GET /products/export` that streams `text/csv; charset=utf-8`
- [ ] T021 [US1] Add unit tests for service layer in `backend/tests/test_product_service.py` (pytest)
- [ ] T022 [US1] Create frontend component `frontend/src/components/ProductsTable.jsx` to display product list and low-stock highlight
- [ ] T023 [US1] Create frontend component `frontend/src/components/ProductForm.jsx` for create/edit flows and validations
- [ ] T024 [US1] Implement frontend pages/routes in `frontend/src/pages/ProductsPage.jsx` and wire to `App.jsx`
- [ ] T025 [US1] Implement API integration in `frontend/src/services/api.js` for products (list, get, create, update, delete, export)
- [ ] T026 [US1] Add E2E/integration test skeleton for product CRUD in `frontend/tests/e2e/products.spec.js` (optional)

**Checkpoint**: US1 should be functional and testable independently

---

## Phase 4: User Story 2 - Buscar y filtrar (Priority: P1)

**Goal**: Implement search by name and filter by category on products page

**Independent Test**: Use search input and category dropdown to reduce results; responses must match API filters.

- [ ] T027 [P] [US2] Add `search` and `category` query params handling in `backend/app/api/v1/products.py` and service layer (implement LIKE search and category filter)
- [ ] T028 [P] [US2] Add indexed lookup or optimized query in `backend/app/services/product_service.py` (ensure query params applied)
- [ ] T029 [US2] Implement frontend search input `frontend/src/components/SearchBar.jsx` and category filter `frontend/src/components/CategoryFilter.jsx`
- [ ] T030 [US2] Connect frontend filters to `ProductsTable.jsx` and update API calls in `frontend/src/services/api.js`
- [ ] T031 [US2] Add integration tests for search/filter in `backend/tests/test_products_search.py`

---

## Phase 5: User Story 3 - Alertas de stock bajo (Priority: P1)

**Goal**: Visual alert when `cantidad < 5` in table rows and panel summary

**Independent Test**: Create/edit product to quantity <5 and confirm UI shows highlight and summary includes low-stock count.

- [ ] T032 [P] [US3] Add computed property or query flag `low_stock` in `backend/app/services/product_service.py` when listing products
- [ ] T033 [US3] Update product list JSON to include `low_stock` attribute (backend) in `backend/app/schemas.py`
- [ ] T034 [US3] Implement UI highlight and icon in `frontend/src/components/ProductsTable.jsx` for rows with `low_stock` true
- [ ] T035 [US3] Add low-stock count to summary endpoint or compute on frontend from listing; implement backend summary endpoint `GET /products/summary` in `backend/app/api/v1/products.py`
- [ ] T036 [US3] Add unit/integration test validating low-stock detection in `backend/tests/test_low_stock.py`

---

## Phase 6: User Story 4 - Panel resumen y exportación (Priority: P2)

**Goal**: Summary panel with total products and inventory value; frontend export button triggers CSV download

**Independent Test**: Verify summary numbers and downloaded CSV contents (UTF-8) match backend calculation.

- [ ] T037 [US4] Implement backend summary endpoint `GET /products/summary` returning `{ total_count, total_value, low_stock_count }` in `backend/app/api/v1/products.py`
- [ ] T038 [US4] Implement frontend `frontend/src/components/SummaryPanel.jsx` showing total products, total value and low-stock count
- [ ] T039 [US4] Add export button in `ProductsPage.jsx` that calls `GET /products/export` and saves `inventory.csv` via browser download
- [ ] T040 [US4] Add backend unit tests to validate summary calculations in `backend/tests/test_summary.py`

---

## Phase 7: Polish & Cross-Cutting Concerns

- [ ] T041 [P] Add frontend styling using Tailwind classes in `frontend/src/components/*.jsx` and ensure responsive layout
- [ ] T042 [P] Add input validation and error handling UI flows in `frontend/src/components/ProductForm.jsx`
- [ ] T043 [P] Add logging, request timing and basic metrics in `backend/app/main.py` and services
- [ ] T044 [P] Write README and update `specs/001-gestion-inventario/quickstart.md` with any changed run steps
- [ ] T045 [P] Run formatting and linting across repo and fix issues (`npm run lint`, `black .`)
- [ ] T046 [P] Add additional unit tests in `backend/tests/` and `frontend/tests/` to reach minimal coverage for critical paths
- [ ] T047 [ ] Validate `quickstart.md` by running the dev start commands locally and confirm APIs reachable

---

## Phase 1.5: Frontend Redesign (Priority: P1)

**Purpose**: Rediseñar completamente el frontend React + Tailwind para usuarios no técnicos manteniendo backend sin cambios.

- [ ] T050 Define design tokens and color palette in `frontend/tailwind.config.cjs` and `frontend/src/styles/colors.js`
- [ ] T051 [P] Create reusable component `frontend/src/components/Card.jsx` (props: title, children, actions)
- [ ] T052 [P] Create reusable component `frontend/src/components/Table.jsx` with support for column definitions, sorting and row highlight for low stock
- [ ] T053 [P] Create reusable component `frontend/src/components/ModalForm.jsx` with accessible markup and keyboard handling
- [ ] T054 [P] Create `frontend/src/components/SearchBar.jsx` with debounced input and clear button
- [ ] T055 [P] Implement `frontend/src/components/Toast.jsx` notification system (success, error, info) and global provider
- [ ] T056 Implement `frontend/src/pages/Dashboard.jsx` with metrics (total products, inventory value, low-stock count) and quick actions (crear producto, exportar CSV)
- [ ] T057 Implement localized navigation `frontend/src/components/NavBar.jsx` with icons and Spanish labels
- [ ] T058 Ensure responsive layout and test on desktop/tablet breakpoints; add CSS utilities or Tailwind variants if needed
- [ ] T059 Add integration wiring to existing `frontend/src/services/api.js` endpoints and error handling to trigger `Toast` notifications
- [ ] T060 [P] Update `frontend/src/App.jsx` to use new navigation and route to `Dashboard` and `ProductsPage`
- [ ] T061 Document component usage in `frontend/README.md` (short examples)


## Dependencies & Execution Order

- **Phase 1** (Setup): T001–T006 — can start immediately
- **Phase 2** (Foundational): T007–T014 — BLOCKS user story phases until complete
- **User Stories**: T015–T040 — depend on Foundational (T007–T014)
- **Polish**: T041–T047 — can run in parallel after user stories

### Parallel opportunities

- Tasks marked `[P]` can be done in parallel by different developers (e.g., T008 and T009, frontend vs backend tasks).
- After Foundational completion, User Stories (US1, US2, US3) can proceed in parallel.

## Implementation Strategy

1. Complete Phases 1 and 2 to establish the repository, runtime, DB and API wiring.
2. Implement US1 fully (T015–T026) as MVP and validate end-to-end (quickstart validation T047).
3. Add US2 and US3 in parallel; each story should include its tests and be independently demoable.
4. Implement US4 (summary + export) and finalize styling and docs.
