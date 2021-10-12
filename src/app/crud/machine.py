from sqlalchemy.orm import Session
from model.machine import Machine
from fastapi import HTTPException
from schema.machine import MachineIn, MachinePatch

def list_machines(
        db: Session,
        manufacturer,
        model) -> [Machine]:
    m = db.query(Machine)
    m = m.filter(Machine.manufacturer == manufacturer) if manufacturer is not None else m
    m = m.filter(Machine.model == model) if model is not None else m
    return m.all()

def get_machine(id_machine: int, db: Session) -> Machine:
    m = db.query(Machine).filter(Machine.id == id_machine).first()
    if m is None:
        raise HTTPException(status_code=404, detail="machine not found")
    return m

def create_machine(m_in: MachineIn, db: Session) -> Machine:
    m = Machine(**m_in.dict())
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

def patch_machine(db: Session, machine: MachinePatch, id_machine: int) -> Machine:
    m = db.query(Machine).filter(Machine.id == id_machine).first()
    if m is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    for var, value in vars(machine).items():
        setattr(m, var, value) if value else None
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

def delete_machine(db: Session, id_machine: int):
    m = db.query(Machine).filter(Machine.id == id_machine).first()
    if m is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    db.delete(m)
    db.commit()
