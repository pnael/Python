#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import sys

db = None

try:
    db = MySQLdb.connect(
        "sql.free.fr",
        "philippe.nael",
        "0fkxvrvw",
        "philippe_nael")
    cursor = db.cursor()

    query = """SELECT * FROM pna_test"""
    result = cursor.execute(query)

    print "Il y a %d résulats:" %  (result,)
    for line in cursor.fetchall():
        print ' - %s' % line[1]

except MySQLdb.DatabaseError, e:
    print 'Error %s' %e
    sys.exit(1)

finally:
    if db:
        cursor.close()
        db.close()

