from sqlalchemy import *
from db_connection.db_models.base import Base


# Соотношение групп и занятий
class ClassGroup(Base):
    __tablename__ = 'class_group'
    group_id = Column(Integer, ForeignKey('students_group.id'), primary_key=True)
    class_id = Column(Integer, ForeignKey('class.id'), primary_key=True)

    def __repr__(self):
        return f'{self.group_id} {self.class_id}'
