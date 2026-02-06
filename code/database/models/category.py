# db/models/category.py
from sqlalchemy import Column,String, ForeignKey
from sqlalchemy.orm import relationship
from code.database.base import Base

class Category(Base):
    __tablename__ = "categories"

    # Foreign Key:
    user_id = ForeignKey("users.id", ondelete="CASCADE")

    # Properties:
    name = Column(String(100), nullable=False)
    icon = String(50)
    color = String(20)

    # Relationship:
    user = relationship("User", back_populates="categories")
    expenses = relationship("Expense", back_populates="category")
