#!/usr/bin/python
#Filename:try_except.py

import sys

try:
	s=raw_input('Enter something -->')
except EOFError:
	print '\n Why did you do an EOF on me?'
	sys.exit()
except:
	print '\nSome error/exception occurreed.'


print 'Done'
