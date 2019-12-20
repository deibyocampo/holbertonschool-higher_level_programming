#!/usr/bin/python3
""" Tale in the name of a state and list all cities of that state """


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name\
    FROM cities\
    WHERE cities.state_id IN\
    (SELECT id FROM states WHERE name = %s GROUP BY ID)\
    ORDER BY cities.id ASC", (sys.argv[4],))

    query_rows = cur.fetchall()
    print(", ".join(item[0] for item in query_rows))
    cur.close()
    db.close()
