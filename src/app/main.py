import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from core.settings import settings

from api.routes import router as api_router

# TODO DEBUG et PROD config

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

# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return settings

#def authjwt_exception_handler(request: Request, exc: AuthJWTException):

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

app.include_router(api_router, prefix=settings.api_prefix)

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)
