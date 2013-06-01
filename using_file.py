#!/usr/bin/python 

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''

f = file('poem.txt','w') 
f.write(poem)
print'==>file haved been writed'
f.close()

f = file('poem.txt')
#if no mode is defined. 'r' setted by default

while True:
	line = f.readline()
	if len(line) == 0:
		break
	print line,
	#Notic comma to avoid automatic newline added by Python

f.close()
