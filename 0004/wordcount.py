f = open('english.txt')
content = f.read()

contentlist = content.replace('.','').replace(',','').split(' ')
count = 0
for item in contentlist:
	print item
	count += 1
print 'count =',count
f.close()

# import re

# def count(filepath):
#     f = open(filepath, 'rb')
#     s = f.read()
#     words = re.findall(r'[a-zA-Z]+', s)
#     return len(words)

# if __name__ == '__main__':
#     num = count('english.txt')
#     print num