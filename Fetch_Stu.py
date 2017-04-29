#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("SELECT ID, NAME, MATHS , SCIENCE, SOCIAL_SCIENCE,HINDI,ENGLISH,COMPUTER_SCIENCE  from STUDATA")
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "MATHS = ", row[2]
   print "SCIENCE = ", row[3]
   print "SOCIAL_SCIENCE = ", row[4]
   print "HINDI = ", row[5]
   print "ENGLISH = ", row[6]
   print "COMPUTER_SCIENCE = ", row[7], "\n"

print "Operation done successfully";
conn.close()