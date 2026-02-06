# db/models/receipt_item.py
from sqlalchemy import Column, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from code.database.base import Base

class ReceiptItem(Base):
    __tablename__ = "receipt_items"

    # Foreign Key:
    receipt_id = ForeignKey("receipts.id", ondelete="CASCADE")

    # Properties:
    description = String(255)
    amount = Numeric(10, 2)
    category_guess = String(100)
    confidence = Numeric(5, 2)

    # Relationship:
    receipt = relationship("Receipt", back_populates="items")
