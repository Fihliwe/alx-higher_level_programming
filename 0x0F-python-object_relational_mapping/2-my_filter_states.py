#!/usr/bin/python3
'''Module that lists states from the hbtn_0e_0_usa'''
import MySQLdb
from sys import argv



'''The code should not be executed when imported so (if main) should be used'''
if __name__ == '__main__':

    '''make a connection to the database'''
    db = MySQLdb.connect(host="localhost", port=3306, 
                         mysql_username=argv[1], 
                         mysql_password=argv[2], 
                         data_base_name=argv[3],
                         )
    
    '''creating a cursor object to execute SQL quaeries'''
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(query)

    '''iterate trough to show the results'''
    rows = cur.fetchall()
    for i in rows:
        print(i)

    '''close the cursor and database connection'''
    cur.close()
    db.close()