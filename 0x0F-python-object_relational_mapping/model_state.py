#!/usr/bin/python3

'''
* Write a python file that contains the class definition
of a State and an instance Base = declarative_base():

    * State class:
        * inherits from Base Tips
        * links to the MySQL table states
        * class attribute id that represents a column of an
        auto-generated, unique integer, can’t be null and is a primary key
        * class attribute name that represents a column of a string
        with maximum 128 characters and can’t be null
    * You must use the module SQLAlchemy
    * Your script should connect to a MySQL server
    running on localhost at port 3306
'''

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
