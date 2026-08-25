from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserRegister, UserLogin
from app.services.user_service import (register_user,login_user)
from app.core.security import create_token


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


# Đăng ký
@router.post("/register")
def register(
    data: UserRegister,
    db: Session = Depends(get_db)
):
    user = register_user(db,data.email,data.password,data.full_name)

    return {
        "message": "Đăng ký thành công",
        "user_id": user.id
    }


# Đăng nhập
@router.post("/login")
def login(
    data: UserLogin,
    db: Session = Depends(get_db)
):
    user = login_user(
        db,
        data.email,
        data.password
    )

    token = create_token(user.id)

    return {
        "access_token": token,
        "token_type": "bearer"
    }