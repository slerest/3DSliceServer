import logging
import os
from sqlalchemy import or_
from sqlalchemy.orm import Session
from schema.part import PartIn, PartModify
from model.part import Part
from model.user import User
from model.group import Group
from model.user_group import UserGroup
from model.permission import Permission
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
    if os.path.isfile(path_tmp_file):
        os.remove(path_tmp_file)
    f = open(path_tmp_file, 'wb')
    f.write(p.file)
    f.close()
    return p, path_tmp_file


def list_parts(db: Session, username: str) -> [Part]:
    # TODO
    u = db.query(User).filter(User.username == username).first()
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    grps = db.query(Group).join(UserGroup).filter(UserGroup.user_id == u.id).all()
    g_ids = [g.id for g in grps]
    perm_read_user = db.query(Permission).filter(Permission.user_id == u.id).all()
    perm_read_users_group = db.query(Permission).filter(Permission.group_id._in(g_ids)).all()
    p = db.query(Part).filter(or_(Part.id.in_(part_id_perm_read), ))
    # TODO lister que les part ou l'on a les droit read direct
    # et aussi les part ou le groupe auquel on appartient a les droit read
    # SELECT * FROM PART
    # WHERE PART.ID IN (USER_DIRECT_PERM_READ)
    # OR PART.ID (USER_GROUP_PERM_READ)
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

def modify_part(db: Session, id_part: int, p_modify: PartModify):
    p = db.query(Part).filter(Part.id == id_part).first()
    if p is None:
        raise HTTPException(status_code=404, detail="Part not found")
    p.name = p_modify.name
    p.unit = p_modify.unit
    p.format: p_modify.format
    db.commit()
    db.refresh(p)
    return p
