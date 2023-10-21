#!/usr/bin/python3
"""
Defines the class State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """inherits from Base with id and name as attributes"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
