from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    DateTime, 
    Boolean
)

from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key = True)
    username = Column(String(100), default = 'Example', nullable = False, unique = True)
    email = Column(String(100), default = 'example@email.com', nullable = False, unique = True)
    created_at = Column(DateTime(), default = datetime.now(), nullable = True)
    updated_at = Column(DateTime(), default = datetime.now(), nullable = True)
    is_active = Column(Boolean(), default=True, nullable = True)




