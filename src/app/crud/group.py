from model.group import Group
from schema.group import GroupIn
from model.user import User
from model.user_group import UserGroup
from sqlalchemy.orm import Session
from fastapi import HTTPException

def list_groups(db: Session) -> [Group]:
    g = db.query(Group).all()
    return g

def get_group_by_name(name: str, db: Session) -> Group:
    g = db.query(Group).filter(Group.name == name).first()
    if g is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return g

def get_group(id_group: int, db: Session) -> Group:
    g = db.query(Group).filter(Group.id == id_group).first()
    if g is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return g

def list_users_of_group(id_group: int, db: Session) -> [User]:
    g = db.query(User).join(UserGroup).filter(UserGroup.group_id == id_group).all()
    return g

def create_group(g_in: GroupIn, db: Session) -> Group:
    g = Group(**g_in.dict())
    db.add(g)
    db.commit()
    db.refresh(g)
    return g

def delete_group(id_group: int, db: Session):
    g = db.query(Group).filter(Group.id == id_group).first()
    if g is None:
        raise HTTPException(status_code=404, detail="Group not found")
    db.delete(g)
    db.commit()

def add_user_in_group(id_group: int, id_user: int, db: Session):
    try:
        u_g = UserGroup(group_id=id_group, user_id=id_user)
        db.add(u_g)
        db.commit()
        db.refresh(u_g)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Group or User not found")

def delete_user_in_group(id_group: int, id_user: int, db: Session):
    u_g = db.query(UserGroup).filter(
            UserGroup.group_id == id_group,
            UserGroup.user_id == id_user).first()
    if u_g is None:
        raise HTTPException(status_code=404, detail="Group or User not found")
    db.delete(u_g)
    db.commit()
