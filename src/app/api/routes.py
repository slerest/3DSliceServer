from fastapi import APIRouter
from api import slice

router = APIRouter()
router.include_router(slice.router, tags=["slice"], prefix="/slices")
#router.include_router(material.router, tags=["material"], prefix="/materials")
#router.include_router(machine.router, tags=["machine"], prefix="/machines")
