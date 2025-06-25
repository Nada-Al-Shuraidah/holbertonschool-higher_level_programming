#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where name matches the argument
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
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name.replace("'", "''"))
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
