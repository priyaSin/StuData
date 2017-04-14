#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="postgres")
cursor = conn.cursor()


StuData = open(StuData.csv,r)

for line in StuData:
	fields = line.split(',')
	query = "INSERT INTO STUDATA VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
	data = (fields[0],fields[1],fields[2],fields[3],fields[4],fields[5],fields[6],fields[7])
	cursor.execute(query,data)
	conn.commit()

StuData.close()