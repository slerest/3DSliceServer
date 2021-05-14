from pydantic import BaseModel
from schema.generics import DateTimeModelMixin, IDModelMixin

class SlicerOut(DateTimeModelMixin, IDModelMixin):
    name: str
    version: str
    host: str
    port: str
