from pydantic import BaseModel
from schema.generics import DateTimeModelMixin, IDModelMixin
from typing import Optional

class SlicerOut(DateTimeModelMixin, IDModelMixin):
    name: str
    version: str
    host: Optional[str]
    port: Optional[str]

class SlicerIn(BaseModel):
    name: str
    version: str
    host: Optional[str]
    port: Optional[str]

class SlicerPatch(BaseModel):
    name: Optional[str]
    version: Optional[str]
    host: Optional[str]
    port: Optional[str]
