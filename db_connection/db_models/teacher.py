from sqlalchemy import *
from db_connection.db_models.base import Base


# Преподаватель
class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    work_experience = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

    def __repr__(self):
        return f'{self.id} {self.work_experience} {self.person_id}'
