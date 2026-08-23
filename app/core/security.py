import bcrypt
import jwt
from datetime import datetime, timedelta

from app.core.config import settings


# Mã hóa password
def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


# Kiểm tra password
def verify_password(password, hashed_password):
    return bcrypt.checkpw(
        password.encode(),
        hashed_password.encode()
    )


# Tạo token
def create_token(user_id):
    data = {
        "sub": str(user_id),
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    return jwt.encode(
        data,
        settings.SECRET_KEY,
        algorithm="HS256"
    )