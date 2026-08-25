from pydantic import BaseModel


# Schema thêm member
class SiteMemberCreate(BaseModel):
    user_id: int


# Schema trả member
class SiteMemberResponse(BaseModel):
    id: int
    user_id: int
    construction_site_id: int
    role: str

    class Config:
        from_attributes = True