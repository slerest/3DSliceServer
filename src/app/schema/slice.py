from pydantic import BaseModel
from typing import Optional
import datetime
from enum import Enum
from schema.material import MaterialOut
from schema.part import PartOut
from schema.slicer import SlicerOut
from schema.slice_specification import SliceSpecificationOut, SliceSpecificationIn
from schema.generics import DateTimeModelMixin, IDModelMixin

# slerest 18/10/2021
# TODO do a queue with position when slicer server is busy

class SliceStatus(str, Enum):
    sliced = "sliced"
    slicing = "slicing"
#    in_queue = "in_queue"
    error = "error"
    unsliced = "unsliced"

# slerest 22/03/2021
# TODO finir de setup tout les model de Slice, Slicer et ca sera deja pas mal

class SliceOut(DateTimeModelMixin, IDModelMixin):
    print_time: Optional[datetime.timedelta]
    slice_time: Optional[datetime.timedelta]
    part: PartOut
    material: MaterialOut
    status: SliceStatus
    slicer: SlicerOut
    slice_spec: SliceSpecificationOut
    error_code: Optional[int]
    error_message: Optional[str]
    comment: Optional[str]

class SliceIn(BaseModel):
    part_id: int
    material_id: Optional[int]
    machine_id: Optional[int]
    slicer_id: int
    slice_spec: SliceSpecificationIn
    comment: Optional[str]
