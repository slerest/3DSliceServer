from typing import Optional

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

app = FastAPI()

# TODO tester slic3r et voir si on peut avoir des tables generic de material

class Slice(BaseModel):
    id: int
    gcode: str
    print_time: datetime
    slice_time: datetime
    material: int
    part: int
    status: int
    technologie: str
    color_rgb: str

class Material(BaseModel):
    id: int
    name: str
    description_file: str

# TODO return la version de l'api principal et les versions des slicer proposé
@app.get("/version")
async def version():
    return {"version": "0.1"}

@app.post("/curaengine/4.8.0/slice")
async def slice_curaengine_4_8_0(file_id: str, material: str):
    # TODO
    # check in database if curaengine 4.8.0 have been setup
    # if not return 400
    # if it exists redirect to the container curaengine 4.8.0 for slicing
    # return object
    return {"file_size": len(file)}
