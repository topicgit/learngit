#!/usr/bin/python
#Filename:inherit.py

class SchooMember:
	'''Represents any school member.'''
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print '(Initialized SchooMember: %s)' % self.name

	def tell(self):
		'''Tell my details.'''
		print 'Name:"%s" Age:"%s"' % (self.name,self.age)

class Teacher(SchooMember):
	'''Represents a teacher.'''
	def __init__(self,name,age,salary):
		SchooMember.__init__(self,name,age)
		self.salary=salary
		print '(Initialized Teacher:%s)' % self.name

	def tell(self):
		SchooMember.tell(self)
		print 'Salary:"%d"' % self.salary

class Student(SchooMember):
	'''Represents a student'''
	def __init__(self,name,age,marks):
		SchooMember.__init__(self,name,age)
		self.marks=marks
		print '(Initialized Student:%s)' % self.name

	def tell(self):
		SchooMember.tell(self)
		print 'Marks:"%d"' % self.marks

t=Teacher('Mrs.Shrividya',40,30000)
s=Student('Swaroop',22,75)

print

members=[t,s]

for member in members:
	member.tell()
