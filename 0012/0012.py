# -*- coding:utf-8 -*-
import sys
import chardet
reload(sys)
sys.setdefaultencoding('utf-8')
f = open('filtered_words.txt')
wordlist = []
for line in f.readlines():
	wordlist.append(line.strip('\n').strip('\r'))
while(True):
	word = raw_input('input your word: ')
	for item in wordlist:
		if item in word:
			if chardet.detect(item)['encoding'] == 'utf-8':
				print word.replace(item,'*'*(len(item)/3))
			else:
				print word.replace(item,'*'*len(item))
f.close()
