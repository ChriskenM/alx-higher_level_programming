#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists
all cities of that state
"""

import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(port=3306, user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE state.name = '{}';".format(sys.argv[4]))
    states = cur.fetchall()

    for state in states:
        print(state)
