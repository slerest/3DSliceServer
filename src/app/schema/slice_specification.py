from pydantic import BaseModel
from typing import Optional, List
from schema.generics import DateTimeModelMixin, IDModelMixin

class CuraParameterIn(BaseModel):
    slice_specification_id: int
    no_extruder: int
    key: str
    value: str

class CuraParameterOut(IDModelMixin):
    slice_specification_id: int
    no_extruder: int
    key: str
    value: str

class SliceSpecificationOut(DateTimeModelMixin, IDModelMixin):
    cura_definition_file_e0: Optional[str]
    cura_definition_file_e1: Optional[str]
    cura_prarameters: Optional[List[CuraParameterOut]]

class SliceSpecificationIn(BaseModel):
    cura_definition_file_e0: Optional[str]
    cura_definition_file_e1: Optional[str]
    cura_parameter_e0: Optional[CuraParameterIn]
    cura_parameter_e1: Optional[CuraParameterIn]
