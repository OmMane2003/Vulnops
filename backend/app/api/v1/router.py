from fastapi import APIRouter

from app.api import auth
from app.api.v1 import users, scans
from app.api.v1.dashboard import router as dashboard_router


api_router = APIRouter()

api_router.include_router(auth.router, tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(scans.router, prefix="/scans", tags=["Scans"])
api_router.include_router(dashboard_router)