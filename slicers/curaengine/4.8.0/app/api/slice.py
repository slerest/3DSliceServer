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

@router.post("/{id_part}", response_model=SliceOut, name="slice:create-slice")
async def create_slice(
        id_part: int,
        part: SliceIn,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> SliceOut:
    Authorize.jwt_required()
    # TODO
    cmd = "CuraEngine slice -v -e1 -j {definition_file_e1}"
    perm = crud_permission.check_user_permission_part(db, id_part, Authorize.get_jwt_subject())
    if not perm.read:
        raise HTTPException(status_code=401, detail="Unauthorized access")
    s = crud_slice.create_slice(db, id_part, slice_in)
    return s.ToSliceOut()
    '''
    return True
