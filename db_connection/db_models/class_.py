from sqlalchemy import *
from db_connection.db_models.base import Base


# Занятие
class Class(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)
    date_class = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    audience = Column(String(50), nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)

    def __repr__(self):
        return f'{self.id} {self.date_class} {self.start_time} {self.end_time} {self.audience} {self.subject_id}'
