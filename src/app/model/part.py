#from core.database import Base
from core.settings import settings
from model.base import BaseModel
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    LargeBinary
)

class Part(BaseModel):
    __tablename__ = 'PART'

    name = Column('NAME', String, nullable=False)
    unit = Column('UNIT', String, nullable=False)
    file = Column('FILE', LargeBinary, default=None)
    format = Column('FORMAT', String, nullable=False)
    volume = Column('VOLUME', Float, default=None)
    volume_support = Column('VOLUME_SUPPORT', Float, default=None)
    x = Column('X', Float, default=None)
    y = Column('Y', Float, default=None)
    z = Column('Z', Float, default=None)

    def __init__(self, name, unit, format):
        self.name = name
        self.unit = unit
        self.format = format

    def __str__(self):
        s = '''
        id={id},
        name={name},
        unit={unit},
        file={file},
        format={format},
        volume={volume},
        volume_support={volume_support},
        x =={x},
        y =={y},
        z =={z}'''.format(
            id=self.id,
            name=self.name,
            unit=self.unit,
            file=self.file,
            format=self.format,
            volume=self.volume,
            volume_support=self.volume_support,
            x=self.x,
            y=self.y,
            z=self.z)
        return s
