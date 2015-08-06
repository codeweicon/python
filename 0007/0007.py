# -*- coding:utf-8 -*-
f = open('test.py')
lines = f.readlines()
comments = 0
codeline = 0
spaceline = 0
for index, item in enumerate(lines):
	# print 'line number :',index
	# print 'line length :',len(item)
	print 'line content:',item.strip('\n')
	stripstr = item.strip('\n').strip('\t').replace(' ','')
	if item.strip(' ').strip('\t')[0] == '#':
		print '**this is comments line**\n'
		comments += 1
	elif len(stripstr) == 0:
		print '**this is space line**\n'
		spaceline += 1
	else:
		print '**this is code line**\n'
		codeline += 1

print 'comments line :',comments
print 'code line :',codeline
print 'space line :',spaceline

f.close()