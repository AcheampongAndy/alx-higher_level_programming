#!/usr/bin/python3

'''
* Write a script that prints the first State
    * Your script should take 3 arguments:
    mysql username, mysql password and database name
    * You must use the module SQLAlchemy
    * You must import State and Base from model_state -
    from model_state import Base, State
    * Your script should connect to a MySQL
    server running on localhost at port 3306
    * The state you display must be the first in states.id
    * You are not allowed to fetch all states
    from the database before displaying the result
    * The results must be displayed as they are in the example below
    * If the table states is empty, print Nothing followed by a new line
    * Your code should not be executed when imported
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

    first_instance = session.query(State).order_by(State.id).first()

    if first_instance:
        print('{}: {}'.format(first_instance.id, first_instance.name))
    else:
        print('Nothing')
