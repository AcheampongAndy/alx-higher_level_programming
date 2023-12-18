#!/usr/bin/python3
'''
* Write a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
* Your script should take 3 arguments: mysql
username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state -
from model_state import Base, State
* Your script should connect to a MySQL
server running on localhost at port 3306
* Print the new states.id after creation
* Your code should not be executed when imported
'''
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username, password, database = argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           username, password, database))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    states = session.query(State).filter(State.name == 'Louisiana')
    for state in states:
        print(state.id)
        break

    session.close()
