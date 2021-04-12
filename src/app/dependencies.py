from fastapi import Header, HTTPException

# 3 modes d'authentification
# authentication: token ou jwt ou basic
# Authorization: Basic user:password (convert base64)
# Authorization: Bearer <jwt-token>
# Authorization: Apikey <token generated server side>

# TODO se renseigner sur OAuth 2.0

accepted_auth_method = [
    'Basic',
    'Bearer',
    'Apikey'
]
async def get_auth(authorization: str = Header(...)):
    auth_method = authorization.split()[0]
    if auth_method not in accepted_auth_method:
        return False
    return True

async def auth(authorization: str = Header(...), admin=False):
    return True
