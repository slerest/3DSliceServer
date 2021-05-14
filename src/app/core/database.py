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
meta = MetaData(schema="3DSLICESERVER")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

'''
class Database:
    def __init__(self):
        self.user = settings.db_user
        self.password = settings.db_password
        self.host = settings.db_host
        self.port = settings.db_port
        self.database = settings.db_name
        self._cursor = None

        self._connection_pool = None
        self.conn = None

    async def connect(self):
        if not self._connection_pool:
            try:
                self._connection_pool = await asyncpg.create_pool(
                    min_size=1,
                    max_size=10,
                    command_timeout=60,
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                )
            except Exception as e:
                logging.error(e)

    async def fetch_rows(self, query: str):
        if not self._connection_pool:
            await self.connect()
        else:
            self.conn = await self._connection_pool.acquire()
            try:
                result = await self.conn.fetch(query)
                return result
            except Exception as e:
                logging.error(e)
            finally:
                await self._connection_pool.release(self.conn)

    async def close(self):
        await self._connection_pool.close()
'''
