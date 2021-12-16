#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import datetime
debug = True

def verbose(args,val):
	if (args.verbose):
		print(val)
	
	return False

def logstr(string):
	if len(sys.argv) == 4:
		if (sys.argv[3] == "-vvv"):
			print(string)

	if (debug == True):
		today = datetime.datetime.now() 
		dirname = "debuglog/"
		logfile_name = dirname+"debug_" + today.strftime("%Y%m%d") +".log"
		f = open(logfile_name, "a")

		if isinstance(string, list):
			str1 = ','.join(str(e) for e in string)
			string = str1

		log_string=os.environ.get('USER')+" ["+today.strftime('%Y-%m-%d %H:%M:%S')+"] "+string
		f.write(log_string + "\n")
		f.close()
		return False