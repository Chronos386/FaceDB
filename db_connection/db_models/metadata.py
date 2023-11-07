from sqlalchemy import *
from db_connection.db_models.base import Base


# Мета данные
class Metadata(Base):
    __tablename__ = 'metadata'
    id = Column(Integer, primary_key=True)
    path = Column(String(500), nullable=False)
    add_date = Column(TIMESTAMP(timezone=True), nullable=False)

    def __repr__(self):
        return f'{self.id} {self.path} {self.add_date}'
