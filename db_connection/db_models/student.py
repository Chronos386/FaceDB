from sqlalchemy import *
from db_connection.db_models.base import Base


# Студент
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    group_id = Column(Integer, ForeignKey('students_group.id'))

    def __repr__(self):
        return f'{self.id} {self.person_id} {self.group_id}'
