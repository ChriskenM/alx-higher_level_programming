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
    cur.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`".format(sys.argv[4]))
    states = cur.fetchall()

    for state in states:
        print(state)
