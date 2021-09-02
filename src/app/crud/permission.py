from sqlalchemy.orm import Session
from fastapi import HTTPException
from model.user import User
from model.group import Group
from model.user_group import UserGroup

# TODO a refaire
def check_user_permission_create(db: Session, username: str) -> bool:
    c = False
    u = db.query(User).filter(User.username == username).first()
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    if u.superuser:
        return True
    c = u.create
    groups = db.query(Group).join(UserGroup).filter(UserGroup.user_id == id_user).all()
    for g in groups:
        c = True if g.create else c
    return c
