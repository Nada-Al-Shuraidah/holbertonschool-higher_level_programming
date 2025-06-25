#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
where name matches the argument (unsafe version)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8"
    )
    cur = conn.cursor()
    # لا تضيف escaping يدوي، خله زي كذا بالضبط
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
