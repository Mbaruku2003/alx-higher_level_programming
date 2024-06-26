#!/usr/bin/python3
""" Contains the class definition of a State and an instance. """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


themetadata = MetaData()
Base = declarative_base(metadata=themetadata)


class State(Base):
    """class ith attributes of a state."""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
