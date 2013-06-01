#!/usr/bin/python 

import sys

def readfile(filename):
	'''Print a file to the standard output'''
	f = file(filename)
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print line,
	f.close()

#START
if len(sys.argv) < 2:
	print'No action specified.'
	sys.exit()

if sys.argv[1].startswith('--'):
	option = sys.argv[1][2:]
	#fetch sys.argv[1] but without the first two characters
	if option == 'version':
		print'Version 1.2'
	elif option == 'help':
		print'''\
This Program has NO HELP
'''
 	else:
		print'Unknown option'
	sys.exit()
else:
	print'sys.argv[0] is %s' %sys.argv[0]
	for filename in sys.argv[1:]:
		readfile(filename)
