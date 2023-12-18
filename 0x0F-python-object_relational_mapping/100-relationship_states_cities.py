#!/usr/bin/python3
'''
Write a script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa:
(100-relationship_states_cities.py)

Your script should take 3 arguments: mysql
username, mysql password and database name
You must use the module SQLAlchemy
Your script should connect to a MySQL server
running on localhost at port 3306
You must use the cities relationship for all State objects
Your code should not be executed when imported
'''
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    username, password, database = argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           username, password, database))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()
    session.close()
