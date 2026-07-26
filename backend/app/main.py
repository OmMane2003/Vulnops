from fastapi import FastAPI

from app.database.init_db import init_db
from app.api.v1.router import api_router

app = FastAPI(
    title="VulnOps API",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {
        "name": "VulnOps API",
        "version": "1.0.0",
        "status": "running"
    }

app.include_router(api_router)