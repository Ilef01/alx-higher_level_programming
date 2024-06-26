#!/usr/bin/python3

""" a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""

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
    cur.execute(
        "SELECT * FROM states "
        "WHERE name = %s "
        "ORDER BY id",
        (sys.argv[4],)
    )

    """ Obtaining query results """
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """ Closing the cursor and the database """
    cur.close()
    db.close()
