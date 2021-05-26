from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request
)
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT

from sqlalchemy.orm import Session
import logging
from core.settings import settings
from dependencies.database import get_db
import crud.user as crud_user
from schema.user import UserLogin

logger = logging.getLogger(__name__)
router = APIRouter()

# TODO on doit pouvoir se log avec username OU email
@router.post('/login')
def login(user: UserLogin, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    if not crud_user.login(user, db):
        raise HTTPException(status_code=401,detail="Bad username or password")
    token = Authorize.create_access_token(subject=user.username)
    return {"token": token}
