

# TODO voir comment on peut recuperer app

@app.post("/slice")
async def post_slice(slice: SlicIn, response_model=SliceOut):
    # TODO
    # check in database if curaengine 4.8.0 have been setup
    # if not return 400
    # if it exists redirect to the container curaengine 4.8.0 for slicing
    # return object
    return s

@app.get("/slice")
async def get_slices(file_id: str, material: str, response_model=List[SliceOut]):
    # TODO
    # check in database if slicer is here
    # if not return 400
    # if it exists redirect to the container curaengine 4.8.0 for slicing
    # return object
    return s

@app.get("/slice/{id}")
async def get_slice(file_id: str, material: str, response_model=SliceOut):
    # TODO
    # if it exists redirect to the container curaengine 4.8.0 for slicing
    # return object
    return s

@app.post("/slice/{id}/status")
async def post_slice():
    # Il y aura qq chose de tricky a faire ici
    # on ne peut pas faire un appell a la bae de donnée a chaque
    # fois que l'on appel status, c'est un endpoint ou ca va bombarder sec

    return {'status', s.status}
