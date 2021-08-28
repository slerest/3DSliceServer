from schema.generics import DateTimeModelMixin, IDModelMixin
from schema.user import UserOut
from schema.group import GroupOut
from schema.part import PartOut
from typing import Optional

class PermissionPartOut(DateTimeModelMixin, IDModelMixin):
    user: Optional[UserOut]
    group: Optional[GroupOut]
    part: PartOut
    read: bool = False
    write: bool = False
    delete: bool = False

class RightsPart():

    def __init__(self, read=True, write=True, delete=True):
        self.read = read
        self.write = write
        self.delete = delete
