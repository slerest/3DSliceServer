from pydantic import BaseModel
import datetime
from enum import Enum
from model.material import MaterialOut
from model.part import PartOut
from model.slicer import SlicerOut
from model.generics import DateTimeModelMixin, IDModelMixin

class SliceStatus(str, Enum):
    sliced = "sliced"
    slicing = "slicing"
    in_queue = "in_queue"
    error = "error"
    no_slice = "no_slice"

# slerest 22/03/2021
# TODO
# finir de setup tout les model de Slice, Slicer et ca sera deja pas mal

class SliceOut(DateTimeModelMixin, IDModelMixin):
    gcode: str
    print_time: datetime.timedelta = None
    slice_time: datetime.timedelta = None
    material: MaterialOut
    part: PartOut
    status: SliceStatus
    slicer: SlicerOut
