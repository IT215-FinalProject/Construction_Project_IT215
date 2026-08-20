from fastapi import FastAPI

from app.db.database import Base, engine

from app.core.exception import (
    NotFoundException,
    BadRequestException,
    not_found_handler,
    bad_request_handler
)

# Import các model để SQLAlchemy nhận diện bảng
from app.models.user import User
from app.models.construction_site import ConstructionSite
from app.models.site_member import SiteMember
from app.models.work_item import WorkItem


# Tạo các bảng trong database
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Construction Site Management API"
)


# Đăng ký xử lý lỗi 404
app.add_exception_handler(
    NotFoundException,
    not_found_handler
)


# Đăng ký xử lý lỗi 400
app.add_exception_handler(
    BadRequestException,
    bad_request_handler
)


@app.get("/")
def home():
    return {
        "status_code": 200,
        "message": "Construction Site Management API",
        "data": None,
        "error": None
    }


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