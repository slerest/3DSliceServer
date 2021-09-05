from pydantic import BaseModel
from schema.generics import DateTimeModelMixin, IDModelMixin

# data from senvol.com

class MaterialOut(DateTimeModelMixin, IDModelMixin):
    supplier: str
    name: str
    general_type: str
    specific_type: str
    am_process: str
    post_process: Optional[bool]
    ultimate_tensible_strength_min: Optional[float]
    ultimate_tensible_strength_max: Optional[float]
    tensile_modulus_min: Optional[float]
    tensile_modulus_max: Optional[float]
    elongation_at_break_min: Optional[float]
    elongation_at_break_max: Optional[float]
    flexural_strength_min: Optional[float]
    flexural_strength_max: Optional[float]
    flexural_modulus_min: Optional[float]
    flexural_modulus_max: Optional[float]
    hardness_shore_scale: Optional[str]
    hardness_min: Optional[float]
    hardness_max: Optional[float]
    hdt_min: Optional[float]
    hdt_max: Optional[float]
    glass_transition_temp_min: Optional[float]
    glass_transition_temp_max: Optional[float]
    part_density: Optional[float]
    flammability: Optional[str]
    usp_class_vi_certified: Optional[bool]
    availability: Optional[bool]
