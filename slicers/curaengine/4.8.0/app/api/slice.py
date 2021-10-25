from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    File,
    UploadFile
)
from fastapi_jwt_auth import AuthJWT
from typing import List
from sqlalchemy.orm import Session
from core.settings import settings
from dependencies.database import get_db
from fastapi.responses import FileResponse
from schema.slice import SliceOut, SliceIn

router = APIRouter()

@router.post("", response_model=SliceOut, name="slice:create-slice")
async def create_slice(
        part: SliceIn,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> SliceOut:
    Authorize.jwt_required()
    '''
    if not crud_permission.check_user_permission_create(db, Authorize.get_jwt_subject()):
        raise HTTPException(status_code=401, detail="Unauthorized access")
    p = crud_slice.create_slice(db, slice_in)
    perm = crud_permission_part.create_permission_part_user(db, p.id, Authorize.get_jwt_subject())
    '''
    return True
