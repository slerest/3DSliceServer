import aiosql
import asyncio
import time
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependencies import auth
from model.slice import SliceOut, SliceIn

router = APIRouter()

@router.get("")
async def read_slices(response_model=List[SliceOut]) -> bool:
    a = await asyncio.sleep(1)
    # TODO
    # check in database if slicer is here
    # if not return 400
    # if it exists redirect to the container curaengine 4.8.0 for slicing
    # return object
    return True
