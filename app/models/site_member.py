from sqlalchemy import (Column, Integer, String, ForeignKey, DateTime, UniqueConstraint)
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base


# Model lưu thành viên công trình
class SiteMember(Base):
    __tablename__ = "site_members"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    construction_site_id = Column(Integer, ForeignKey("construction_sites.id"), nullable=False)
    role = Column(String(20), nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User")
    construction_site = relationship("ConstructionSite", back_populates="members")