from pydantic import BaseModel
from typing import Optional
from enum import Enum
from schema.generics import DateTimeModelMixin, IDModelMixin
import logging

logger = logging.getLogger(__name__)


class PartFormat(str, Enum):
    stl = "stl"

class PartOut(DateTimeModelMixin, IDModelMixin):
    name: str
    unit: str
    size_file: Optional[int]
    volume: Optional[float]
    volume_support: Optional[float]
    format: str
    x: Optional[float]
    y: Optional[float]
    z: Optional[float]

    class Config:
        orm_mode = True


class PartIn(BaseModel):
    name: str
    unit: str
    format: PartFormat
