from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # General info
    app_name: str = Field(..., env='APP_NAME')
    admin_email: str = Field(..., env='ADMIN_EMAIL')
    version: str = Field(..., env='VERSION')
    description: str = Field(..., env='APP_DESCRIPTION')
    debug: bool = Field(..., env='DEBUG')
    api_prefix: str = Field(..., env='API_PREFIX')
    allowed_hosts: str = Field(..., env='ALLOWED_HOSTS')
    # Database
    db_host: str = Field(..., env='DB_HOST')
    db_port: str = Field(..., env='DB_PORT')
    db_name: str = Field(..., env='DB_NAME')
    db_schema: str = Field(..., env='DB_SCHEMA')
    db_user: str = Field(..., env='DB_USER')
    db_password: str = Field(..., env='DB_PASSWORD')
    db_conn: str = Field(..., env='DB_CONN')
    db_schema: str = Field(..., env='DB_SCHEMA')
    # Auth
    basic: bool = Field(..., env='AUTH_BASIC')
    bearer: bool = Field(..., env='AUTH_BEARER')
    api_key: bool = Field(..., env='AUTH_API_KEY')
    # Path
    path_queries: str = Field(..., env='PATH_QUERIES')

settings = Settings()
