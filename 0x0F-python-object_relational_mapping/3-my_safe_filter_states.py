#!/usr/bin/python3
""" takes in arguments and displays all values in the states table """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    C = db.cursor()
    matching = sys.argv[4]
    C.execute("SELECT * FROM states WHERE name LIKE %s", (matching, ))
    rows = C.fetchall()
    for row in rows:
        print(row)
    C.close
    db.close
