from model.base import BaseModel
from model.user import User
from model.group import Group
from model.part import Part
from sqlalchemy.orm import Session
from schema.permission_part import PermissionPartOut
from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    ForeignKey
)
from sqlalchemy.orm import relationship

class PermissionPart(BaseModel):
    __tablename__ = 'PERMISSION_PART'

    user_id = Column('USER_ID', Integer, ForeignKey("USER.ID"), nullable=True)
    group_id = Column('GROUP_ID', Integer, ForeignKey("GROUP.ID"), nullable=True)
    part_id = Column('PART_ID', Integer, ForeignKey("PART.ID"))
    read = Column('READ', Boolean, default=False, nullable=False)
    write = Column('WRITE', Boolean, default=False, nullable=False)
    delete = Column('DELETE', Boolean, default=False, nullable=False)
    user = relationship("User", back_populates="user_permission_part")
    group = relationship("Group", back_populates="group_permission_part")
    part = relationship("Part", back_populates="part_permission_part")

    def ToPermissionPartOut(self, db: Session) -> PermissionPartOut:
        g = db.query(Group).filter(Group.id == self.group_id).first()
        if g is not None:
            g = g.ToGroupOut()
        u = db.query(User).filter(User.id == self.user_id).first()
        if u is not None:
            u = u.ToUserOut()
        p = db.query(Part).filter(Part.id == self.part_id).first()
        return PermissionPartOut(
            id = self.id,
            user = u,
            group = g,
            part = p.ToPartOut(),
            read = self.read,
            write = self.write,
            delete = self.delete,
            created_at = self.created_at,
            updated_at = self.updated_at
        )
