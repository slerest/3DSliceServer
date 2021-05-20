from fastapi import (
    APIRouter,
    Depends
)
import logging
from typing import List
from sqlalchemy.orm import Session
from schema.user import UserOut
from dependencies.database import get_db
import crud.user as crud_user

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("", response_model=List[UserOut], name="users:list-users")
async def list_users(db: Session = Depends(get_db)) -> List[UserOut]:
    all_u = crud_user.list_users(db)
    for i, u in enumerate(all_u):
        all_u[i] = all_u[i].ToUserOut()
    return all_u

@router.get("/(id_user}", response_model=List[UserOut], name="users:list-user")
async def list_users(id_user: int, db: Session = Depends(get_db)) -> List[UserOut]:
    all_u = crud_user.list_users(db)
    for i, u in enumerate(all_u):
        all_u[i] = all_u[i].ToUserOut()
    return all_u
