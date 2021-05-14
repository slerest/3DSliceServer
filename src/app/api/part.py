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
from crud.part import create_part as crud_create_part
from core.database import SessionLocal
from dependencies.database import get_db
logger = logging.getLogger(__name__)
router = APIRouter()

# Pour creer une part
# create part
# post file part with id of creating part

@router.post("", response_model=PartOut, name="parts:post-part")
async def create_part(part: PartIn, db: Session = Depends(get_db)) -> PartOut:
    #p = Part(part.name, part.unit, part.format)
    #logger.info(dir(p))
    crud_create_part(db, part)
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

@router.post("/upload-file/{id_part}", name="parts:post-part-file")
async def upload_file_part(id_part: int, stl_file: UploadFile = File(...)):
        return {"filename": file.filename}
'''
