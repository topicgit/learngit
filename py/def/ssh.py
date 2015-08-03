#!/usr/bin/env python

import os

user='root'
ip = 'localhost'
cmd = 'df'

def runCmd(uname,host,command = 0):
	if command != 0:
		CMD='ssh %s@%s %s' % (uname,host,command)
	else:
		CMD='ssh %s@%s ' % (uname,host)
	print CMD
	os.system(CMD)
	print '\033[32;1mExit from %s,bye !\033[0m' % host

runCmd(user,ip,cmd)
