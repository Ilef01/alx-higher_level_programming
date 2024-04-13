#!/usr/bin/python3

"""A script that takes the name of a state and lists all cities
of that state using the database hbtn_0e_4_usa."""

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
            "SELECT cities.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id",
            (sys.argv[4],)
    )

    """ Obtaining query results """
    rows = cur.fetchall()
    cities = ", ".join(row[0] for row in rows)
    print(cities)

    """ Closing the cursor and the database """
    cur.close()
    db.close()
