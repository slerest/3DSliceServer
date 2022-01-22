from model.base import BaseModel
from schema.machine import MachineOut
from sqlalchemy import (
    Column,
    Float,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

class Machine(BaseModel):
    __tablename__ = 'MACHINE'

    manufacturer = Column('MANUFACTURER', String, nullable=False)
    model = Column('MODEL', String, nullable=False)
    mode = Column('MODE', String, default=None, nullable=True)
    power = Column('POWER', String, default=None, nullable=True)
    am_process = Column('AM_PROCESS', String, default=None, nullable=True)
    general_material_type = Column('GENERAL_MATERIAL_TYPE', String, default=None, nullable=True)
    specific_material_type = Column('SPECIFIC_MATERIAL_TYPE', String, default=None, nullable=True)
    x = Column('X', Float, default=None, nullable=True)
    y = Column('Y', Float, default=None, nullable=True)
    z = Column('Z', Float, default=None, nullable=True)
    machine_slice = relationship("Slice", back_populates='machine')

    def ToMachineOut(self) -> MachineOut:
        return MachineOut(
            id = self.id,
            manufacturer = self.manufacturer,
            model = self.model,
            mode = self.mode,
            power = self.power,
            am_process = self.am_process,
            general_material_type = self.general_material_type,
            specific_material_type = self.specific_material_type,
            x = self.x,
            y = self.y,
            z = self.z,
            created_at = self.created_at,
            updated_at = self.updated_at
        )
