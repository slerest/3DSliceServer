from pydantic import BaseModel
from datetime import datetime, timedelta
from enum import Enum
from model.material import MaterialOut
from model.part import PartOut
from model.slicer import SlicerOut

class SliceStatus(str, Enum):
    sliced = "sliced"
    slicing = "slicing"
    in_queue = "in_queue"
    error = "error"
    no_slice = "no_slice"

# slerest 22/03/2021
# TODO
# finir de setup tout les model de Slice, Slicer et ca sera deja pas mal

class SliceOut(BaseModel):
    id: int
    gcode: str
    print_time: timedelta
    slice_time: timedelta
    material: MaterialOut
    part: PartOut
    status: SliceStatus
    slicer: SlicerOut
    created_at: datetime
    updated_at: datetime

class SliceIn(BaseModel):
    file: bytes
    slicer: int # id of the slicer
    material: int # id of the material
    part: int # id of the material

class SliceUpdateIn(BaseModel):
    gcode: str
    print_time: int
    slice_time: int
    material: int
    part: int
    status: SliceStatus
    slicer: int
