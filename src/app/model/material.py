from model.base import BaseModel
from schema.material import MaterialOut
from sqlalchemy import (
    Column,
    Float,
    String,
    Boolean,
)

class Material(BaseModel):
    __tablename__ = 'MATERIAL'

    supplier = Column('SUPPLIER', String, nullable=False)
    name = Column('NAME', String, nullable=False)
    general_type = Column('GENERAL_TYPE', String, nullable=False)
    specific_type = Column('SPECIFIC_TYPE', String, nullable=False)
    am_process = Column('AM_PROCESS', String, nullable=False)
    post_process = Column('POST_PROCESS', Boolean, default=None, nullable=True)
    ultimate_tensible_strength_min = Column('ULTIMATE_TENSILE_STRENGTH_MIN', Float, default=None, nullable=True)
    ultimate_tensible_strength_max = Column('ULTIMATE_TENSILE_STRENGTH_MAX', Float, default=None, nullable=True)
    tensile_modulus_min = Column('TENSILE_MODULUS_MIN', Float, default=None, nullable=True)
    tensile_modulus_max = Column('TENSILE_MODULUS_MAX', Float, default=None, nullable=True)
    elongation_at_break_min = Column('ELONGATION_AT_BREAK_MIN', Float, default=None, nullable=True)
    elongation_at_break_max = Column('ELONGATION_AT_BREAK_MAX', Float, default=None, nullable=True)
    flexural_strength_min = Column('FLEXURAL_STRENGTH_MIN', Float, default=None, nullable=True)
    flexural_strength_max = Column('FLEXURAL_STRENGTH_MAX', Float, default=None, nullable=True)
    flexural_modulus_min = Column('FLEXURAL_MODULUS_MIN', Float, default=None, nullable=True)
    flexural_modulus_max = Column('FLEXURAL_MODULUS_MAX', Float, default=None, nullable=True)
    hardness_shore_scale = Column('HARDNESS_SHORE_SCALE', String, default=None, nullable=True)
    hardness_min = Column('HARDNESS_MIN', Float, default=None, nullable=True)
    hardness_max = Column('HARDNESS_MAX', Float, default=None, nullable=True)
    hdt_min = Column('HDT_MIN', Float, default=None, nullable=True)
    hdt_max = Column('HDT_MAX', Float, default=None, nullable=True)
    glass_transition_temp_min = Column('GLASS_TRANSITION_TEMP_MIN', Float, default=None, nullable=True)
    glass_transition_temp_max = Column('GLASS_TRANSITION_TEMP_MAX', Float, default=None, nullable=True)
    part_density = Column('PART_DENSITY', Float, default=None, nullable=True)
    flammability = Column('FLAMMABILITY', String, default=None, nullable=True)
    usp_class_vi_certified = Column('USP_CLASS_VI_CERTIFIED', Boolean, default=None, nullable=True)
    availability = Column('AVAILABILITY', Boolean, default=None, nullable=True)

    def ToMaterialOut(self) -> MaterialOut:
        return MaterialOut(
            id = self.id,
            supplier = self.supplier,
            name = self.name,
            general_type = self.general_type,
            specific_type = self.specific_type,
            am_process = self.am_process,
            post_process = self.post_process,
            ultimate_tensible_strength_min = self.ultimate_tensible_strength_min,
            ultimate_tensible_strength_max = self.ultimate_tensible_strength_max,
            tensile_modulus_min = self.tensile_modulus_min,
            tensile_modulus_max = self.tensile_modulus_max,
            elongation_at_break_min = self.elongation_at_break_min,
            elongation_at_break_max = self.elongation_at_break_max,
            flexural_strength_min = self.flexural_strength_min,
            flexural_strength_max = self.flexural_strength_max,
            flexural_modulus_min = self.flexural_modulus_min,
            flexural_modulus_max = self.flexural_modulus_max,
            hardness_shore_scale = self.hardness_shore_scale,
            hardness_min = self.hardness_min,
            hardness_max = self.hardness_max,
            hdt_min = self.hdt_min,
            hdt_max = self.hdt_max,
            glass_transition_temp_min = self.glass_transition_temp_min,
            glass_transition_temp_max = self.glass_transition_temp_max,
            part_density = self.part_density,
            flammability = self.flammability,
            usp_class_vi_certified = self.usp_class_vi_certified,
            availability = self.availability,
            created_at = self.created_at,
            updated_at = self.updated_at
        )
