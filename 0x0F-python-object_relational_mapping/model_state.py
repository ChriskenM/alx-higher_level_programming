#!/usr/bin/python3
"""
 contains the class definition of a State and an
 instance Base = declarative_base()
"""
from sqlalchemy import column, string, integer, Metadata
from sqlalchemy.ext.declarative import declarative_base


mymetadata = Metadata()
Base = declarative_base(metadata=mymetadata)

class state(Base):
    """
    class with states: id and name attributes
    """

    __tablename__ = 'states'
    id = column(integer, unique=True, nullable=False, primary_key=True)
    name = column(string(128), nullable=False)
