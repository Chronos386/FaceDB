from sqlalchemy import *
from db_connection.db_models.base import Base


# Человек
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)
    meta_id = Column(Integer, ForeignKey('metadata.id'))

    def __repr__(self):
        return f'{self.id} {self.name} {self.meta_id}'
