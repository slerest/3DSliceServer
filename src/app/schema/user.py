from schema.generics import DateTimeModelMixin, IDModelMixin
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserOut(DateTimeModelMixin, IDModelMixin):
    username: str
    email: EmailStr
    disable: bool = True # TODO pour default a True ? pk j'ai fais ca ?
    superuser: bool = False # TODO pour default a False ? pk j'ai fais ca ?

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    disable: Optional[bool]
    superuser: Optional[bool]

class UserLogin(BaseModel):
    username: str
    password: str
