from model.user import User
from model.group import Group
from model.user_group import UserGroup
from model.permission import Permission
from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Tuple

def check_part_permission(
        db: Session,
        username: str,
        id_part: int) -> Tuple[bool, bool]:
    u = db.query(User).filter(User.username == username).first()
    # Check is user exists in database
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    # Check is user is super user, in that case, he has all the rights
    if u.superuser == True:
        return True, True
    # Get direct part's permission information
    p = db.query(Permission).filter(
            Permission.part_id == id_part,
            Permission.user_id == u.id).first()
    # Return the direct rights that was given to user
    # direct right bypass group'user right on the part
    if p is not None:
        return p.read, p.write
    # get group of user
    groups_user = db.query(Group).join(UserGroup).filter(UserGroup.user_id == u.id).all()
    groups_user_id = [g.id for g in groups_user]
    res_read, res_write = False, False
    for g in groups_user:
        p = db.query(Permission).filter(
                Permission.part_id == id_part,
                Permission.group_id == g.id).first()
        if p is None:
            continue
        res_read = True if p.read else res_read
        res_write = True if p.write else res_write
    return res_read, res_write

def check_admin(db: Session, username: str):
    u = db.query(User).filter(User.username == username).first()
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    if u.superuser is False:
        raise HTTPException(status_code=401, detail="Unauthorized access")
    return True
