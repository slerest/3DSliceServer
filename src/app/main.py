from fastapi import FastAPI

from core.settings import Settings
from core.events import startup, shutdown

from api.routes import router

def get_app() -> FastAPI:
    app = FastAPI(title=APP_NAME, debug=DEBUG, version=VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", startup(application))
    app.add_event_handler("shutdown", shutdown(application))

    app.add_exception_handler(HTTPException, http_error_handler)
    app.add_exception_handler(RequestValidationError, http422_error_handler)

    # TODO test things with API_PREFIX
    app.include_router(router, prefix=API_PREFIX)

    return app

# TODO tester slic3r et voir si on peut avoir des tables generic de material
# TODO return la version de l'api principal et les versions des slicer proposé

app = get_app()
