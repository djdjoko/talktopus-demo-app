from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.payments.router import router as payments_router
from app.dashboard.router import router as dashboard_router

app = FastAPI(title="Demo SaaS App", version="0.9.0")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(payments_router, prefix="/payments", tags=["payments"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["dashboard"])


@app.get("/health")
def health():
    return {"status": "ok"}
