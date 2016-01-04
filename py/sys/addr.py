#!/usr/bin/python
#Filename: addr.py

import sys
import pickle as pi


class Person:
	def __init__(self,name,age,email,phone):
		self.name=name
		self.age=age
		self.email=email
		self.phone=phone

	def printInfo(self):

		print '-----------------------------'
		print
		print '''Name : %s 
age  : %s 
email: %s 
phone: %s
			   ''' % (self.name,self.age,self.email,self.phone)
		print '-----------------------------'

def add():

	aname=raw_input('\033[32;1mInput You name) : \033[0m').strip()
	aage=raw_input('\033[32;1mage) : \033[0m').strip()
	aemail=raw_input('\033[32;1memail) : \033[0m').strip()
	aphone=raw_input('\033[32;1mphone) : \033[0m').strip()

	p=Person(aname,aage,aemail,aphone)
	p.printInfo()



add()
#while True:
#	user_input = raw_input('\033[33;1mSelect model [ sea/add/mod/del ]: \033[0m').strip()
#
#	if len(user_input) == 0:continue
#
#	if user_input == 'exit' :
#		sys.exit()
#	
#	elif user_input == 'sea' :
#		print '-'*40
#		print 'Loading Search mode ...'
#		print '\033[32;1mInput name/email/phone to search  : \033[0m'
#		print '-'*40
#		while True:
#			search_str = raw_input('\033[33;1mSearch Mode  : \033[0m').strip()
#
