import random

def random_str(length):
	str = ''
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
	# print chars[62]
	for i in range(length):
		index = random.randint(0, len(chars)-1)
		# print "index ",index
		str+=chars[index]
	return str

if __name__ == '__main__':
	f = open('0001.txt','a')
	for i in range(200):
		string = random_str(6)
		print string
		f.write(string+'\n')
	f.close()
