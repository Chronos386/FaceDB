from sqlalchemy import *
from db_connection.db_models.base import Base


# Соотношение преподавателя и предмета
class ClassTeacher(Base):
    __tablename__ = 'class_teacher'
    teacher_id = Column(Integer, ForeignKey('teacher.id'), primary_key=True)
    class_id = Column(Integer, ForeignKey('class.id'), primary_key=True)

    def __repr__(self):
        return f'{self.teacher_id} {self.class_id}'
