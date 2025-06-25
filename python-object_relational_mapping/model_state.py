#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class linked to 'states' table in MySQL database.
    Attributes:
        id (int): auto-incremented, primary key, non-nullable.
        name (str): string with max 128 chars, non-nullable.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
