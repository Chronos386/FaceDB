from sqlalchemy import *
from db_connection.db_models.base import Base


# Соотношение групп и занятий
class SubjectTeacher(Base):
    __tablename__ = 'subject_teacher'
    teacher_id = Column(Integer, ForeignKey('teacher.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id'), primary_key=True)

    def __repr__(self):
        return f'{self.teacher_id} {self.subject_id}'
