#!/usr/bin/python
'''input
055
'''
import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres")
print "Opened database successfully"

cur = conn.cursor()
id=raw_input("Enter ID of the student:")
roll_no = (id,)
cur.execute("SELECT *  from STUDATA WHERE ID=%s",roll_no)
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   totalMarks= row[2]+row[3]+row[4]+row[5]+row[6]+row[7]
   maxMarks=row[8]+row[9]+row[10]+row[11]+row[12]+row[13]
   per= totalMarks/maxMarks
   avg= totalMarks/6
   if per < 33:
   	result= "Pass"
   else:
    result= "Fail"
   gpa= (per/20)-1	
   print "TOTAL MARKS = " ,totalMarks
   print "PERCENTAGE = " ,per
   print "AVERAGE = " ,avg
   print "GPA = ",gpa
   print "RESULT = ", result

print "Operation done successfully";
conn.close()
if __name__ == "__main__":
    main()