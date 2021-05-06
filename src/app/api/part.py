from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    File,
    UploadFile
)
import logging
from typing import List
from model.part import PartOut, PartIn
from core.settings import settings

logger = logging.getLogger(__name__)
router = APIRouter()

# Pour creer une part
# create part
# post file part with id of creating part

@router.get("", response_model=List[PartOut], name="parts:list-parts")
async def read_parts() -> List[PartOut]:
    logger.info(settings)
    return [PartOut(
        name = "name",
        unit = "mm",
        volume = 0.0,
        volume_support = None,
        format = "mm",
        x = 0.0,
        y = 0.0,
        z = 0.0
    )]

@router.post("", response_model=PartOut, name="parts:post-part")
async def post_part(part: PartIn) -> PartOut:
    return PartOut(
        name = "name",
        unit = "mm",
        volume = 0.0,
        volume_support = None,
        format = "mm",
        x = 0.0,
        y = 0.0,
        z = 0.0
    )

@router.post("/upload-file/{id_part}", name="parts:post-part-file")
async def post_part_file(id_part: int, stl_file: UploadFile = File(...)):
        return {"filename": file.filename}
