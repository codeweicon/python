import xlrd
import xlwt

f = open('numbers.txt')
lines = f.readlines()
datalist = []
for i in range(1, len(lines)-1):
	str =  lines[i][lines[i].find('[')+1:lines[i].find(']')-1]
	datalist.append(str.split(','))
wb = xlwt.Workbook(encoding = 'utf-8')
ws = wb.add_sheet('city')
for i in range(0,len(datalist)):
	for j in range(0,3):
		ws.write(i,j,datalist[i][j])
wb.save('numbers.xls')
f.close()