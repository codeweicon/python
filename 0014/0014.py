# -*- coding:utf-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy

f = open('student.txt')
datalist = []
data = []
lines = f.readlines()
for i in range(1,len(lines)-1):
	left = lines[i].find('[')
	right = lines[i].find(']')
	string = lines[i][left+1:right].replace('"','')
	datalist.append(string.split(','))
	
wb = xlwt.Workbook(encoding='utf-8') #wb for workbook
ws = wb.add_sheet('studentInfo') #ws for work sheet
for i in range(0,len(datalist)):
	ws.write(i,0,i)
	for j in range(0,4):
		ws.write(i,j+1,datalist[i][j])
wb.save('student.xls')
f.close()
