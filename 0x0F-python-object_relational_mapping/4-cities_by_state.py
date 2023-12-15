#!/usr/bin/python3

'''
* Write a script that lists all cities from the database hbtn_0e_4_usa
    * Your script should take 3 arguments: mysql username
mysql password and database name
    * You must use the module MySQLdb (import MySQLdb)
    * Your script should connect to a MySQL server
running on localhost at port 3306
    * Results must be sorted in ascending order by cities.id
    * You can use only execute() once
    * Results must be displayed as they are in the example below
    * Your code should not be executed when imported
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    username, password, database = argv[1:4]
    connection = MySQLdb.connect(
            host='localhost', port=3306, user=username,
            passwd=password, db=database
            )
    cursor = connection.cursor()
    query = '''SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC'''
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()
