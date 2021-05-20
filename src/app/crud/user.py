from schema.user import UserLogin
from model.user import User
from sqlalchemy.orm import Session
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

def list_users(db: Session) -> [User]:
    u = db.query(User).all()
    return u

