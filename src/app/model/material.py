from pydantic import BaseModel
from model.generics import DateTimeModelMixin, IDModelMixin

# data from senvol.com

class MaterialOut(DateTimeModelMixin, IDModelMixin):
    supplier: str
    name: str
    general_type: str
    specific_type: str
    am_process: str
    post_process: bool
    ultimate_tensible_strength_min: float
    ultimate_tensible_strength_max: float
    tensile_modulus_min: float
    tensile_modulus_max: float
    elongation_at_break_min: float
    elongation_at_break_max: float
    flexural_strength_min: float
    flexural_strength_max: float
    flexural_modulus_min: float
    flexural_modulus_max: float
    hardness_shore_scale: str
    hardness_min: float
    hardness_max: float
    hdt_min: float
    hdt_max: float
    glass_transition_temp_min: float
    glass_transition_temp_max: float
    part_density: float
    flammability: str
    usp_class_vi_certified: bool
    availability: bool
