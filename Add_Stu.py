#!/usr/bin/env python
# -*- coding: utf-8 -*-
import StuData_Connect

StuData = open("StuData.csv","r")

for line in StuData:
	fields = line.split(',')
	query = "INSERT INTO STUDATA VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
	data = (fields[0],fields[1],fields[2],fields[3],fields[4],fields[5],fields[6],fields[7],\
		   fields[8],fields[9],fields[10],fields[11],fields[12],fields[13])
	cursor.execute(query,data)
	conn.commit()

StuData.close()