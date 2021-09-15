from fastapi import (
    APIRouter,
    Depends,
    Query
)
from fastapi_jwt_auth import AuthJWT
from typing import List, Optional
from sqlalchemy.orm import Session
from schema.material import MaterialOut, MaterialIn
from dependencies.database import get_db
import crud.material as crud_material
from fastapi import HTTPException

router = APIRouter()

@router.get("", response_model=List[MaterialOut], name="users:list-users")
async def list_materials(
        supplier: Optional[str] = Query(
            None,
            title="Supplier",
            description="Query string for filter material by supplier",
        ),
        name: Optional[str] = Query(
            None,
            title="Name",
            description="Query string for filter material by name",
        ),
        general_type: Optional[str] = Query(
            None,
            title="General type",
            description="Query string for filter material by general type",
        ),
        specific_type: Optional[str] = Query(
            None,
            title="Specific type",
            description="Query string for filter material by specific type",
        ),
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> List[MaterialOut]:
    Authorize.jwt_required()
    materials = crud_material.list_materials(
        db, supplier, name, general_type, specific_type)
    if materials is None:
        return []
    for i, u in enumerate(materials):
        materials[i] = materials[i].ToMaterialOut()
    return materials

@router.get("/{id_material}", response_model=MaterialOut, name="materials:get-material")
async def get_material(
        id_material: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> MaterialOut:
    Authorize.jwt_required()
    m = crud_material.get_material(id_material, db)
    return m.ToMaterialOut()

@router.post("", response_model=MaterialOut, name="materials:create-material")
async def create_material(
        material: MaterialIn,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> MaterialOut:
    m = crud_material.create_material(material, db)
    return m.ToMaterialOut()

@router.delete("/{id_material}", status_code=204, name="materials:delete-material")
async def delete_material(
        id_material: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)):
    Authorize.jwt_required()
    m = crud_material.delete_material(db, id_material)
