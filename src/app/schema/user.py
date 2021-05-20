from schema.generics import DateTimeModelMixin, IDModelMixin
from pydantic import BaseModel
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class UserOut(DateTimeModelMixin, IDModelMixin):
    username: str
    email: Optional[str] = None
    disable: bool = True

class UserLogin(BaseModel):
    username: str
    password: str
