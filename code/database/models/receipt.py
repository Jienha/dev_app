# db/models/receipt.py
from sqlalchemy import Column, String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from code.database.base import Base

class Receipt(Base):
    __tablename__ = "receipts"

    # Foreign Key:
    user_id = ForeignKey("users.id", ondelete="CASCADE")

    # Properties:
    image_path = Column(String(255), nullable=False)
    total_detected = Numeric(10, 2)
    confidence_score = Numeric(5, 2)
    processed_at = DateTime(timezone=True)

    # Relationship:
    user = relationship("User", back_populates="receipts")
    items = relationship("ReceiptItem", back_populates="receipt")
