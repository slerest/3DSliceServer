import logging

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from core.settings import settings
from core.events import startup, shutdown

from api.routes import router as api_router

def get_app() -> FastAPI:
    app = FastAPI(
            title=settings.app_name,
            debug=settings.debug,
            version=settings.version,
            openapi_url=settings.api_prefix + '/openapi.json',
            docs_url=settings.api_prefix + '/docs')
    

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    #app.add_event_handler("startup", startup(app))
    #app.add_event_handler("shutdown", shutdown(app))

    #app.add_exception_handler(HTTPException, http_error_handler)
    #app.add_exception_handler(RequestValidationError, http422_error_handler)

    # TODO test things with API_PREFIX
    app.include_router(api_router, prefix=settings.api_prefix)
    #

    return app

# TODO tester slic3r et voir si on peut avoir des tables generic de material
# TODO return la version de l'api principal et les versions des slicer proposé

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)

app = get_app()

dumb_router = APIRouter()

@dumb_router.get("/ping")
def pong():
    url_list = [{"path": route.path, "name": route.name} for route in app.routes]
    return url_list

app.include_router(dumb_router, prefix=settings.api_prefix)
