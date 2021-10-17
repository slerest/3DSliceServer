from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from fastapi_jwt_auth import AuthJWT
from typing import List
from sqlalchemy.orm import Session
from schema.slicer import SlicerOut, SlicerIn, SlicerPatch
from model.slicer import Slicer
from core.settings import settings
import crud.slicer as crud_slicer
from dependencies.database import get_db

router = APIRouter()

@router.get("", response_model=List[SlicerOut], name="slicers:list-slicers")
async def list_slicers(
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> List[SlicerOut]:
    Authorize.jwt_required()
    all_s = crud_slicer.list_slicers(db)
    if all_s is None:
        return []
    for i, s in enumerate(all_s):
        all_s[i] = all_s[i].ToSlicerOut()
    return all_s

@router.get("/{id_slicer}", response_model=SlicerOut, name="slicers:get-slicer")
async def get_slicer(
        id_slicer: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> SlicerOut:
    Authorize.jwt_required()
    s = crud_slicer.get_slicer(id_slicer, db)
    return s.ToSlicerOut()

@router.post("", response_model=SlicerOut, name="slicers:create-slicer")
async def create_slicer(
        slicer: SlicerIn,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> SlicerOut:
    Authorize.jwt_required()
    s = crud_slicer.create_slicer(slicer, db)
    return s.ToSlicerOut()

# TODO test si il peut etre reach ou pas check si il est occuppe ou pas cpu ram healthcheck ?

@router.patch("/{id_slicer}", response_model=SlicerOut, name="slicers:modify-slicer")
async def patch_slicer(
        id_slicer: int,
        slicer: SlicerPatch,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> SlicerOut:
    Authorize.jwt_required()
    s = crud_slicer.patch_slicer(db, slicer, id_slicer)
    return s.ToSlicerOut()

@router.delete("/{id_slicer}", status_code=204, name="slicers:delete-slicer")
async def delete_slicer(
        id_slicer: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)):
    Authorize.jwt_required()
    s = crud_slicer.delete_slicer(db, id_slicer)
