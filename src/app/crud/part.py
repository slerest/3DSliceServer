import logging
import os
from sqlalchemy.orm import Session
from schema.part import PartIn
from model.part import Part
from fastapi import HTTPException, UploadFile

logger = logging.getLogger(__name__)

def create_part(db: Session, p_in: PartIn) -> Part:
    p = Part(**p_in.dict())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

def add_file_part(db: Session, id_part: int, data: bytes) -> Part:
    p = db.query(Part).filter(Part.id == id_part).first()
    # TODO error 404 ou 204 ?
    if p is None:
        raise HTTPException(status_code=404, detail="Part not found")
    p.file =  data
    p.file_size = len(data)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

def get_file_from_id(db: Session, id_part: int):
    p = db.query(Part).filter(Part.id == id_part).first()
    if p is None:
        raise HTTPException(status_code=404, detail="Part not found")
    path_tmp_file = '/tmp/' + str(p.id) + '.stl'
    if os.path.isfile(path_tmp_file) == True:
        os.remove(path_tmp_file)
    f = open(path_tmp_file, 'wb')
    f.write(p.file)
    f.close()
    return p, path_tmp_file


def list_parts(db: Session) -> [Part]:
    p = db.query(Part).all()
    return p

def get_part(id_part: int, db: Session) -> Part:
    p = db.query(Part).filter(Part.id == id_part).first()
    if p is None:
        raise HTTPException(status_code=404, detail="Part not found")
    return p

def delete_part(id_part: int, db: Session):
    p = db.query(Part).filter(Part.id == id_part).first()
    if p is None:
        raise HTTPException(status_code=404, detail="Part not found")
    db.delete(p)
    db.commit()
