from typing import Optional

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from .api import slice


# TODO tester slic3r et voir si on peut avoir des tables generic de material

# TODO return la version de l'api principal et les versions des slicer proposé

def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    #application.include_router(api_router, prefix=API_PREFIX)

    app.include_router(slice.router)

    return application

app = get_application()

@app.get("/version")
async def version():
    return {"version": "0.1"}

