from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from model.generics import DateTimeModelMixin, IDModelMixin

class PartOut(DateTimeModelMixin, IDModelMixin):
    name: str
    unit: str
    volume: Optional[float]
    volume_support: Optional[float]
    format: str
    x: Optional[float]
    y: Optional[float]
    z: Optional[float]

class PartIn(BaseModel):
    name: str
    unit: str
    format: str # TODO doit etre un enum
