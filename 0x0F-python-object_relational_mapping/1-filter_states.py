#!/usr/bin/python3

"""A script that lists all states with a name starting with N from the
database hbtn_0e_0_usai.

It takes 3 arguments : mysql username, mysql password and database name.
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    """ Connecting to the database """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    """ Getting the cursor """
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    """ Obtaining query results """
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """ Closing the cursor and the database """
    cur.close()
    db.close()
