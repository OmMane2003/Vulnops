from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)

    password_hash = Column(String, nullable=False)

    role = Column(String, default="analyst")

    is_active = Column(Boolean, default=True)

    # user.py
    scans = relationship("Scan", back_populates="user")