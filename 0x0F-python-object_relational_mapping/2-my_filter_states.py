#!/usr/bin/python3
""" Display all values in the states table where name matches
the argument and prevent a SQL injection """


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT *\
    FROM states WHERE states.name =%s\
    ORDER BY id ASC", (sys.argv[4],))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
