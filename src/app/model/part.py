from pydantic import BaseModel
from datetime import datetime

class PartOut(BaseModel):
    id: int
    name: str
    unit: str
    volume: float
    volume_support: float
    file: bytes
    format: str
    x: float
    y: float
    z: float
    created_at: datetime
    updated_at: datetime

class PartIn(BaseModel):
    name: str
    file: bytes
    format: str
