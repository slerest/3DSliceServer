from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from model.generics import DateTimeModelMixin, IDModelMixin

class PartOut(DateTimeModelMixin, IDModelMixin):
    name: str
    unit: str
    volume: Optional[float]
    volume_support: Optional[float]
    file: Optional[bytes]
    format: str
    x: float
    y: float
    z: float
