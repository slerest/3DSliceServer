from schema.generics import DateTimeModelMixin, IDModelMixin
from schema.user import UserOut
from schema.group import GroupOut
from typing import Optional

class PermissionOut(DateTimeModelMixin, IDModelMixin):
    user: Optional[UserOut]
    group: Optional[GroupOut]
    create_part: bool = True
    create_user: bool = False
    modify_user: bool = False
    supress_user: bool = False
    create_group: bool = False
    modify_group: bool = False
    supress_group: bool = False
