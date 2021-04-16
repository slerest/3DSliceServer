from fastapi import FastAPI
from typing import Callable

import logging

from core.database import Database, Settings

def startup(app: FastAPI) -> Callable:
    # aucune idée de ce que je fais
    async def start_app() -> None:
    # TODO
    # ici il faut au moins un await
    # on va le faire pour lancer un await conn = database() ou un truc dans le genre
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
    return start

async def shutdown(app: FastAPI):
    async def stop_app() -> None:
        logger = logging.getLogger()
        if not app.state.db:
            await app.state.db.close()
        logging.info("Server Shutdown")
    return stop_app
