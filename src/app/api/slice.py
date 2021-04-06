import aiosql
import psycopg2
from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import auth

router = APIRouter(
    prefix="/slices",
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
async def add_slice(slice: SlicIn, response_model=SliceOut):
    queries = aiosql.from_path(PATH_SQL  + "slice.sql", "psycopg2")
    # TODO
    # check in database if curaengine 4.8.0 have been setup
    # if not return 400
    # if it exists redirect to the container curaengine 4.8.0 for slicing
    # return object
    return s
