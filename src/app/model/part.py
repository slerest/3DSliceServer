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
    x: float
    y: float
    z: float

class PartIn(DateTimeModelMixin, IDModelMixin):
    name: str
    unit: str
    format: str
