from sqlalchemy.orm import Session
from model.slicer import Slicer
from fastapi import HTTPException
from schema.slicer import SlicerIn, SlicerPatch

def list_slicers(db: Session) -> [Slicer]:
    s = db.query(Slicer)
    return s.all()

def get_slicer(id_slicer: int, db: Session) -> Slicer:
    s = db.query(Slicer).filter(Slicer.id == id_slicer).first()
    if s is None:
        raise HTTPException(status_code=404, detail="slicer not found")
    return s

def create_slicer(s_in: SlicerIn, db: Session) -> Slicer:
    s = Slicer(**s_in.dict())
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

def patch_slicer(db: Session, machine: SlicerPatch, id_slicer: int) -> Slicer:
    s = db.query(Slicer).filter(Slicer.id == id_slicer).first()
    if s is None:
        raise HTTPException(status_code=404, detail="Slicer not found")
    for var, value in vars(machine).items():
        setattr(s, var, value) if value else None
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

def delete_slicer(db: Session, id_slicer: int):
    s = db.query(Slicer).filter(Slicer.id == id_slicer).first()
    if s is None:
        raise HTTPException(status_code=404, detail="Slicer not found")
    db.delete(s)
    db.commit()
