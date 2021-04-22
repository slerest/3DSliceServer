from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from core.settings import Settings
from core.events import startup, shutdown

from api.routes import router as api_router

def get_app() -> FastAPI:
    s = Settings()
    app = FastAPI(
            title=s.app_name,
            debug=s.debug,
            version=s.version,
            openapi_url=s.api_prefix + '/openapi.json',
            docs_url=s.api_prefix + '/docs')
    

    app.add_middleware(
        CORSMiddleware,
        allow_origins=s.allowed_hosts or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    #app.add_event_handler("startup", startup(app))
    #app.add_event_handler("shutdown", shutdown(app))

    #app.add_exception_handler(HTTPException, http_error_handler)
    #app.add_exception_handler(RequestValidationError, http422_error_handler)

    # TODO test things with API_PREFIX
    app.include_router(api_router, prefix=s.api_prefix)
    #

    return app

# TODO tester slic3r et voir si on peut avoir des tables generic de material
# TODO return la version de l'api principal et les versions des slicer proposé

app = get_app()

dumb_router = APIRouter()

@dumb_router.get("/ping")
def pong():
    url_list = [{"path": route.path, "name": route.name} for route in app.routes]
    return url_list

app.include_router(dumb_router, prefix=Settings().api_prefix)
