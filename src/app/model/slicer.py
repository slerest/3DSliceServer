from pydantic import BaseModel
from model.generics import DateTimeModelMixin, IDModelMixin

class SlicerOut(DateTimeModelMixin, IDModelMixin):
    name: str
    version: str
    host: str
    port: str
