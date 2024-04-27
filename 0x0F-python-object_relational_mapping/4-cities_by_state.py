#!/usr/bin/python3
"""  list all states from database hbtn
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    res = db.cursor()
    res.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = res.fetchall()
    for row in rows:
        print(row)
    res.close()
    db.close()
