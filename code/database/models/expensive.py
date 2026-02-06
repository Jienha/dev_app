# db/models/expense.py
from sqlalchemy import (
    Column, String, ForeignKey, Numeric, Date, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from code.database.base import Base

class Expense(Base):
    __tablename__ = "expenses"

    # Foreign Key:
    user_id = ForeignKey("users.id", ondelete="CASCADE")
    category_id = ForeignKey("categories.id", ondelete="SET NULL")

    # Properties:
    amount = Column(Numeric(10, 2), nullable=False)

    # NOTE: Currency is not well difened yet. Require user preference!
    currency = Column(String(3), default="JPY") # EUR alternative 
    date = Column(Date, nullable=False)
    note = String(255)
    source = String(20)  # manual | receipt | import
    device_id = String(100)
    sync_version = String(50)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = DateTime(timezone=True)

    # Relationship:
    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")
