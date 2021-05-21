from schema.user import UserLogin, UserIn
from model.user import User
from sqlalchemy.orm import Session
from fastapi import HTTPException
import hashlib

def login(user: UserLogin) -> bool:
    u = db.query(User).filter(User.username == user.username).first()
    # username not exist
    if u is None:
        return False
    #TODO SHA-256
    hash_password = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        user.password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
    )
    if u.password == hash_password:
        return True
    return False

def create_user(u_in: UserIn, db: Session) -> User:
    u = User(**u_in.dict())
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
