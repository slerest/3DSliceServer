from model.base import BaseModel
from model.slice_specification import SliceSpecification
from model.material import Material
from model.machine import Machine
from model.slicer import Slicer
from model.part import Part
from schema.slice import SliceOut
from sqlalchemy import (
        Column,
        Integer,
        Interval,
        String,
        ForeignKey
        )
from sqlalchemy.orm import Session, relationship


class Slice(BaseModel):
    __tablename__ = 'SLICE'

    gcode = Column('GCODE', String, default=None, nullable=True)
    print_time = Column('PRINT_TIME', Interval, default=None, nullable=True)
    slice_time = Column('SLICE_TIME', Interval, default=None, nullable=True)
    status = Column('STATUS', String, default='unsliced', nullable=True)
    part_id = Column('PART_ID', Integer, ForeignKey('PART.ID'), nullable=False)
    material_id = Column('MATERIAL_ID', Integer, ForeignKey('MATERIAL.ID'), nullable=True)
    machine_id = Column('MACHINE_ID', Integer, ForeignKey('MACHINE.ID'), nullable=True)
    slicer_id = Column('SLICER_ID', Integer, ForeignKey('SLICER.ID'), nullable=False)
    slice_spec_id = Column('SLICE_SPECIFICATION_ID', Integer, ForeignKey('SLICE_SPECIFICATION.ID'), nullable=False)
    error_code = Column('ERROR_CODE', Integer, default=None, nullable=True)
    error_message = Column('ERROR_MESSAGE', String, default=None, nullable=True)
    comment = Column('COMMENT', String, default=None, nullable=True)
    part = relationship("Part", back_populates="part_slice")
    slicer = relationship("Slicer", back_populates='slicer_slice')
    material = relationship("Material", back_populates='material_slice')
    machine = relationship("Machine", back_populates='machine_slice')
    slice_spec = relationship("SliceSpecification", back_populates='slice_spec_slice')

    def ToSliceOut(self, db: Session) -> SliceOut:
        # Part
        part = db.query(Part).filter(Part.id == self.part_id).first()
        if part is not None:
            part = part.ToPartOut()
        # Slicer
        slicer = db.query(Slicer).filter(Slicer.id == self.slicer_id).first()
        if slicer is not None:
            slicer = slicer.ToSlicerOut()
        # Material
        material = db.query(Material).filter(Material.id == self.material_id).first()
        if material is not None:
            material = material.ToMaterialOut()
        # Machine
        machine = db.query(Machine).filter(Machine.id == self.machine_id).first()
        if machine is not None:
            machine = machine.ToMachineOut()
        # SliceSpecification
        sp = db.query(SliceSpecification).filter(SliceSpecification.id == self.slice_spec_id).first()
        if sp is not None:
            sp = sp.ToSliceSpecificationOut()
        return SliceOut(
            id = self.id,
            print_time = self.print_time,
            slice_time = self.slice_time,
            status = self.status,
            error_code = self.error_code,
            error_message = self.error_message,
            comment = self.comment,
            part = part,
            slicer = slicer,
            material = material,
            machine = machine,
            slice_spec = sp,
            created_at = self.created_at,
            updated_at = self.updated_at
        )
