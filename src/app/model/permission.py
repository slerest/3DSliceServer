from model.base import BaseModel
from model.user import User
from model.group import Group
from model.part import Part
from sqlalchemy.orm import Session
from pydantic import EmailStr
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
    part_id = Column('PART_ID', Integer, ForeignKey("PART.ID"))
    read = Column('READ', Boolean, default=False, nullable=False)
    write = Column('WRITE', Boolean, default=False, nullable=False)
    user = relationship("User", back_populates="user_permission")
    group = relationship("Group", back_populates="group_permission")
    part = relationship("Part", back_populates="part_permission")

    def ToPermissionOut(self, db: Session) -> PermissionOut:
        g = db.query(Group).filter(Group.id == self.group_id).first()
        u = db.query(User).filter(User.id == self.user_id).first()
        p = db.query(Part).filter(Part.id == self.part_id).first()
        return PermissionOut(
            id = self.id,
            user = u.ToUserOut(),
            group = g.ToGroupOut(),
            part = p.ToPartOut(),
            read = self.read,
            write = self.write,
            created_at = self.created_at,
            updated_at = self.updated_at
        )
