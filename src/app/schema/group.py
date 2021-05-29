from schema.generics import DateTimeModelMixin, IDModelMixin
from pydantic import BaseModel

class GroupOut(DateTimeModelMixin, IDModelMixin):
    name: str

class GroupIn(BaseModel):
    name: str
