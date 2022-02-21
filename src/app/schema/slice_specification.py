from pydantic import BaseModel
from typing import Optional, List
from schema.generics import DateTimeModelMixin, IDModelMixin

class CuraParameterIn(BaseModel):
    no_extruder: int
    key: str
    value: str

class CuraParameterOut(IDModelMixin):
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
    cura_parameters: Optional[List[CuraParameterIn]]
