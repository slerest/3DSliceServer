from fastapi import (
    APIRouter,
    Depends,
    Query
)
from fastapi_jwt_auth import AuthJWT
from typing import List, Optional
from sqlalchemy.orm import Session
from schema.material import MaterialOut
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
