# VulnOps

A cybersecurity vulnerability management platform built with FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and Docker.

## Features

- JWT Authentication
- Role-Based Access Control (Admin, Analyst, Viewer)
- Nmap Port Scanner
- WHOIS Scanner
- DNS Scanner
- HTTP Security Headers Scanner
- Dashboard Analytics
- PostgreSQL Database
- Docker Support
- Swagger API Documentation

---

## 🏗️ Architecture

```mermaid
flowchart TD

A[Client]

A --> B[Swagger UI]

A --> C[REST API]

B --> D[FastAPI]

C --> D

D --> E[JWT Authentication]

E --> F[RBAC]

F --> G[Scan Service]

G --> H[Nmap Scanner]

G --> I[WHOIS Scanner]

G --> J[DNS Scanner]

G --> K[HTTP Headers Scanner]

H --> L[(PostgreSQL)]

I --> L

J --> L

K --> L

L --> M[Dashboard]

L --> N[Recent Scans]

L --> O[Statistics]
```


## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT
- Docker
- Python

---

## Project Structure

```
## 📂 Project Structure

```text
VulnOps/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── auth/
│   │   ├── database/
│   │   ├── models/
│   │   ├── scanners/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── core/
│   │
│   └── alembic/
│
├── frontend/
├── docker/
├── assets/
├── README.md
└── requirements.txt

```

---

## Installation

```bash
git clone https://github.com/OmMane2003/VulnOps.git

cd VulnOps

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## API Documentation

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📸 Screenshots

### API Documentation

![Swagger Home](assets/swagger-home.png)

### Login Endpoint

![Login](assets/login.png)

### Create Scan

![Create Scan](assets/create-scan.png)

### Dashboard

![Dashboard](assets/dashboard.png)

---

## Future Improvements

- React Dashboard
- Scan Scheduling
- PDF Report Generation
- Email Notifications
- CVE Integration
- Risk Scoring

---
## 🚀 Roadmap

- [x] JWT Authentication
- [x] Role-Based Access Control
- [x] PostgreSQL Integration
- [x] Nmap Scanner
- [x] WHOIS Scanner
- [x] DNS Scanner
- [x] HTTP Headers Scanner
- [x] Dashboard Analytics

### Planned Features

- [ ] React Frontend Dashboard
- [ ] Background Scan Queue (Celery + Redis)
- [ ] PDF Report Generation
- [ ] CVE & Vulnerability Mapping
- [ ] Email Notifications
- [ ] Scan Scheduling

---

## License

MIT License

---

## 👨‍💻 Author

**Om Mane**

B.Tech Computer Science

Cybersecurity | Python | FastAPI | PostgreSQL
