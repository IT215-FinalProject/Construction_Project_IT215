from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.db.database import Base, engine

from app.core.exception import (
    http_exception_handler,
    validation_exception_handler
)

# Import model để SQLAlchemy nhận diện bảng
from app.models.user import User
from app.models.construction_site import ConstructionSite
from app.models.site_member import SiteMember
from app.models.work_item import WorkItem

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.construction_site import (
    router as construction_site_router
)


# Tạo bảng database
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Construction Site Management API"
)


# Xử lý lỗi HTTP
app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

# Xử lý lỗi 422
app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)


# Đăng ký router
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(construction_site_router)


# API Home
@app.get("/")
def home():
    return {
        "status_code": 200,
        "message": "Construction Site Management API",
        "data": None,
        "error": None
    }


# API Health
@app.get("/health")
def health_check():
    return {
        "status_code": 200,
        "message": "API is running",
        "data": {
            "status": "healthy"
        },
        "error": None
    }