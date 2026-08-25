from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User

from app.schemas.construction_site import (
    ConstructionSiteCreate,
    ConstructionSiteUpdate,
    ConstructionSiteResponse
)

from app.schemas.site_member import (
    SiteMemberCreate,
    SiteMemberResponse
)

from app.dependencies.dependencies import get_current_user

from app.services.construction_site_service import (
    create_site,
    get_sites,
    get_site,
    update_site,
    delete_site,
    add_member,
    get_members,
    remove_member
)


router = APIRouter(
    prefix="/construction-sites",
    tags=["Construction Site"]
)


# Tạo công trình
@router.post("/", response_model=ConstructionSiteResponse)
def create_construction_site(
    data: ConstructionSiteCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return create_site(db, data, user)


# Danh sách công trình
@router.get("/", response_model=list[ConstructionSiteResponse])
def get_construction_sites(
    search: str | None = None,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_sites(db, user, search)


# Chi tiết công trình
@router.get(
    "/{site_id}",
    response_model=ConstructionSiteResponse
)
def get_construction_site(
    site_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_site(db, site_id, user)


# Cập nhật công trình
@router.patch(
    "/{site_id}",
    response_model=ConstructionSiteResponse
)
def update_construction_site(
    site_id: int,
    data: ConstructionSiteUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return update_site(db, site_id, data, user)


# Xóa công trình
@router.delete("/{site_id}")
def delete_construction_site(
    site_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    delete_site(db, site_id, user)

    return {
        "message": "Xóa công trình thành công"
    }


# Thêm member
@router.post(
    "/{site_id}/members",
    response_model=SiteMemberResponse
)
def create_member(
    site_id: int,
    data: SiteMemberCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return add_member(db,site_id,data.user_id,user)


# Danh sách member
@router.get(
    "/{site_id}/members",
    response_model=list[SiteMemberResponse]
)
def get_site_members(
    site_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_members(db, site_id, user)


# Xóa member
@router.delete(
    "/{site_id}/members/{user_id}"
)
def delete_member(
    site_id: int,
    user_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    remove_member(db,site_id,user_id,user)

    return {
        "message": "Xóa member thành công"
    }