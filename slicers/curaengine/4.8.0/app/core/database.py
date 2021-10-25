'''
import asyncpg
import asyncpg
'''
from core.settings import settings
import logging


from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}".format(
        user=settings.db_user,
        password=settings.db_password,
        host=settings.db_host,
        port=settings.db_port,
        db_name=settings.db_name
)
'''

logger = logging.getLogger(__name__)

SQLALCHEMY_DATABASE_URL = settings.db_conn

engine = create_engine(SQLALCHEMY_DATABASE_URL)
meta = MetaData(schema=settings.db_schema)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
