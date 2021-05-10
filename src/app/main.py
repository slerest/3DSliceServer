import logging

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from core.settings import settings
from core.db_session import db

from api.routes import router as api_router



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

app.include_router(api_router, prefix=settings.api_prefix)

# TODO tester slic3r et voir si on peut avoir des tables generic de material
# TODO return la version de l'api principal et les versions des slicer proposé

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def startup():
    await db.close()

dumb_router = APIRouter()

# DEBUGGING
@dumb_router.get("/ping")
def pong():
    url_list = [{"path": route.path, "name": route.name} for route in app.routes]
    return url_list

app.include_router(dumb_router, prefix=settings.api_prefix)
