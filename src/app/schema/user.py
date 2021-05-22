from schema.generics import DateTimeModelMixin, IDModelMixin
from pydantic import BaseModel, EmailStr
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class UserOut(DateTimeModelMixin, IDModelMixin):
    username: str
    email: EmailStr
    disable: bool = True

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str
