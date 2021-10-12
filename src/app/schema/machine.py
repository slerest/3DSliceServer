from pydantic import BaseModel
from schema.generics import DateTimeModelMixin, IDModelMixin
from typing import Optional

# data from senvol.com

class MachineOut(DateTimeModelMixin, IDModelMixin):
    manufacturer: str
    model: str
    mode: Optional[str]
    power: Optional[str]
    am_process: Optional[str]
    general_material_type: Optional[str]
    specific_material_type: Optional[str]
    x: Optional[float]
    y: Optional[float]
    z: Optional[float]

class MachineIn(BaseModel):
    manufacturer: str
    model: str
    mode: Optional[str]
    power: Optional[str]
    am_process: Optional[str]
    general_material_type: Optional[str]
    specific_material_type: Optional[str]
    x: Optional[float]
    y: Optional[float]
    z: Optional[float]

class MachinePatch(BaseModel):
    manufacturer: Optional[str]
    model: Optional[str]
    mode: Optional[str]
    power: Optional[str]
    am_process: Optional[str]
    general_material_type: Optional[str]
    specific_material_type: Optional[str]
    x: Optional[float]
    y: Optional[float]
    z: Optional[float]
