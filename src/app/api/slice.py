import aiosql
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependencies import auth
from model.slice import SliceOut, SliceIn

router = APIRouter(
    prefix="/api/slice-server/v0.1/slice",
    tags=["slices"],
    dependencies=[Depends(auth)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_slices(file_id: str, material: str, response_model=List[SliceOut]):
    conn, cursor = get_conn_cursor() # TODO
    queries = aiosql.from_path(PATH_SQL  + "slice.sql", "psycopg2")
    query = queries.get_all_slices(conn)
    # TODO
    # check in database if slicer is here
    # if not return 400
    # if it exists redirect to the container curaengine 4.8.0 for slicing
    # return object
    return s

@router.get("/{id}")
async def read_slice(file_id: str, material: str, response_model=SliceOut):
    # TODO
    # if it exists redirect to the container curaengine 4.8.0 for slicing
    # return object
    return s

@router.post("/")
async def add_slice(slice: SliceIn, response_model=SliceOut):
    queries = aiosql.from_path(PATH_SQL  + "slice.sql", "psycopg2")
    # TODO
    # check in database if curaengine 4.8.0 have been setup
    # if not return 400
    # if it exists redirect to the container curaengine 4.8.0 for slicing
    # return object
    return s
