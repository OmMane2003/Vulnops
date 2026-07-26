from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ScanResponse(BaseModel):
    id: int
    target: str
    scan_type: str
    status: str
    result: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class ScanCreate(BaseModel):
    target: str
    scan_type: str


class ScanResponse(BaseModel):
    id: int
    target: str
    scan_type: str
    status: str

    class Config:
        from_attributes = True