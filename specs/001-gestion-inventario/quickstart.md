# Quickstart — Ejecutar localmente (sin Docker)

Prerequisitos:
- Python 3.11
- Node 18+

Backend (FastAPI):

```bash
cd backend
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\Activate.ps1 or Activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Frontend (Vite + React):

```bash
cd frontend
npm install
npm run dev
```

Notas:
- La API base estará en `http://localhost:8000/api/v1` por defecto.
- Exportar CSV devuelve un `Content-Type: text/csv; charset=utf-8`.
- Para producción considerar migrar a Postgres y añadir Docker/CI.
