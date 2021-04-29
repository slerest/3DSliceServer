import asyncpg
import logging
from core.settings import Settings

class Database:

    def __init__(self):
        self.settings = Settings()
        self.pool = None

    async def connect(self):
        logger = logging.getLogger()
        if not self.pool:
            try:
                self.pool = await asyncpg.create_pool(
                    min_size=1,
                    max_size=20,
                    command_timeout=60,
                    host=self.settings.db_host,
                    port=self.settings.db_port,
                    database=self.settings.db_name,
                    user=self.settings.db_user,
                    password=self.settings.db_password)
            except Exception as e:
                logger.exception(e)
            logger.info("Database pool connectionn opened")
