#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa safely
Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name> <state name>
Results sorted by cities.id ascending, displayed as city names separated by comma
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name,
                         charset="utf8")

    cursor = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    if rows:
        print(", ".join(city[0] for city in rows))

    cursor.close()
    db.close()
