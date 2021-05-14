import logging
from sqlalchemy.orm import Session
from schema.part import PartIn
from model.part import Part

logger = logging.getLogger(__name__)

def create_part(db: Session, p_in: PartIn):
    p = Part(**p_in.dict())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p
