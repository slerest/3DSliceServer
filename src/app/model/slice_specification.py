from model.base import BaseModel
from model.cura_parameter import CuraParameter
from schema.slice_specification import SliceSpecificationOut
from sqlalchemy import (
        Column,
        String
)
from sqlalchemy.orm import relationship

class SliceSpecification(BaseModel):
    __tablename__ = 'SLICE_SPECIFICATION'

    cura_definition_file_e1 = Column('CURA_DEFINITION_FILE_E1', String, default=None, nullable=True)
    cura_definition_file_e2 = Column('CURA_DEFINITION_FILE_E2', String, default=None, nullable=True)
    slice_spec_slice = relationship("Slice", back_populates='slice_spec')
    cura_param = relationship("CuraParameter", back_populates='cura_param_slice_spec')

    def ToSliceSpecificationOut(self) -> SliceSpecificationOut:
        return SliceSpecificationOut(
            id = self.id,
            cura_definition_file_e1 = self.cura_definition_file_e1,
            cura_definition_file_e2 = self.cura_definition_file_e2,
            created_at = self.created_at,
            updated_at = self.updated_at
        );
