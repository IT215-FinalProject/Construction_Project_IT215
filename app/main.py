from fastapi import FastAPI, HTTPException
from app.db.database import Base, engine
from app.core.exception import http_exception_handler

# Import các model để SQLAlchemy nhận diện bảng
from app.models.user import User
from app.models.construction_site import ConstructionSite
from app.models.site_member import SiteMember
from app.models.work_item import WorkItem

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router


# Tạo các bảng trong database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Construction Site Management API"
)

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.include_router(auth_router)
app.include_router(users_router)


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