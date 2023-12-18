#!/usr/bin/python3
'''
* Write a script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa
* Your script should take 4 arguments: mysql username,
mysql password, database name and state name to search (SQL injection free)
* You must use the module SQLAlchemy
* You must import State and Base from model_state -
from model_state import Base, State
* Your script should connect to a MySQL
server running on localhost at port 3306
* You can assume you have one record with the state name to search
* Results must display the states.id
* If no state has the name you searched for, display Not found
* Your code should not be executed when imported
'''
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username, password, database, state_name = argv[1:5]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           username, password, database))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    found = False
    for state in session.query(State).filter(State.name == state_name):
        print(state.id)
        found = True
        break
    if not found:
        print('Not found')
