from core.database import Base
from core.settings import settings
from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    Integer,
    DateTime
)

class BaseModel(Base):
    __abstract__ = True

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    created_at = Column('CREATED_AT', DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column('UPDATED_AT', DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
