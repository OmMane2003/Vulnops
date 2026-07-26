from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.auth.dependencies import get_current_user

from app.schemas.scan import ScanCreate, ScanResponse
from app.services.scan_service import ScanService

from fastapi import HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ScanResponse)
def create_scan(
    scan: ScanCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ScanService.create_scan(
        db=db,
        target=scan.target,
        scan_type=scan.scan_type,
        user_id=current_user.id,
    )


@router.get("/", response_model=List[ScanResponse])
def get_my_scans(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ScanService.get_user_scans(
        db=db,
        user_id=current_user.id,
    )




@router.get("/{scan_id}", response_model=ScanResponse)
def get_scan(
    scan_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    scan = ScanService.get_scan(
        db=db,
        scan_id=scan_id,
        user_id=current_user.id
    )

    if not scan:
        raise HTTPException(
            status_code=404,
            detail="Scan not found"
        )

    return scan