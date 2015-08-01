# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
f = open('filtered_words.txt')
wordlist = []
for line in f.readlines():
	wordlist.append(line.strip('\n').strip('\r'))
while(True):
	flag = 0
	word = raw_input('input your word: ')
	for item in wordlist:
		if item in word:
			flag = 1
	if flag == 1:
		print 'Freedom'
	else:
		print 'Human Rights'
f.close()
