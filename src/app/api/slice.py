from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from fastapi_jwt_auth import AuthJWT
from typing import List
from sqlalchemy.orm import Session
from schema.slice import SliceOut
from model.slice import Slice
from core.settings import settings
import crud.slice as crud_slice
from dependencies.database import get_db
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("", response_model=List[SliceOut], name="slices:list-slices")
async def list_slices(
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> List[PartOut]:
    Authorize.jwt_required()
    all_s = crud_slice.list_slices(db, Authorize.get_jwt_subject())
    if all_s is None:
        return []
    for i, s in enumerate(all_s):
        all_s[i] = all_s[i].ToSliceOut()
    return all_s

@router.get("/{id_slice}", response_model=SliceOut, name="slices:get-slice")
async def get_slice(
        id_slice: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> PartOut:
    Authorize.jwt_required()
    r = crud_permission_slice.check_slice_right(db, Authorize.get_jwt_subject(), id_slice)
    if not r.read:
        raise HTTPException(status_code=401, detail="Unauthorized access")
    p = crud_slice.get_slice(db, id_slice)
    return s.ToSliceOut()
