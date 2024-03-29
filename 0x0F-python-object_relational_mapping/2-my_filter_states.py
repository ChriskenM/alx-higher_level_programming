#!/usr/bin/python3
"""
displays all values in the states table
where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(port=3306, user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * \
                FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))

    states = cur.fetchall()

    for state in states:
        print(state)
