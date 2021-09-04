from model.user import User
from model.group import Group
from model.user_group import UserGroup
from model.permission_part import PermissionPart
from schema.permission_part import PermissionPartOut
from schema.permission_part import RightsPart
from sqlalchemy.orm import Session
from fastapi import HTTPException

def check_part_right(
        db: Session,
        username: str,
        id_part: int) -> RightsPart:
    u = db.query(User).filter(User.username == username).first()
    # Check is user exists in database
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    if u.superuser:
        return RightsPart(read=True, write=True, delete=True)
    # Check is user is super user, in that case, he has all the rights
    # Get direct part's permission information
    p = db.query(PermissionPart).filter(
            PermissionPart.part_id == id_part,
            PermissionPart.user_id == u.id).first()
    # Return the direct rights that was given to user
    # direct right bypass group'user right on the part
    if p is not None:
        return RightsPart(read=p.read, write=p.write, delete=p.delete)
    # get group of user
    groups_user = db.query(Group).join(UserGroup).filter(UserGroup.user_id == u.id).all()
    groups_user_id = [g.id for g in groups_user]
    res_read, res_write, res_delete = False, False, False
    for g in groups_user:
        p = db.query(PermissionPart).filter(
                PermissionPart.part_id == id_part,
                PermissionPart.group_id == g.id).first()
        if p is None:
            continue
        res_read = True if p.read else res_read
        res_write = True if p.write else res_write
        res_delete = True if p.delete else res_delete
    return RightsPart(read=res_read, write=res_write, delete=res_delete)

def create_permission_part_user(
        db: Session,
        id_part: int,
        username: str,
        read=True,
        write=True,
        delete=True) -> PermissionPartOut:
    u = db.query(User).filter(User.username == username).first()
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    if u.superuser:
        return None
    perm = PermissionPart(
            user_id=u.id,
            group_id=None,
            part_id=id_part,
            read=read,
            write=write,
            delete=delete)
    db.add(perm)
    db.commit()
    db.refresh(perm)
    return perm.ToPermissionPartOut(db)
