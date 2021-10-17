from model.base import BaseModel
from schema.slicer import SlicerOut
from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

class Slicer(BaseModel):
    __tablename__ = 'SLICER'

    name = Column('NAME', String, nullable=False)
    version = Column('VERSION', String, nullable=False)
    host = Column('HOST', String, default=None, nullable=True)
    port = Column('PORT', String, default=None, nullable=True)

    def ToSlicerOut(self) -> SlicerOut:
        return SlicerOut(
            id = self.id,
            name = self.name,
            version = self.version,
            host = self.host,
            port = self.port,
            created_at = self.created_at,
            updated_at = self.updated_at
        )
