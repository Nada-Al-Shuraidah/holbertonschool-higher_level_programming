#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where name matches the argument safely
Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name>
Results sorted by states.id ascending
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
    # Use parameterized query to avoid SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
