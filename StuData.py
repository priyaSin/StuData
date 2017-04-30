#!/usr/bin/env python
# -*- coding: utf-8 -*-

def add_stu():
	import Add_Stu
def fetch_stu():
	import Fetch_Stu
def main():
	option=int(raw_input("Select from the options below: \n 1.Adding Student Data \n 2. Fetching Student Record \n"))
	if option==1:
		add_stu()
	elif option==2:
		fetch_stu()
	return 0
	
if __name__ == "__main__":
    main()