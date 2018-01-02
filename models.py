import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(150), nullable=False)

engine = create_engine('mysql://alfin:admin@localhost/pymysqlalchemy')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
