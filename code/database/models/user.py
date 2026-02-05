# db/models/user.py
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from code.database.base import Base

class User(Base):
    __tablename__ = "users"

    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    last_login = DateTime(timezone=True)
    is_active = Column(Boolean, default=True)

    categories = relationship("Category", back_populates="user")
    expenses = relationship("Expense", back_populates="user")
    receipts = relationship("Receipt", back_populates="user")
    predictions = relationship("Prediction", back_populates="user")
