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
    group_permission = relationship("Permission", back_populates="group")
    group_permission_part = relationship("PermissionPart", back_populates="group")

    def ToGroupOut(self) -> GroupOut:
        return GroupOut(
            id = self.id,
            name = self.name,
            created_at = self.created_at,
            updated_at = self.updated_at
        )
