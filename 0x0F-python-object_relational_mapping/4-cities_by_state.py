#!/usr/bin/python3

"""A script that lists all cities from the database hbtn_0e_4_usa."""

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
            "SELECT cities.state_id, cities.name, states.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id"
    )

    """ Obtaining query results """
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """ Closing the cursor and the database """
    cur.close()
    db.close()
