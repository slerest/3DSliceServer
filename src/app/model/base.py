from core.database import Base
from core.settings import settings
from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    Integer,
    DateTime
)
from sqlalchemy.schema import Identity

class BaseModel(Base):
    __abstract__ = True


    id = Column('ID', Integer, autoincrement=True, primary_key=True)
    created_at = Column('CREATED_AT', DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column('UPDATED_AT', DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
