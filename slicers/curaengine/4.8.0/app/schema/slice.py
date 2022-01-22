import datetime
from typing import Optional, Dict
from model.generics import DateTimeModelMixin, IDModelMixin
from fastapi import File, UploadFile

class SliceOut(DateTimeModelMixin, IDModelMixin):
    gcode: str
    print_time: Optional[datetime.timedelta]
    slice_time: Optional[datetime.timedelta]
    error_code: Optional[int]
    message_code: Optional[str]
    definition_file_e1: Optional[str]
    definition_file_e2: Optional[str]
    parameters_e1: Optional[Dict[str, str]]
    parameters_e2: Optional[Dict[str, str]]

# 24/10/2021
# slerest
# prevoir que l'envoit d'un slice peut se faire sans
# preciser aucun fichier de definition .json de CuraEngine

class SliceIn(DateTimeModelMixin, IDModelMixin):
    definition_file_e1: Optional[str]
    definition_file_e2: Optional[str]
    parameters_e1: Optional[Dict[str, str]]
    parameters_e2: Optional[Dict[str, str]]
