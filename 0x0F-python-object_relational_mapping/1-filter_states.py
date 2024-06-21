#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) from hbtn_0e_0_usa. """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user_name=sys.argv[1],
                        passwd=sys.argv[2], dbname=sys.argv[3], posrt=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states where name
                LIKE BINARY "N%" ORDER BY states.id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
