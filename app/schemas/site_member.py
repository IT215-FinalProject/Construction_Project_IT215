from pydantic import BaseModel


# Schema dùng cho thành viên công trình
class SiteMemberCreate(BaseModel):
    user_id: int
    construction_site_id: int
    role: str = "MEMBER"


class SiteMemberResponse(SiteMemberCreate):
    id: int

    class Config:
        from_attributes = True