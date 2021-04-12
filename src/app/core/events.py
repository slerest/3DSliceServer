import logging
from core.database import Database, Settings

async def startup():
    # Param logger
    # TODO opt for logging into file
    FORMAT = '%(asctime)-15s %(levelname)s: %(message)s'
    DATEFMT = '%d/%m/%Y %H:%M:%S'
    FILENAME = 'slice_new_quotes.log'
    logging.basicConfig(format=FORMAT,
            level=logging.INFO,
            datefmt=DATEFMT)
    # Settings
    app.state.settings = Settings()
    # Connect database
    # We can reach database pool  with app.state.db.pool
    database = Database()
    await database.connect()
    app.state.db = database
    logging.info("Server Startup")

async def shutdown():
    logger = logging.getLogger()
    if not app.state.db:
        await app.state.db.close()
    logging.info("Server Shutdown")
