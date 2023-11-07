from sqlalchemy import *
from db_connection.db_models.base import Base


# Посещаемость
class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)
    status = Column(Boolean, nullable=False)
    entry_time = Column(Time, nullable=False)
    leave_time = Column(Time, nullable=False)
    class_id = Column(Integer, ForeignKey('class.id'), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=False)

    def __repr__(self):
        return f'{self.id} {self.status} {self.entry_time} {self.leave_time} {self.class_id} {self.person_id}'
