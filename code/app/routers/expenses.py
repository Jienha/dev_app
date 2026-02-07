from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from code.database.models.expense import Expense
from code.app.deps import get_db
from code.app.schemas.expense import ExpenseCreate

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.post("/")
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@router.get("/")
def list_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).filter(Expense.deleted_at.is_(None)).all()
