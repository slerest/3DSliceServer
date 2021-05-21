from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    File,
    UploadFile
)
from sqlalchemy.orm import Session
import logging
from typing import List
from schema.part import PartOut, PartIn
from model.part import Part
from core.settings import settings
from core.utils import get_queries
import crud.part as crud_part
from dependencies.database import get_db

logger = logging.getLogger(__name__)
router = APIRouter()

# Pour creer une part
# create part
# post file part with id of creating part

@router.get("", response_model=List[PartOut], name="parts:list-parts")
async def list_parts(db: Session = Depends(get_db)) -> List[PartOut]:
    all_p = crud_part.list_parts(db)
    for i, p in enumerate(all_p):
        all_p[i] = all_p[i].ToPartOut()
    return all_p

@router.get("/{id_part}", response_model=PartOut, name="parts:get-part")
async def get_part(id_part: int, db: Session = Depends(get_db)) -> PartOut:
    p = crud_part.get_part(id_part, db)
    return p.ToPartOut()

@router.post("", response_model=PartOut, name="parts:create-part")
async def create_part(part: PartIn, db: Session = Depends(get_db)) -> PartOut:
    p = crud_part.create_part(db, part)
    return p.ToPartOut()

@router.post("/upload-file/{id_part}",response_model=PartOut, name="parts:upload-file-part")
async def upload_file_part(
        id_part: int,
        file_part: UploadFile = File(...),
        db: Session = Depends(get_db)) -> PartOut:
    data = await file_part.read()
    try:
        p = crud_part.add_file_part(db, id_part, data)
    except Exception as e:
        raise e
    return p.ToPartOut()

@router.delete("/{id_part}", status_code=204, name="parts:delete-part")
async def delete_part(id_part: int, db: Session = Depends(get_db)):
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
