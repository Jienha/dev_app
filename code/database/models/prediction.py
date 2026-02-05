# db/models/prediction.py
from sqlalchemy import String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from code.database.base import Base

class Prediction(Base):
    __tablename__ = "predictions"

    user_id = ForeignKey("users.id", ondelete="CASCADE")

    type = String(50)  # monthly_forecast | anomaly
    value = Numeric(10, 2)
    confidence = Numeric(5, 2)
    valid_for = DateTime(timezone=True)

    user = relationship("User", back_populates="predictions")
