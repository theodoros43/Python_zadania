#!/usr/bin/python3

import os

directory = '/home/pi/Documents/Python_zadania'
for dirpath,dirnames,filenames in os.walk(directory):
	print ("ścieżka :",dirpath)
	print ("katalogi :",dirnames)
	print ("pliki :",filenames)
