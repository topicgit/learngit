#!/usr/bin/python
#Filename: backup_ver2.py

import os
import time
import sys

def help():
	print 'Usage: python %s  src  dst' % sys.argv[0]
	
if len(sys.argv) != 3 :
	help()
	sys.exit()

source=[]
source.append(sys.argv[1])
target_dir=sys.argv[2]

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory',today

target = today + os.sep + now + '.tar.gz'
zip_command = "tar -zcf %s %s" % (target,' '.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup to',target
else:
	print 'Backup FAILED'
