from core.database import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship

class CuraParameter(Base):
    __tablename__ = 'CURA_PARAMETER'

    id = Column('ID', Integer, autoincrement=True, primary_key=True)
    slicer_spec_id = Column('SLICE_SPECIFICATION_ID', Integer, ForeignKey('SLICE_SPECIFICATION.ID'), nullable=False)
    no_extruder = Column('NO_EXTRUDER', Integer, nullable=False)
    key = Column('KEY', String, nullable=False)
    value = Column('VALUE', String, nullable=False)
    cura_param_slice_spec = relationship("SliceSpecification", back_populates='cura_param')
