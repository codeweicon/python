import xlrd
import xlwt
from xlutils.copy import copy

f = open('city.txt')
lines = f.readlines()
datalist = []
for i in range(1,len(lines)-1):
	string =  lines[i].replace('"','').replace(',','').strip('\n').strip(' ')
	datalist.append(string.split(':'))
print datalist
wb = xlwt.Workbook(encoding = 'utf-8')
ws = wb.add_sheet('city')
for i in range(0,len(datalist)):
	ws.write(i,0,i)
	ws.write(i,1,datalist[i][1])
wb.save('city.xls')
f.close()