#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="postgres")
cursor = conn.cursor()
def main(args):
    option=raw_input ("Select from the options below: \n 1.Adding Student Data \n 2. Fetching Student Record")
	if option=1:
		add_stu()
	elif option=2:
		fetch_stu()
    return 0