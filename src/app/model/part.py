from pydantic import BaseModel
from datetime import datetime
from model.generics import DateTimeModelMixin, IDModelMixin

class PartOut(DateTimeModelMixin, IDModelMixin):
    name: str
    unit: str
    volume: float
    volume_support: float
    file: bytes
    format: str
    x: float
    y: float
    z: float
