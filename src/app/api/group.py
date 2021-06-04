from fastapi import (
    APIRouter,
    Depends,
    Query
)

from fastapi_jwt_auth import AuthJWT
from typing import List
from sqlalchemy.orm import Session
from schema.group import GroupOut, GroupIn
from schema.user import UserOut
from dependencies.database import get_db
import crud.group as crud_group
from typing import Optional

router = APIRouter()

@router.get("", response_model=List[GroupOut], name="groups:list-groups")
async def list_groups(
        name: Optional[str] = Query(
            None,
            title="Name",
            description="Query string for filter group by name",
        ),
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> List[UserOut]:

    Authorize.jwt_required()
    if name is not None:
        return [crud_group.get_group_by_name(name, db).ToGroupOut()]
    groups = crud_group.list_groups(db)
    for i, g in enumerate(groups):
        groups[i] = groups[i].ToGroupOut()
    return groups

@router.get("/{id_group}", response_model=GroupOut, name="groups:get-group")
async def get_group(
        id_group: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> UserOut:

    Authorize.jwt_required()
    g = crud_group.get_group(id_group, db)
    return g.ToGroupOut()

@router.get("/{id_group}/users", response_model=List[UserOut], name="groups:list-users")
async def list_users_of_group(
        id_group: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> List[GroupOut]:

    Authorize.jwt_required()
    users = crud_group.list_users_of_group(id_group, db)
    for i, u in enumerate(users):
        users[i] = users[i].ToUserOut()
    return users

@router.post("", response_model=GroupOut, name="groups:create-group")
async def create_group(
        group: GroupIn,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> GroupOut:

    g = crud_group.create_group(group, db)
    return g.ToGroupOut()

@router.delete("/{id_group}", status_code=204, name="groups:delete-group")
async def delete_group(id_group: int, db: Session = Depends(get_db)):
    g = crud_group.delete_group(id_group, db)
