from fastapi import (
    APIRouter,
    Depends,
    Query
)

from fastapi_jwt_auth import AuthJWT
from typing import List
from sqlalchemy.orm import Session
from schema.user import UserOut, UserIn
from schema.group import GroupOut
from dependencies.database import get_db
import crud.user as crud_user
from typing import Optional
from pydantic import EmailStr

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
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> List[UserOut]:

    Authorize.jwt_required()
    if email is not None:
        return [crud_user.get_user_by_email(email, db).ToUserOut()]
    if username is not None:
        return [crud_user.get_user_by_username(username, db).ToUserOut()]
    users = crud_user.list_users(db)
    for i, u in enumerate(users):
        users[i] = users[i].ToUserOut()
    return users


@router.get("/{id_user}", response_model=UserOut, name="users:get-user")
async def get_user(
        id_user: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> UserOut:

    Authorize.jwt_required()
    u = crud_user.get_user(id_user, db)
    return u.ToUserOut()

@router.get("/{id_user}/groups", response_model=List[GroupOut], name="users:get-group")
async def get_user_group(
        id_user: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> List[GroupOut]:

    Authorize.jwt_required()
    groups = crud_user.get_user_group(id_user, db)
    for i, g in enumerate(groups):
        groups[i] = groups[i].ToGroupOut()
    return groups

@router.post("", response_model=UserOut, name="users:create-user")
async def create_user(
        user: UserIn,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> UserOut:

    u = crud_user.create_user(user, db)
    return u.ToUserOut()
