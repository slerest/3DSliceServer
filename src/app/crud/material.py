from sqlalchemy.orm import Session
from model.material import Material
from schema.material import MaterialIn
from fastapi import HTTPException

def list_materials(
        db: Session,
        supplier,
        name,
        general_type,
        specific_type) -> [Material]:
    m = db.query(Material)
    m = m.filter(Material.supplier == supplier) if supplier is not None else m
    m = m.filter(Material.name == name) if name is not None else m
    m = m.filter(Material.general_type == general_type) if general_type is not None else m
    m = m.filter(Material.specific_type == specific_type) if specific_type is not None else m
    return m.all()

def get_material(id_material: int, db: Session) -> Material:
    m = db.query(Material).filter(Material.id == id_material).first()
    if m is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return m

def create_material(m_in: MaterialIn, db: Session) -> Material:
    m = Material(**m_in.dict())
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

def delete_material(db: Session, id_material: int):
    m = db.query(Material).filter(Material.id == id_material).first()
    if m is None:
        raise HTTPException(status_code=404, detail="Material not found")
    db.delete(m)
    db.commit()
