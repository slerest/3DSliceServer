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
from schema.part import PartOut, PartIn, PartModify
from model.part import Part
from core.settings import settings
import crud.part as crud_part
import crud.permission_part as crud_permission_part
import crud.permission as crud_permission
from dependencies.database import get_db
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("", response_model=List[PartOut], name="parts:list-parts")
async def list_parts(
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> List[PartOut]:
    Authorize.jwt_required()
    all_p = crud_part.list_parts(db, Authorize.get_jwt_subject())
    if all_p is None:
        return []
    for i, p in enumerate(all_p):
        all_p[i] = all_p[i].ToPartOut()
    return all_p

@router.get("/{id_part}", response_model=PartOut, name="parts:get-part")
async def get_part(
        id_part: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> PartOut:
    Authorize.jwt_required()
    r = crud_permission_part.check_part_right(db, Authorize.get_jwt_subject(), id_part)
    if not r.read:
        raise HTTPException(status_code=401, detail="Unauthorized access")
    p = crud_part.get_part(id_part, db)
    return p.ToPartOut()

@router.post("", response_model=PartOut, name="parts:create-part")
async def create_part(
        part: PartIn,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> PartOut:
    Authorize.jwt_required()
    if not crud_permission.check_user_permission_create(db, Authorize.get_jwt_subject()):
        raise HTTPException(status_code=401, detail="Unauthorized access")
    p = crud_part.create_part(db, part)
    perm = crud_permission_part.create_permission_part_user(db, p.id, Authorize.get_jwt_subject())
    return p.ToPartOut()

@router.put("/{id_part}", response_model=PartOut, name="parts:modify-part")
async def modify_part(
        id_part: int,
        part: PartModify,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> PartOut:
    Authorize.jwt_required()
    r = crud_permission_part.check_part_right(db, Authorize.get_jwt_subject(), id_part)
    if not r.write:
        raise HTTPException(status_code=401, detail="Unauthorized access")
    p = crud_part.modify_part(db, id_part, part)
    return p.ToPartOut()

@router.post("/file/{id_part}",response_model=PartOut, name="parts:upload-file-part")
async def upload_file_part(
        id_part: int,
        file_part: UploadFile = File(...),
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> PartOut:
    Authorize.jwt_required()
    r = crud_permission_part.check_part_right(db, Authorize.get_jwt_subject(), id_part)
    if not r.write:
        raise HTTPException(status_code=401, detail="Unauthorized access")
    data = await file_part.read()
    try:
        p = crud_part.add_file_part(db, id_part, data)
    except Exception as e:
        raise e
    return p.ToPartOut()

@router.get("/file/{id_part}", name="parts:download-file-part")
async def download_file_part(
        id_part: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> PartOut:
    Authorize.jwt_required()
    r = crud_permission_part.check_part_right(db, Authorize.get_jwt_subject(), id_part)
    if not r.read:
        raise HTTPException(status_code=401, detail="Unauthorized access")
    p, path_tmp_file = crud_part.get_file_from_id(db, id_part)
    h = {'format': p.format}
    return FileResponse(path_tmp_file, headers=h, filename=p.name)

@router.delete("/{id_part}", status_code=204, name="parts:delete-part")
async def delete_part(
        id_part: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)):
    Authorize.jwt_required()
    r = crud_permission_part.check_part_right(db, Authorize.get_jwt_subject(), id_part)
    if not r.delete:
        raise HTTPException(status_code=401, detail="Unauthorized access")
    p = crud_part.delete_part(id_part, db)
