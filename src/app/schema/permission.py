from schema.generics import DateTimeModelMixin, IDModelMixin
from schema.user import UserOut
from schema.group import GroupOut
from schema.part import PartOut

class PermissionOut(DateTimeModelMixin, IDModelMixin):
    user: UserOut
    group: GroupOut
    part: PartOut
    read: bool = False
    write: bool = False
