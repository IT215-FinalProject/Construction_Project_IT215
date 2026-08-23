from sqlalchemy import Column, Integer, String, Boolean

from app.db.database import Base

# Model lưu thông tin người dùng
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50),unique=True,nullable=False)
    email = Column(String(100),unique=True,nullable=False)
    password = Column(String(255),nullable=False)
    role = Column(String(20),default="MEMBER")
    is_active = Column(Boolean,default=True)