
#-*- coding: UTF-8 -*-
#!/usr/bin/python 

#首行解决中文编码问题

###########################################
#设置编码，解决中文问题.或者如下：
###########################################
#import sys
#encoding = sys.getdefaultencoding()
#print encoding
#reload(sys)
#sys.setdefaultencoding("UTF-8")
#encoding = sys.getdefaultencoding()
#print encoding
###########################################
#还或者如下：
#print "呵呵".decode().encode("GBK")
###########################################


class Person:
	'''Represents a person'''
	population = 0

	def __init__(self,name):
		'''Initializes the person's data.'''
		self.name = name 
		print '(Initializing %s)' %self.name
		Person.population += 1

	def __del__(self):
		'''I am dying.'''
		print '%s says bye.' %self.name
		print globals()['Person']
		Person.population -= 1
		
		if 'Person.population' == 0:
			###############################################################################################
			#此处会出错，因为Python回收机制并不确定何时回收Person，有可能当调用到此处的时候Person已经被回收
			###############################################################################################
			print 'I am the last one.'
		else:
			print 'There are still %d pepole left.' %Person.population

	def sayHi(self):
		print 'Hi, my name is '+self.name
	
	def howMany(self):
		if Person.population == 1:
			print 'I am the only person here.'
		else:
			print 'We have %d persons here.' %Person.population

xiaohong = Person('Xiaohong')
xiaohong.sayHi()
xiaohong.howMany()

huang = Person('huang')
huang.sayHi()
huang.howMany()

xiaohong.sayHi()
xiaohong.howMany()
