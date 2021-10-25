from sqlalchemy.orm import Session
from model.part import Slice
from model.user import User
from model.group import Group
from model.user_group import UserGroup
from model.permission_part import PermissionPart
from fastapi import HTTPException

def list_slices(db: Session, username: str) -> [Slice]:
    u = db.query(User).filter(User.username == username).first()
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    if u.superuser:
        return db.query(Slice).all()
    grps = db.query(Group).join(UserGroup).filter(UserGroup.user_id == u.id).all()
    g_ids = [g.id for g in grps]
    perm_read_user = db.query(PermissionPart).filter(PermissionPart.user_id == u.id).all()
    perm_read_users_group = db.query(PermissionPart).filter(PermissionPart.group_id.in_(g_ids)).all()
    parts_id = [p.part_id for p in perm_read_user]
    parts_id += [p.part_id for p in perm_read_users_group]
    if not len(parts_id):
        return None
    s = db.query(Slice).filter(Slice.part_id.in_(parts_id)).all()
    return s

def get_slice(db: Session, id_slice: int) -> Slice:
    s = db.query(Slice).filter(Slice.id == id_slice).first()
    if s is None:
        raise HTTPException(status_code=404, detail="Slice not found")
    return s
