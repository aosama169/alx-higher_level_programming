#!/usr/bin/python3
"""  list all states from database hbtn
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    res = db.cursor()
    res.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = res.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    res.close()
    db.close()
