#!/usr/bin/env python

import psycopg2
import sys


con = None

con = psycopg2.connect("host='localhost',dbname='cerealdb',user='bbrelin',password='secret')

cursor = con.cursor()

cursor.execute('select * from table1 where col1='foo')
records = cursor.fetchall()
print records
