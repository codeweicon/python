import requests
import re
import threading

class spider(threading.Thread):
	def __init__(self, url,threadnum):
		self.url = url
		self.threadnum = threadnum
		self.imgurl = []
		threading.Thread.__init__(self)  #didn't complete this mutiple thread part

	def getimgurl(self):
		r = requests.get(self.url)
		content = r.content
		pattern = re.compile('http://imgsrc.baidu.com/forum/w%3D580/(.*?).jpg')
		imglist =  re.findall(pattern,content)
		for item in imglist:
			print item
			self.imgurl.append('http://imgsrc.baidu.com/forum/w%3D580/'+item+'.jpg')

	def savepic(self):
		count = 1
		for item in self.imgurl:
			print item
			filename = 'pic/'+str(count)+'.jpg'
			ff = open(filename, 'wb')
			data = requests.get(item).content
			print 'Download the '+str(count)+' pic'
			ff.write(data)
			count+=1
		ff.close()

if __name__ == '__main__':
	url = 'http://tieba.baidu.com/p/2166231880'
	threadnum = 2

	get = spider(url,threadnum)
	get.getimgurl()
	get.savepic()


