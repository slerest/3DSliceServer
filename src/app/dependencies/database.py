from core.database import SessionLocal
from core.settings import settings
import logging

logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    conn = db.connection()
    conn.execute('set search_path="{}", public'.format("3DSLICESERVER"))
    try:
        yield db
    finally:
        db.close()
