#!/usr/bin/python3

'''
* Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
    * Your script should take 4 arguments: mysql username, mysql password
database name and state name (SQL injection free!)
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
    username, password, database, state_name = argv[1:5]
    connection = MySQLdb.connect(
            host='localhost', port=3306, user=username,
            passwd=password, db=database
            )
    cursor = connection.cursor()
    query = '''SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states ON cities.state_id = states.id 
    WHERE states.name LIKE %s ORDER BY cities.id ASC'''
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    results_list = []
    for row in results:
        results_list.append(row[1])

    results = ", ".join(results_list)
    print(results)

    cursor.close()
    connection.close()
