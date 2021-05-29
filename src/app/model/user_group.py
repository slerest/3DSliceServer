from model.base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class UserGroup(BaseModel):
    __tablename__ = 'USER_GROUP'

    user_id = Column('USER_ID', Integer, ForeignKey('USER.ID'), nullable=False)
    group_id = Column('GROUP_ID', Integer, ForeignKey('GROUP.ID'), nullable=False)
    user = relationship("User", back_populates="user_group")
    group = relationship("Group", back_populates='group_user')
