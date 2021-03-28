#!/usr/bin/python3
"""
Lists all states from hbtn_0e_0_usa where
name matches the input argument (argv[4])
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    line = """SELECT * FROM states WHERE name
           LIKE BINARY '{}' ORDER BY states.id ASC"""
    toExect = line.format(argv[4])
    cur.execute(toExect)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
