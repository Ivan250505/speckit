# API Contract: Gestión de Inventario (REST)

Base URL: `/api/v1`

Endpoints:

- `GET /api/v1/products` — List products
  - Query params: `search` (partial name), `category` (id or name), `page`, `limit`
  - Response: 200 OK, JSON `{items: [...], total: N}`

- `POST /api/v1/products` — Create product
  - Body: JSON `{nombre, categoria_id or categoria_nombre, cantidad, precio, descripcion}`
  - Response: 201 Created, JSON product object

- `GET /api/v1/products/{id}` — Get product
  - Response: 200 OK, product JSON or 404 if not found

- `PUT /api/v1/products/{id}` — Update product
  - Body: partial or full product fields to update
  - Response: 200 OK, updated product JSON

- `DELETE /api/v1/products/{id}` — Delete product
  - Response: 204 No Content

- `GET /api/v1/products/export` — Export visible products to CSV
  - Query params: same as list for filtering
  - Response: 200 OK, `text/csv` attachment (UTF-8)

Schemas (example):

Product JSON:

```json
{
  "id": 1,
  "nombre": "Tornillo M4",
  "categoria": { "id": 2, "nombre": "Ferretería" },
  "cantidad": 12,
  "precio": 0.25,
  "descripcion": "Pack 100 unidades",
  "creado_at": "2026-05-17T12:00:00Z"
}
```

Errors:
- 400 Bad Request — validation errors
- 404 Not Found — resource not found
- 500 Internal Server Error — unexpected

Examples:

curl list:

```bash
curl 'http://localhost:8000/api/v1/products?search=tornillo&category=Ferreter%C3%ADa'
```
