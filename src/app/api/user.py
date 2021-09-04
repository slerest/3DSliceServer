from fastapi import (
    APIRouter,
    Depends,
    Query
)

from fastapi_jwt_auth import AuthJWT
from typing import List
from sqlalchemy.orm import Session
from schema.user import UserOut, UserIn, UserPatch
from schema.permission import PermissionOut
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
    if not crud_user.check_superuser(db, Authorize.get_jwt_subject()):
        raise HTTPException(status_code=401, detail="Unauthorized access")
    if email is not None:
        return [crud_user.get_user_by_email(email, db).ToUserOut()]
    if username is not None:
        return [crud_user.get_user_by_username(username, db).ToUserOut()]
    users = crud_user.list_users(db)
    if users is None:
        return []
    for i, u in enumerate(users):
        users[i] = users[i].ToUserOut()
    return users


@router.get("/{id_user}", response_model=UserOut, name="users:get-user")
async def get_user(
        id_user: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> UserOut:
    Authorize.jwt_required()
    if not crud_user.check_read_user(db, Authorize.get_jwt_subject(), id_user):
        raise HTTPException(status_code=401, detail="Unauthorized access")
    u = crud_user.get_user(id_user, db)
    return u.ToUserOut()

@router.get("/{id_user}/permission", response_model=List[PermissionOut], name="users:list-permission")
async def list_user_permissions(
        id_user: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> UserOut:
    Authorize.jwt_required()
    if not crud_user.check_read_user(db, Authorize.get_jwt_subject(), id_user):
        raise HTTPException(status_code=401, detail="Unauthorized access")
    parts = crud_user.list_user_permissions(id_user, db)
    if parts is None:
        return []
    for i, p in enumerate(parts):
        parts[i] = parts[i].ToPermissionOut(db)
    return parts

@router.get("/{id_user}/groups", response_model=List[GroupOut], name="users:list-groups")
async def list_groups_of_user(
        id_user: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> List[GroupOut]:

    Authorize.jwt_required()
    if not crud_user.check_read_user(db, Authorize.get_jwt_subject(), id_user):
        raise HTTPException(status_code=401, detail="Unauthorized access")
    groups = crud_user.list_groups_of_user(id_user, db)
    if groups is None:
        return []
    for i, g in enumerate(groups):
        groups[i] = groups[i].ToGroupOut()
    return groups

# TODO create user with disable == True and send a email confirmation for validation account
@router.post("", response_model=UserOut, name="users:create-user")
async def create_user(
        user: UserIn,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> UserOut:
    u = crud_user.create_user(user, db)
    return u.ToUserOut()

@router.patch("/{id_user}", response_model=UserOut, name="users:modify-user")
async def patch_user(
        id_user: int,
        user: UserPatch,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> UserOut:
    Authorize.jwt_required()
    superuser, check_user = crud_user.check_modify_user(db, Authorize.get_jwt_subject(), id_user)
    if not superuser and not check_user:
        raise HTTPException(status_code=401, detail="Unauthorized access")
    u = crud_user.patch_user(db, user, id_user)
    return u.ToUserOut()

@router.delete("/{id_user}", status_code=204, name="users:delete-user")
async def delete_user(
        id_user: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)):
    Authorize.jwt_required()
    if not crud_user.check_superuser(db, Authorize.get_jwt_subject()):
        raise HTTPException(status_code=401, detail="Unauthorized access")
    u = crud_user.delete_user(db, id_user)
