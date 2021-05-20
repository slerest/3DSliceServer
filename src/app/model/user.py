from model.base import BaseModel
from schema.user import UserOut
from sqlalchemy import (
    Column,
    String,
    Boolean
)

class User(BaseModel):
    __tablename__ = 'USER'

    username = Column('USERNAME', String, nullable=False)
    # TODO voir si il y a un obj Email
    email = Column('EMAIL', String, nullable=False)
    password = Column('PASSWORD', String, nullable=False)
    disable = Column('DISABLE', Boolean, default=True, nullable=False)

    def ToUserOut(self) -> UserOut:
        return UserOut(
            id = self.id,
            username = self.username,
            email = self.email,
            password = self.password,
            disable = self.disable,
            created_at = self.created_at,
            updated_at = self.updated_at
        )
