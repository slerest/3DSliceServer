import logging
from sqlalchemy.orm import Session
from schema.part import PartIn
from model.part import Part
from fastapi import HTTPException,HTTPException, UploadFile

logger = logging.getLogger(__name__)

def create_part(db: Session, p_in: PartIn) -> Part:
    p = Part(**p_in.dict())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

def add_file_part(db: Session, id_part: int, data: bytes) -> Part:
    p = db.query(Part).filter(Part.id == id_part).first()
    if p is None:
        raise HTTPException(status_code=404, detail="Part with id {} not found".format(id))
    p.file =  data
    p.file_size = len(data)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p
