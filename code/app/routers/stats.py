from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import extract, func
from code.app.deps import get_db
from code.database.models.expense import Expense

router = APIRouter(prefix="/stats", tags=["stats"])

@router.get("/monthly")
def monthly_stats(year: int, month: int, db: Session = Depends(get_db)):
    total = db.query(
        func.sum(Expense.amount)
    ).filter(
        extract("year", Expense.date) == year,
        extract("month", Expense.date) == month,
        Expense.deleted_at.is_(None)
    ).scalar()

    return {
        "year": year,
        "month": month,
        "total_spent": total or 0
    }
