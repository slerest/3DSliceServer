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
from core.utils import get_queries
import crud.part as crud_part
import crud.permission as crud_permission
from dependencies.database import get_db
from fastapi.responses import FileResponse
from fastapi_jwt_auth import AuthJWT

router = APIRouter()

@router.get("", response_model=List[PartOut], name="parts:list-parts")
async def list_parts(
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> List[PartOut]:
    Authorize.jwt_required()
    crud_permission.check_admin(db, Authorize.get_jwt_subject())
    all_p = crud_part.list_parts(db, Authorize.get_jwt_subject())
    for i, p in enumerate(all_p):
        all_p[i] = all_p[i].ToPartOut()
    return all_p

@router.get("/{id_part}", response_model=PartOut, name="parts:get-part")
async def get_part(
        id_part: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> PartOut:
    Authorize.jwt_required()
    p_read, p_write = crud_permission.check_part_permission(
                        db, Authorize.get_jwt_subject(), id_part)
    if p_read == False:
        raise HTTPException(status_code=401, detail="Unauthorized access")
    p = crud_part.get_part(id_part, db)
    return p.ToPartOut()

@router.post("", response_model=PartOut, name="parts:create-part")
async def create_part(
        part: PartIn,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> PartOut:
    Authorize.jwt_required()
    p = crud_part.create_part(db, part)
    perm = crud_permission.create_permission(db, p.id, Authorize.get_jwt_subject())
    return p.ToPartOut()

@router.put("/{id_part}", response_model=PartOut, name="parts:modify-part")
async def modify_part(
        id_part: int,
        part: PartModify,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> PartOut:
    Authorize.jwt_required()
    p = crud_part.modify_part(db, id_part, part)
    return p.ToPartOut()

@router.post("/upload-file/{id_part}",response_model=PartOut, name="parts:upload-file-part")
async def upload_file_part(
        id_part: int,
        file_part: UploadFile = File(...),
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> PartOut:
    Authorize.jwt_required()
    data = await file_part.read()
    try:
        p = crud_part.add_file_part(db, id_part, data)
    except Exception as e:
        raise e
    return p.ToPartOut()

@router.get("/download-file/{id_part}", name="parts:download-file-part")
async def download_file_part(
        id_part: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> PartOut:
    Authorize.jwt_required()
    p, path_tmp_file = crud_part.get_file_from_id(db, id_part)
    h = {'format': p.format}
    return FileResponse(path_tmp_file, headers=h, filename=p.name)

@router.delete("/{id_part}", status_code=204, name="parts:delete-part")
async def delete_part(
        id_part: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)):
    Authorize.jwt_required()
    p = crud_part.delete_part(id_part, db)

'''

@router.get("", response_model=List[PartOut], name="parts:list-parts")
async def read_parts() -> List[PartOut]:
    try:
        # Request Database
        querie = get_queries('select_all_parts')
        results = await db.fetch_rows(querie)
        # Store values in PartOut objects
        ret = []
        for row in results:
            for v in row.values():
                ret.append(PartOut(
	            id=v[0],
                    name=v[1],
                    unit=v[2],
                    format=v[3],
                    volume=v[4],
                    volume_support=v[5],
                    x=v[6],
                    y=v[7],
                    z=v[8]
                ))
        return ret
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.post("", response_model=PartOut, name="parts:post-part")
async def create_part(part: PartIn) -> PartOut:
    try:
        querie = get_queries('create_part').format(
            name=part.name,
            unit=part.unit,
            format=part.format
        )
        result = await db.fetch_rows(querie)
        logger.info(result)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))
    return PartOut(
        name = part.name,
        unit = part.unit,
        volume = None,
        volume_support = None,
        format = part.format,
        x = None,
        y = None,
        z = None
    )

'''
