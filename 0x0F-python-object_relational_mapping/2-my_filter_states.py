#!/usr/bin/python3
""" Display all values in the states table where name matches the argument
"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT *\
    FROM states WHERE states.name\
    LIKE BINARY '{}'\
    ORDER by states.id ASC".format(sys.argv[4]))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
