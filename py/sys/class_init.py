#!/usr/bin/python
#Filename: class_init.py

class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def sayHi(self):
		print 'Hello,my name is',self.name
	def sayage(self):
		print 'Hello,my age is',self.age

p=Person('Swaroop',19)
p.sayHi()
p.sayage()
