#!/usr/bin/env python


import psycopg2
import urllib2
import sys


con = None

try:
    con = psycopg2.connect(database='cereal',user='bbrelin')
    cur=con.cursor()
    cur.execute('DROP TABLE cereal_data')
    cur.execute('CREATE TABLE cereal_data(cereal_index serial, cereal_name varchar(30), c_mfg char, cereal_type char, calories int, protein int, fat int, sodium int, fiber int, carbohydrates int, sugar int, display_shelf int, potassium int, vitamins int, weight int,cups_per_serving int)')
    con.commit()

except psycopg2.DatabaseError,e:
    con.rollback()
    print "Error %s" %e
    sys.exit(1)

#finally:
#   if con:
#       con.close(),

response = urllib2.urlopen("http://lib.stat.cmu.edu/datasets/1993.expo/cereal")

cereal_list = []

for data in response:
    cereal_list.append(data.strip().split())

try:
    con = psycopg2.connect(database='cereal',user='bbrelin')
    cur=con.cursor()
    for record in cereal_list:
        cur.execute('INSERT INTO cereal_table (cereal_name,c_mfg,cereal_type,calories,protein,fat,sodium,fiber,carbohydrates,sugar,display_shelf,potassium, vitamins,weight,cups_per_serving) VALUES (%s, %c, %c, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)' , (record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14]))
    con.commit()
except psycopg2.DatabaseError,e:
    con.rollback()
    print "Error %s" %e
    sys.exit(1)
finally:
   if con:
       con.close(),
