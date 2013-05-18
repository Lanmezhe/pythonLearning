#!/usr/bin/python 

import os
import time

#list
source = ['/home/lanmezhe/backuptest/sdf', '/home/lanmezhe/backuptest2/Untitled Document']

target_dir = '/home/lanmezhe/'

today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment-->')

if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' +\
			comment.replace(' ','_') + '.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print"Successfully created directory", today

zip_command = "zip -qr '%s' %s"%(target,' '.join(source))

print zip_command

if os.system(zip_command)==0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
