#!/usr/bin/python
#Filename:objvar.py

class Person:
	'''Represents a person.'''
	population=0

	def __init__(self,name):
		'''Initializes the person's data'''
		self.name=name
		print '(initializing %s)' % self.name

		Person.population+=1
 
