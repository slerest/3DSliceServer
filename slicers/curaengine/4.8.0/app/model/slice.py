import datetime
from typing import Optional
from model.generics import DateTimeModelMixin, IDModelMixin
from fastapi import File, UploadFile

class SliceOut(DateTimeModelMixin, IDModelMixin):
    gcode: str
    print_time: Optional[datetime.timedelta]
    slice_time: Optional[datetime.timedelta]
    definition_file: str

class SliceIn(DateTimeModelMixin, IDModelMixin):
    definition_file: str
    id_file: int
