#!/usr/bin/python3
'''
* Write a script that deletes all State objects with a
name containing the letter a from the database hbtn_0e_6_usa

* Your script should take 3 arguments:
mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state -
from model_state import Base, State
* Your script should connect to a MySQL
server running on localhost at port 3306
* Your code should not be executed when imported
'''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    username, password, database = argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           username, password, database))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)

    session.commit()

    session.close()
