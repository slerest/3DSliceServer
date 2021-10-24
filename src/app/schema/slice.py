from typing import Optional
import datetime
from enum import Enum
from schema.material import MaterialOut
from schema.part import PartOut
from schema.slicer import SlicerOut
from schema.generics import DateTimeModelMixin, IDModelMixin

# slerest 18/10/2021
# TODO
# do a queue with position when slicer server is busy

class SliceStatus(str, Enum):
    sliced = "sliced"
    slicing = "slicing"
#    in_queue = "in_queue"
    error = "error"
    no_slice = "no_slice"

# slerest 22/03/2021
# TODO
# finir de setup tout les model de Slice, Slicer et ca sera deja pas mal

class SliceOut(DateTimeModelMixin, IDModelMixin):
    gcode: str
    print_time: Optional[datetime.timedelta]
    slice_time: Optional[datetime.timedelta]
    material: MaterialOut
    part: PartOut
    status: SliceStatus
    slicer: SlicerOut
