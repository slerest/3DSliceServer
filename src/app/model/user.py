from model.base import BaseModel
from pydantic import EmailStr
from schema.user import UserOut
from sqlalchemy import (
    Column,
    String,
    Boolean
)
from sqlalchemy.orm import relationship

class User(BaseModel):
    __tablename__ = 'USER'

    username = Column('USERNAME', String, nullable=False, unique=True)
    email = Column('EMAIL', String, nullable=False, unique=True)
    password = Column('PASSWORD', String, nullable=False)
    disable = Column('DISABLE', Boolean, default=True, nullable=False)
    superuser = Column('SUPERUSER', Boolean, default=False, nullable=False)
    user_group = relationship("UserGroup", back_populates="user")
    user_permission = relationship("Permission", back_populates="user")
    user_permission_part = relationship("PermissionPart", back_populates="user")

    def ToUserOut(self) -> UserOut:
        return UserOut(
            id = self.id,
            username = self.username,
            email = EmailStr(self.email),
            password = self.password,
            disable = self.disable,
            superuser = self.superuser,
            created_at = self.created_at,
            updated_at = self.updated_at
        )
