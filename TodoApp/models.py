from .database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(255) , nullable=False )
    description = Column(String(255) , nullable=False )
    priority = Column(Integer , nullable=False , default=1)
    completed = Column(Boolean , default=False)