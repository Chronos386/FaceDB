from sqlalchemy import *
from db_connection.db_models.base import Base


# Студенческая группа
class StudentsGroup(Base):
    __tablename__ = 'students_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)

    def __repr__(self):
        return f'{self.id} {self.name}'
