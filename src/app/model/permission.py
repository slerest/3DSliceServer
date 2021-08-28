from model.base import BaseModel
from model.user import User
from model.group import Group
from sqlalchemy.orm import Session
from schema.permission import PermissionOut
from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    ForeignKey
)
from sqlalchemy.orm import relationship

class Permission(BaseModel):
    __tablename__ = 'PERMISSION'

    user_id = Column('USER_ID', Integer, ForeignKey("USER.ID"), nullable=True)
    group_id = Column('GROUP_ID', Integer, ForeignKey("GROUP.ID"), nullable=True)
    create_part = Column('CREATE_PART', Boolean, default=True, nullable=False)
    create_user = Column('CREATE_USER', Boolean, default=False, nullable=False)
    modify_user = Column('MODIFY_USER', Boolean, default=False, nullable=False)
    supress_user = Column('SUPRESS_USER', Boolean, default=False, nullable=False)
    create_group = Column('CREATE_GROUP', Boolean, default=False, nullable=False)
    modify_group = Column('MODIFY_GROUP', Boolean, default=False, nullable=False)
    supress_group = Column('SUPRESS_GROUP', Boolean, default=False, nullable=False)
    user = relationship("User", back_populates="user_permission")
    group = relationship("Group", back_populates="group_permission")

    def ToPermissionOut(self, db: Session) -> PermissionOut:
        g = db.query(Group).filter(Group.id == self.group_id).first()
        if g is not None:
            g = g.ToGroupOut()
        u = db.query(User).filter(User.id == self.user_id).first()
        if u is not None:
            u = u.ToUserOut()
        return PermissionOut(
            id = self.id,
            user = u,
            group = g,
            create_part = self.create_part,
            create_user = self.create_user,
            modify_user = self.modify_user,
            supress_user = self.supress_user,
            create_group = self.create_group,
            modify_group = self.modify_group,
            supress_group = self.supress_group,
            created_at = self.created_at,
            updated_at = self.updated_at
        )
