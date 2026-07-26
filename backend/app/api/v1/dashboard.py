from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.session import get_db
from app.models.scan import Scan
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/")
def get_dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    scans = db.query(Scan).filter(
        Scan.user_id == current_user.id
    )

    total_scans = scans.count()

    completed = scans.filter(
        Scan.status == "Completed"
    ).count()

    running = scans.filter(
        Scan.status == "Running"
    ).count()

    failed = scans.filter(
        Scan.status == "Failed"
    ).count()

    scan_types = (
        db.query(
            Scan.scan_type,
            func.count(Scan.id)
        )
        .filter(Scan.user_id == current_user.id)
        .group_by(Scan.scan_type)
        .all()
    )

    recent_scans = (
        db.query(Scan)
        .filter(Scan.user_id == current_user.id)
        .order_by(Scan.created_at.desc())
        .limit(5)
        .all()
    )

    return {
        "total_scans": total_scans,
        "completed_scans": completed,
        "running_scans": running,
        "failed_scans": failed,
        "scan_types": {
            scan_type: count
            for scan_type, count in scan_types
        },
        "recent_scans": recent_scans
    }