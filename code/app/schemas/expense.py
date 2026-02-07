from pydantic import BaseModel
from datetime import date
from uuid import UUID

class ExpenseCreate(BaseModel):
    amount: float
    category_id: UUID | None
    date: date
    note: str | None

class ExpenseOut(ExpenseCreate):
    id: UUID
