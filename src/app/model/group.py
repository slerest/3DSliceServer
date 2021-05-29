from model.base import BaseModel
from schema.group import GroupOut
from sqlalchemy import (
    Column,
    String
)
from sqlalchemy.orm import relationship

class Group(BaseModel):
    __tablename__ = 'GROUP'

    name = Column('NAME', String, nullable=False, unique=True)
    group_user = relationship("UserGroup", back_populates="group")

    def ToGroupOut(self) -> GroupOut:
        return GroupOut(
            id = self.id,
            name = self.name,
            created_at = self.created_at,
            updated_at = self.updated_at
        )

    def __str__(self):
        return f'id {self.id} name {self.name} created_at {self.created_at} updated_at {self.updated_at}'
