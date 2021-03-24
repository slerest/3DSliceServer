from typing import Optional

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

app = FastAPI()


class Slice(BaseModel):
    gcode: str
    print_time: datetime
    slice_time: datetime

@app.get("/version")
async def version():
    return {"version": "4.8.0"}

@app.post("/slice/")
async def slice(file_id: str):
    return {"file_size": len(file)}
