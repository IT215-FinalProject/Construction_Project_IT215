import jwt

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.core.config import settings


security = HTTPBearer()


# Lấy user từ token
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        data = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"]
        )

        user_id = data["sub"]

    except:
        raise HTTPException(
            status_code=401,
            detail="Token không hợp lệ"
        )

    user = db.query(User).filter(
        User.id == int(user_id)
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User không tồn tại"
        )

    return user


# Kiểm tra quyền
class RoleChecker:

    def __init__(self, role):
        self.role = role

    def __call__(
        self,
        user: User = Depends(get_current_user)
    ):
        if user.role != self.role:
            raise HTTPException(
                status_code=403,
                detail="Không có quyền"
            )

        return user


# Chỉ Admin
admin_required = RoleChecker("ADMIN")