from fastapi import APIRouter, File, UploadFile, HTTPException
from subprocess import Popen, PIPE
from asyncio import create_subprocess_shell, subprocess
from model.slice import SliceOut, SliceIn
from pathlib import Path
from typing import List, Dict, Any

router = APIRouter()

# TODO dict of additional parameters
@router.post("/", response_model=SliceOut, name="slices:createslices")
async def create_slice(slice_in: SliceIn) -> SliceOut:
    print("OK")
    # check if definition file is present
    if Path(settings.path_definition_files, + slice_in.definition_file):
        raise HTTPException(status_code=400, detail="Definition file not found")

    # TODO Create stl file from Bytes posted
    print(dir(stl_file))

    # TODO on va changer le output.gcode pour avoir un nom unique
    path_stl_file = '/stl_file.stl'
    path_output_gcode = '/output.gcode'
    cmd = [settings.path_curaengine, 'slice', '-v', '-j',
            settings.path_definition_files + definition_file,
            '-o', path_output_gcode, '-l', path_stl_file]
    process = await create_subprocess_shell(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    print("Started: %s, pid=%s" % (args, process.pid), flush=True)
