#-*- coding:utf-8 -*-
import xlrd

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import dump

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            indent(e, level+1)
        if not e.tail or not e.tail.strip():
            e.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i
    return elem

def loaddata(file):
	wb = xlrd.open_workbook(file)
	ws = wb.sheet_by_index(0)
	datalist = []
	for i in range(0,ws.nrows):
		datalist.append(ws.row_values(i))
	return datalist

def datatoxml(xlsdata):
	xml = ElementTree()
	Students = Element('Students')
	xml._setroot(Students)
	for i in range(0,len(xlsdata)):
		Student = Element('Student',{'Name':xlsdata[i][1]})
		Students.append(Student)
		Scores = Element('Scores')
		Student.append(Scores)
		SubElement(Scores,'math').text= xlsdata[i][2]
		SubElement(Scores,'Yuwen').text = xlsdata[i][3]
		SubElement(Scores,'English').text = xlsdata[i][4]
	dump(indent(Students))
	return xml

if __name__ =='__main__':
	data = loaddata('student.xls')
	xml = datatoxml(data)
	xml.write('Students.xml','utf-8')
