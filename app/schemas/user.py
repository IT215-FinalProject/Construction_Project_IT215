from pydantic import BaseModel, EmailStr


# Schema đăng ký
class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: str


# Schema đăng nhập
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Schema trả thông tin User
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str
    is_active: bool

    class Config:
        from_attributes = True