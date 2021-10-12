from sqlalchemy.orm import Session
from model.machine import Machine
from fastapi import HTTPException

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
