from sqlalchemy import (Column,Integer,String,Text,ForeignKey,DateTime)
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base


# Model lưu hạng mục thi công
class WorkItem(Base):
    __tablename__ = "work_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    assignee_id = Column(Integer,ForeignKey("users.id"),nullable=True)
    status = Column(String(20),default="TODO")
    priority = Column(String(20),default="MEDIUM")
    due_date = Column(DateTime,nullable=True)
    construction_site_id = Column(Integer,ForeignKey("construction_sites.id"),nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow)

    construction_site = relationship("ConstructionSite",back_populates="work_items")
    assignee = relationship("User")