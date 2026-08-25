from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse

from app.dependencies.dependencies import (get_current_user,admin_required)


router = APIRouter(
    prefix="/users",
    tags=["User"]
)


# Xem thông tin bản thân
@router.get("/me", response_model=UserResponse)
def get_me(user: User = Depends(get_current_user)):
    return user


# Admin xem danh sách User
@router.get("/", response_model=list[UserResponse])
def get_users(
    search: str = None,
    is_active: bool = None,
    db: Session = Depends(get_db),
    user: User = Depends(admin_required)
):
    query = db.query(User)

    if search:
        query = query.filter(
            (User.full_name.contains(search)) |
            (User.email.contains(search))
        )

    if is_active is not None:
        query = query.filter(User.is_active == is_active)

    return query.all()