from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base


# Model lưu công trình
class ConstructionSite(Base):
    __tablename__ = "construction_sites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner = relationship("User")
    members = relationship("SiteMember", back_populates="construction_site")
    work_items = relationship("WorkItem", back_populates="construction_site")