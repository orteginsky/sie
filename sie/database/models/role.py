from ..db_base import Base

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped ,mapped_column
from datetime import datetime

"""
    id_role SERIAL PRIMARY KEY,
    role_name VARCHAR(256) NOT NULL,
    role_acronym VARCHAR(64) NOT NULL,
    modified_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
"""

class Role(Base):
    __tablename__ = "roles"

    id_role: Mapped[int] = mapped_column(primary_key=True, index=True)
    role_name: Mapped[str] = mapped_column(String(256), nullable=False)
    role_acronym: Mapped[str] = mapped_column(String(64), nullable=False)
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
