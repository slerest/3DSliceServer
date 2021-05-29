from schema.user import UserLogin, UserIn
from model.user import User
from model.group import Group
from model.user_group import UserGroup
from sqlalchemy.orm import Session
from fastapi import HTTPException
import hashlib
import logging

logger = logging.getLogger(__name__)

def login(user: UserLogin, db: Session) -> bool:
    u = db.query(User).filter(User.username == user.username).first()
    # username not exist
    if u is None:
        return False
    hash_password = hashlib.sha256(user.password.encode()).hexdigest()
    if u.password == hash_password:
        return True
    return False

def create_user(u_in: UserIn, db: Session) -> User:
    u = User(**u_in.dict())
    u.password = hashlib.sha256(u.password.encode()).hexdigest()
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

def delete_user(id_user, db: Session) -> User:
    u = db.query(User).filter(User.id == id_user).first()
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(u)
    db.commit()


def list_users(db: Session) -> [User]:
    u = db.query(User).all()
    return u

def get_user(id_user: int, db: Session) -> User:
    u = db.query(User).filter(User.id == id_user).first()
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    return u

def get_user_by_username(username: str, db: Session) -> User:
    u = db.query(User).filter(User.username == username).first()
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    return u

def get_user_by_email(email: str, db: Session) -> User:
    u = db.query(User).filter(User.email == email).first()
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    return u

def get_user_group(id_user: int, db: Session) -> Group:
    g = db.query(Group).join(UserGroup).filter(UserGroup.user_id == id_user).all()
    return g
