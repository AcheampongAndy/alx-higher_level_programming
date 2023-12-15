#!/usr/bin/python3

'''
* Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where name matches the argument
    * Your script should take 4 arguments:
mysql username, mysql password, database name
and state name searched (safe from MySQL injection)
    * You must use the module MySQLdb (import MySQLdb)
    * Your script should connect to a MySQL
server running on localhost at port 3306
    * You must use format to create the SQL query with the user input
    * Results must be sorted in ascending order by states.id
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

    query = 'SLECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC'
    cursor.execute(query, (state_name + %,))
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()
