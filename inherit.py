#!/usr/bin/python 

class SchoolMember:
	'''Represents any school member.'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print'(Initialzed SchoolMember: %s)' %self.name
	
	def tell(self):
		'''Tell my details.'''
		print'Name:"%s" Age:"%s"' %(self.name,self.age)

class Teacher(SchoolMember):
	'''Represents a teacher.'''
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print'(Initialzed Teacher: %s)' %self.name

	def tell(self):
		SchoolMember.tell(self)
		print'Salary: "%d"' %self.salary

class Student(SchoolMember):
	'''Represents a student.'''
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print'(Initialzed Student: %s)' %self.name

	def tell(self):
		SchoolMember.tell(self)
		print'Marks: "%d"' %self.marks

t = Teacher('Pan',23,10000)
s = Student('Xiaoqiang',12,85)

print

members = [t, s]
for member in members:
	member.tell()




