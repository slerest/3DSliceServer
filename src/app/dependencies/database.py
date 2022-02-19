from core.database import SessionLocal
from core.settings import settings
import logging

logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    conn = db.connection()
    conn.execute(f"set search_path=\"{settings.db_schema}\", public")
    try:
        yield db
    finally:
        db.close()
