from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    # General info
    app_name: str = "3DSliceServer"
    admin_email: str = "sebastienlerest22@gmail.com"
    version: str = "0.0.0"
    # Database
    db_url: str
    db_port: str
    db_name: str
    db_schema: str
    db_user: str
    db_password: str
    # Auth
    basic: bool = True
    bearer: bool = True
    api_key: bool = True

    def __init__(self):
        # Database
        self.db_url = os.getenv('DB_URL', 'db')
        self.db_port = os.getenv('DB_PORT', '5432')
        self.db_name = os.getenv('DB_NAME', '3DSLICESERVER')
        self.db_schema = os.getenv('DB_SCHEMA', 'public')
        self.db_user = os.getenv('DB_USER', 'postgres')
        self.db_password = os.getenv('DB_PASSWORD', 'password')
        # Auth
        self.basic = True is os.getenv('AUTH_BASIC', 'TRUE') == 'TRUE' else False
        self.bearer = True is os.getenv('AUTH_BEARER', 'TRUE') == 'TRUE' else False
        self.api_key = True is os.getenv('AUTH_API_KEY', 'TRUE') == 'TRUE' else False
