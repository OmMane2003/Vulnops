from sqlalchemy.orm import Session
import json
from app.models.scan import Scan
from app.scanners.nmap_scanner import NmapScanner
from app.scanners.whois_scanner import WhoisScanner
from app.scanners.dns_scanner import DNSScanner
from app.scanners.headers_scanner import HeadersScanner

class ScanService:

    @staticmethod
    def create_scan(db: Session, target: str, scan_type: str, user_id: int):
        scan = Scan(
             target=target,
             scan_type=scan_type,
             status="Running",
             user_id=user_id
        )

        db.add(scan)
        db.commit()
        db.refresh(scan)

        if scan_type == "nmap":
            scan_result = NmapScanner.scan(target)

        elif scan_type == "whois":
              scan_result = WhoisScanner.scan(target)

        elif scan_type == "dns":
              scan_result = DNSScanner.scan(target)

        elif scan_type == "headers":
              scan_result = HeadersScanner.scan(target)

        else:
            raise ValueError("Invalid scan type")

        scan.result = json.dumps(scan_result)
        scan.status = "Completed"

        db.commit()
        db.refresh(scan)

        return scan 

    @staticmethod
    def get_user_scans(db: Session, user_id: int):
        return (
             db.query(Scan)
              .filter(Scan.user_id == user_id)
              .order_by(Scan.created_at.desc())
              .all()
        )

    @staticmethod
    def get_scan(db: Session, scan_id: int, user_id: int):
        return (
             db.query(Scan)
             .filter(
                   Scan.id == scan_id,
                   Scan.user_id == user_id
             )       
             .first()
        )