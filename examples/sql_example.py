#!/usr/bin/env python


import psycopg2
import sys

con = None

try:
    con = psycopg2.connect(database='test1',user='bbrelin')
    cur=con.cursor()
    cur.execute('CREATE TABLE bar  ( meh varchar(20), bleh int, mydate date)')
    con.commit()
#    cur.execute('SELECT version()')
#    ver=cur.fetchone()
#    print ver
except psycopg2.DatabaseError,e:
    print "Error %s" %e
    sys.exit(1)

finally:
   if con:
       con.close()
