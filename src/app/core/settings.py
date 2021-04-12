from pydantic import BaseSettings

class Settings(BaseSettings):
    # General info
    app_name: str = "3DSliceServer"
    admin_email: str
    version: str = "0.0"
    api_prefix: str
    # Database
    db_host: str
    db_port: str
    db_name: str
    db_schema: str
    db_user: str
    db_password: str
    # Auth
    basic: bool = True
    bearer: bool = True
    api_key: bool = True
