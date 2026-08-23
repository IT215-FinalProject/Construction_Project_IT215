from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


# Model lưu hạng mục công việc
class WorkItem(Base):
    __tablename__ = "work_items"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(150),nullable=False)
    description = Column(Text,nullable=True)
    status = Column(String(20),default="TODO")
    priority = Column(String(20),default="MEDIUM")
    construction_site_id = Column(Integer,ForeignKey("construction_sites.id"),nullable=False)
    assignee_id = Column(Integer,ForeignKey("users.id"),nullable=True)
    construction_site = relationship("ConstructionSite",back_populates="work_items")
    assignee = relationship("User")