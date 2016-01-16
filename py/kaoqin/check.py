#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

check = '1.5_v7.txt'
day = '2015-01-06'

def get_time():
	a = random.randint(10, 50)
	return a

def gat():	
	atime = '08:%s:%s' % (get_time(),get_time())
	return atime

def gnt():	
	ltime = '23:%s:%s' % (get_time(),get_time())
	return ltime

f = open(check,'r')
cline = f.readlines()
f.close()


for i in range(len(cline)):

	userid = cline[i][0] + cline[i][1]	
	name = cline[i][3:]
	name.replace("\r\n"," ")

	print '%s,%s %s,%s,%s' % (userid,day,gat(),'1',name)
	print '%s,%s %s,%s,%s' % (userid,day,gnt(),'1',name)
	
