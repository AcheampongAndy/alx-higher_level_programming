#!/usr/bin/python3
'''
Write a script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa

Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server
running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported
'''

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username, password, database = argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    instances = session.query(State).order_by(State.id).filter(
            State.name.contains('a'))

    for state in instances:
        print('{0}: {1}'.format(state.id, state.name))
