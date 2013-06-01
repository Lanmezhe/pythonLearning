#!/usr/bin/python 


class ShortInputException(Exception):
	'''A user-defined except class.'''
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	s = raw_input('Enter somthing-->')
	if len(s) < 3:
		raise ShortInputException(len(s), 3)
	print'Other work.'

except EOFError:
	print'\nWhy did you do an EOF on me?'
	sys.exit()
except ShortInputException,x:
	print'ShortInputException: THe input was of length %d, was expecting at least %d' %(x.length, x.atleast)
else:
	print'No exception was raise.'

