from pydantic import BaseModel


# Schema dùng cho công trình
class ConstructionSiteBase(BaseModel):
    name: str
    description: str | None = None
    location: str | None = None


class ConstructionSiteCreate(ConstructionSiteBase):
    owner_id: int


class ConstructionSiteUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    location: str | None = None


class ConstructionSiteResponse(ConstructionSiteBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True