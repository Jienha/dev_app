# db/base.py
import uuid
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    id = Column(
        default=uuid.uuid4,
        primary_key=True,
        unique=True,
        nullable=False
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
