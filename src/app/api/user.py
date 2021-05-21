from fastapi import (
    APIRouter,
    Depends,
    Query
)
import logging
from typing import List
from sqlalchemy.orm import Session
from schema.user import UserOut, UserIn
from dependencies.database import get_db
import crud.user as crud_user
from typing import Optional
from pydantic import EmailStr

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("", response_model=List[UserOut], name="users:list-users")
async def list_users(
        email: Optional[EmailStr] = Query(
            None,
            title="Email",
            description="Query string for filter user by email",
        ),
        username: Optional[str] = Query(
            None,
            title="Username",
            description="Query string for filter user by username",
        ),
        db: Session = Depends(get_db)) -> List[UserOut]:

    if email is not None:
        return [crud_user.get_user_by_email(email, db).ToUserOut()]
    if username is not None:
        return [crud_user.get_user_by_username(username, db).ToUserOut()]
    all_u = crud_user.list_users(db)
    for i, u in enumerate(all_u):
        all_u[i] = all_u[i].ToUserOut()
    return all_u


@router.get("/{id_user}", response_model=UserOut, name="users:get-user")
async def get_user(id_user: int, db: Session = Depends(get_db)) -> UserOut:
    u = crud_user.get_user(id_user, db)
    return u.ToUserOut()

@router.post("", response_model=UserOut, name="users:create-user")
async def create_user(user: UserIn, db: Session = Depends(get_db)) -> UserOut:
    u = crud_user.create_user(user, db)
    return u.ToUserOut()
