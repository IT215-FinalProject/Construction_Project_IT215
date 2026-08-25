from pydantic import BaseModel
from datetime import datetime


class WorkItemBase(BaseModel):
    title: str
    description: str | None = None
    status: str = "TODO"
    priority: str = "MEDIUM"
    due_date: datetime | None = None


class WorkItemCreate(WorkItemBase):
    construction_site_id: int
    assignee_id: int | None = None


class WorkItemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None
    due_date: datetime | None = None
    assignee_id: int | None = None


class WorkItemResponse(WorkItemBase):
    id: int
    construction_site_id: int
    assignee_id: int | None

    class Config:
        from_attributes = True