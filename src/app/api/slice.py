import aiosql
import asyncio
import time
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependencies import auth
from model.slice import SliceOut
from model.material import MaterialOut
from model.part import PartOut
from model.slicer import SlicerOut

router = APIRouter()

@router.get("", response_model=List[SliceOut], name="slices:listslices")
async def read_slices() -> List[SliceOut]:
    a = await asyncio.sleep(1)
    # TODO
    # check in database if slicer is here
    # if not return 400
    # if it exists redirect to the container curaengine 4.8.0 for slicing
    # return object
    m = MaterialOut(
        supplier = "supplier",
        name = "name",
        general_type = "general_type",
        specific_type = "specific_type",
        am_process = "am_process",
        post_process = False,
        ultimate_tensible_strength_min = 0.0,
        ultimate_tensible_strength_max = 0.0,
        tensile_modulus_min = 0.0,
        tensile_modulus_max = 0.0,
        elongation_at_break_min = 0.0,
        elongation_at_break_max = 0.0,
        flexural_strength_min = 0.0,
        flexural_strength_max = 0.0,
        flexural_modulus_min = 0.0,
        flexural_modulus_max = 0.0,
        hardness_shore_scale ="hardness_shore_scale",
        hardness_min = 0.0,
        hardness_max = 0.0,
        hdt_min = 0.0,
        hdt_max = 0.0,
        glass_transition_temp_min = 0.0,
        glass_transition_temp_max = 0.0,
        part_density = 0.0,
        flammability = "flammability",
        usp_class_vi_certified = False,
        availability = False
    )

    p = PartOut(
        name = "name",
        unit = "mm",
        volume = 0.0,
        volume_support = 0.0,
        file = None,
        format = ".stl",
        x = 0.0,
        y = 0.0,
        z = 0.0
    )
    one_slicer = SlicerOut(
        name = "name",
        version = "0.0",
        host = "slicer.com",
        port = "80",
    )
    one_slice = SliceOut(
        gcode = "lol+gcode",
        print_time = None,
        slice_time = None,
        material = m,
        part = p,
        status = "sliced",
        slicer = one_slicer
    )
    return [one_slice]
