from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

from fastapi import Depends
from app.auth.permissions import require_role


@router.get("/admin")
def admin_only(current_user=Depends(require_role("admin"))):
    return {
        "message": "Welcome Admin",
        "user": current_user.email
    }


@router.get("/analyst")
def analyst_only(current_user=Depends(require_role("admin", "analyst"))):
    return {
        "message": "Welcome Analyst",
        "user": current_user.email
    }


@router.get("/viewer")
def viewer_only(current_user=Depends(require_role("admin", "analyst", "viewer"))):
    return {
        "message": "Welcome Viewer",
        "user": current_user.email
    }