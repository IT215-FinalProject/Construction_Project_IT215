from fastapi import HTTPException

from app.models.construction_site import ConstructionSite
from app.models.site_member import SiteMember
from app.models.user import User


# Tạo công trình
def create_site(db, data, user):

    site = ConstructionSite(name=data.name.strip(), description=data.description, owner_id=user.id)

    db.add(site)
    db.commit()
    db.refresh(site)

    # Người tạo tự động trở thành OWNER
    member = SiteMember(user_id=user.id, construction_site_id=site.id, role="OWNER")

    db.add(member)
    db.commit()

    return site


# Kiểm tra user có trong công trình không
def check_member(db, site_id, user_id):

    member = db.query(SiteMember).filter(SiteMember.construction_site_id == site_id,SiteMember.user_id == user_id).first()

    return member


# Kiểm tra user có phải owner không
def check_owner(db, site_id, user_id):

    site = db.query(ConstructionSite).filter(ConstructionSite.id == site_id).first()

    if not site:
        raise HTTPException(
            status_code=404,
            detail="Công trình không tồn tại"
        )

    if site.owner_id != user_id:
        raise HTTPException(
            status_code=403,
            detail="Chỉ OWNER mới được thực hiện"
        )

    return site


# Lấy danh sách công trình của user
def get_sites(db, user, search=None):

    query = db.query(ConstructionSite).join(SiteMember, SiteMember.construction_site_id == ConstructionSite.id).filter(
        SiteMember.user_id == user.id
    )

    if search:
        query = query.filter(ConstructionSite.name.contains(search))

    return query.all()


# Lấy chi tiết công trình
def get_site(db, site_id, user):

    site = db.query(ConstructionSite).filter(ConstructionSite.id == site_id).first()

    if not site:
        raise HTTPException(
            status_code=404,
            detail="Công trình không tồn tại"
        )

    if not check_member(db,site_id,user.id):
        raise HTTPException(
            status_code=403,
            detail="Bạn không thuộc công trình này"
        )

    return site


# Cập nhật công trình
def update_site(db, site_id, data, user):

    site = check_owner(db, site_id, user.id)

    if data.name is not None:
        site.name = data.name.strip()

    if data.description is not None:
        site.description = data.description

    db.commit()
    db.refresh(site)

    return site


# Xóa công trình
def delete_site(db, site_id, user):

    site = check_owner(db, site_id, user.id)

    db.delete(site)
    db.commit()


# Thêm member
def add_member(db, site_id, user_id, user):

    check_owner(db, site_id, user.id)
    new_user = db.query(User).filter(User.id == user_id).first()
    if not new_user:
        raise HTTPException(
            status_code=404,
            detail="User không tồn tại"
        )

    member = check_member(db, site_id, user_id)

    if member:
        raise HTTPException(
            status_code=400,
            detail="User đã là thành viên"
        )

    member = SiteMember(user_id=user_id,construction_site_id=site_id,role="MEMBER")

    db.add(member)
    db.commit()
    db.refresh(member)

    return member


# Lấy danh sách member
def get_members(db, site_id, user):

    get_site(db,site_id,user)

    return db.query(SiteMember).filter(SiteMember.construction_site_id == site_id).all()


# Xóa member
def remove_member(db,site_id,user_id,user):

    check_owner(db,site_id,user.id)
    member = check_member(db,site_id,user_id)
    
    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member không tồn tại"
        )

    if member.role == "OWNER":
        raise HTTPException(
            status_code=400,
            detail="Không thể xóa OWNER"
        )

    db.delete(member)
    db.commit()