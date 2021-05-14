from pydantic import BaseModel

# data from senvol.com

class MachineOut(BaseModel):
    id: int
    manufacturer: str
    model: str
    mode: str
    power: int
    am_process: str
    general_material_type: str
    specific_material_type: str
    x: float
    y: float
    z: float
    price: str
    availability: bool
