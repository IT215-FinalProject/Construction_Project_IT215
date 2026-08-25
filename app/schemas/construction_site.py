from pydantic import BaseModel, Field


# Schema tạo công trình
class ConstructionSiteCreate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    description: str | None = None


# Schema cập nhật công trình
class ConstructionSiteUpdate(BaseModel):
    name: str | None = Field(default=None,min_length=1,max_length=150)
    description: str | None = None


# Schema trả công trình
class ConstructionSiteResponse(BaseModel):
    id: int
    name: str
    description: str | None
    owner_id: int

    class Config:
        from_attributes = True