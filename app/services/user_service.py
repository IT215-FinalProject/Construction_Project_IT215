from fastapi import HTTPException

from app.models.user import User
from app.core.security import hash_password, verify_password


# Đăng ký
def register_user(db,email,password,full_name):

    user = db.query(User).filter(User.email == email).first()

    if user:
        raise HTTPException(
            status_code=400,
            detail="Email đã tồn tại"
        )

    user = User(
        email=email,
        password=hash_password(password),
        full_name=full_name,
        role="USER",
        is_active=True
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# Đăng nhập
def login_user(db, email, password):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Email hoặc password sai"
        )

    if not verify_password(
        password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Email hoặc password sai"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="Tài khoản không hoạt động"
        )

    return user