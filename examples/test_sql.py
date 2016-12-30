#!/usr/bin/env python


import psycopg2
import urllib2
import sys


con = None

try:
    con = psycopg2.connect(database='cereal',user='bbrelin')
    cur=con.cursor()
    cur.execute('CREATE TABLE test(alpha varchar(10), beta varchar(10))')
    con.commit()
    cur.execute('INSERT INTO test (alpha,beta) VALUES (%s,%s)',("foo","bar"))
    con.commit()

except psycopg2.DatabaseError,e:
    con.rollback()
    print "Error %s" %e
    sys.exit(1)


finally:
   if con:
       con.close(),

