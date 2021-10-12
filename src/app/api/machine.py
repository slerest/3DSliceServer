from fastapi import (
    APIRouter,
    Depends,
    Query
)
from fastapi_jwt_auth import AuthJWT
from typing import List, Optional
from sqlalchemy.orm import Session
from schema.machine import MachineOut, MachineIn, MachinePatch
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

@router.get("/{id_machine}", response_model=MachineOut, name="machines:get-machine")
async def get_machine(
        id_machine: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> MachineOut:
    Authorize.jwt_required()
    m = crud_machine.get_machine(id_machine, db)
    return m.ToMachineOut()

@router.post("", response_model=MachineOut, name="machines:create-machine")
async def create_machine(
        machine: MachineIn,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> MachineOut:
    Authorize.jwt_required()
    m = crud_machine.create_machine(machine, db)
    return m.ToMachineOut()

@router.patch("/{id_machine}", response_model=MachineOut, name="machines:modify-machine")
async def patch_machine(
        id_machine: int,
        machine: MachinePatch,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)) -> MachineOut:
    Authorize.jwt_required()
    m = crud_machine.patch_machine(db, machine, id_machine)
    return m.ToMachineOut()

@router.delete("/{id_machine}", status_code=204, name="machines:delete-machine")
async def delete_machine(
        id_machine: int,
        Authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)):
    Authorize.jwt_required()
    m = crud_machine.delete_machine(db, id_machine)
