from fastapi import (
    APIRouter,
    Depends,
    Query
)
from fastapi_jwt_auth import AuthJWT
from typing import List, Optional
from sqlalchemy.orm import Session
from schema.machine import MachineOut
from dependencies.database import get_db
import crud.machine as crud_machine
from fastapi import HTTPException

router = APIRouter()

@router.get("", response_model=List[MachineOut], name="machines:list-machines")
async def list_machines(
        manufacturer: Optional[str] = Query(
            None,
            title="Manufacturer",
            description="Query string for filter material by manufacturer",
        ),
        model: Optional[str] = Query(
            None,
            title="Model",
            description="Query string for filter material by model",
        ),
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> List[MachineOut]:
    Authorize.jwt_required()
    machines = crud_machine.list_machines(db, manufacturer, model)
    if machines is None:
        return []
    for i, m in enumerate(machines):
        machines[i] = machines[i].ToMachineOut()
    return machines

@router.get("/{id_machine}", response_model=MachineOut, name="machine:get-machine")
async def get_machine(
        id_machine: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> MachineOut:
    Authorize.jwt_required()
    m = crud_machine.get_machine(id_machine, db)
    return m.ToMachineOut()
