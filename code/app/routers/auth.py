from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from code.app.deps import get_db
from code.app.auth import verify_password, create_access_token
from code.database.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenziali errate")

    token = create_access_token(str(user.id))
    return {"access_token": token, "token_type": "bearer"}
