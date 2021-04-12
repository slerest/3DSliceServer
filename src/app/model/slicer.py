from pydantic import BaseModel

class SlicerOut(BaseModel):
    id: int
    name: str
    version: str
    host: str
    port: str

class SlicerIn(BaseModel):
    id: int
    name: str
    version: str
    host: str
    port: str
