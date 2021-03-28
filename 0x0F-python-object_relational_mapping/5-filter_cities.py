#!/usr/bin/python3
"""
Takes in the name of a state as an argument
and lists all cities of that state
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        WHERE states.name = %s ORDER BY cities.id ASC;
        """, (argv[4], ))
    query_rows = cur.fetchall()
    print(", ".join([row[1] for row in query_rows]))
    cur.close()
    db.close()
