from schema.generics import DateTimeModelMixin, IDModelMixin
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserOut(DateTimeModelMixin, IDModelMixin):
    username: str
    email: EmailStr
    disable: bool = True
    superuser: bool = False
    create: bool = True

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    disable: Optional[bool]
    superuser: Optional[bool]
    create: Optional[bool]

class UserLogin(BaseModel):
    username: str
    password: str
