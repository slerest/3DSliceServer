from fastapi import (
    APIRouter,
    Depends,
    HTTPException.
    Request
)
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from sqlalchemy.orm import Session
import logging
from core.settings import settings
from dependencies.database import get_db
import crud.user as crud_user
from schema.user import UserLogin

logger = logging.getLogger(__name__)
router = APIRouter()

# TODO on doit pouvoir se log avec username OU email
@app.post('/login')
def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    if not crud_user.login(user):
        raise HTTPException(status_code=401,detail="Bad username or password")
    access_token = Authorize.create_access_token(subject=user.username)
    return {"access_token": access_token}
