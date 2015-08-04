import requests
import re
import thread
import threading

def getimgurl():
	url = 'http://tieba.baidu.com/p/2166231880'
	r = requests.get(url)
	content = r.content
	pattern = re.compile('http://imgsrc.baidu.com/forum/w%3D580/(.*?).jpg')
	imglist =  re.findall(pattern,content)
	imgurl = []
	for item in imglist:
		print item
		imgurl.append('http://imgsrc.baidu.com/forum/w%3D580/'+item+'.jpg')
	return imgurl

def savepic(imgurl):
	count = 1
	for item in imgurl:
		filename = 'pic/'+str(count)+'.jpg'
		ff = open(filename, 'wb')
		data = requests.get(item).content
		print 'Download the '+str(count)+' pic'
		ff.write(data)
		count+=1
	ff.close

if __name__ == '__main__':
	imgurl = getimgurl()
	savepic(imgurl)


