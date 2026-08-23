from pydantic import BaseModel, EmailStr


# Schema dùng cho User
class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None


class UserResponse(UserBase):
    id: int
    role: str
    is_active: bool

    class Config:
        from_attributes = True


# Đăng ký
class UserRegister(BaseModel):
    username: str
    email: str
    password: str


# Đăng nhập
class UserLogin(BaseModel):
    email: str
    password: str


# Trả thông tin User
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True