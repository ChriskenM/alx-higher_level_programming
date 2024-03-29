#!/usr/bin/python3
"""
    filter states starting with N
"""


import sys
import MySQLdb


if __name__ == '__main__':

    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT *\
                FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS \
    LIKE 'N%';")
    states = cur.fetchall()

    for state in states:
        print(state)
