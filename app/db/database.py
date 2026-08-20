from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Tạo kết nối đến MySQL
engine = create_engine(settings.DATABASE_URL)

# Tạo session làm việc với database
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base dùng để tạo các model
Base = declarative_base()

# Lấy database session
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()