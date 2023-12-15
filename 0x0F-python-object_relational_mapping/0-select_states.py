#!/usr/bin/python
'''
* Write a script that lists all states from the database hbtn_0e_0_usa:
    * Your script should take 3 arguments: mysql username, 
    mysql password and database name (no argument validation needed)
    * You must use the module MySQLdb (import MySQLdb)
    * Your script should connect to a MySQL server running on localhost at port 3306
    * Results must be sorted in ascending order by states.id
    * Results must be displayed as they are in the example below
    * Your code should not be executed when imported
'''
import MySQLdb
from sys import argv

''' Establish a connection'''
connection = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3])

''' Create a cursor object to execute SQL queries'''
cursor = connection.cursor()

cursor.execute('SELECT * FROM states ORDER BY states.id ASC')

results = cursor.fetchall()

for row in results:
    print(row)
