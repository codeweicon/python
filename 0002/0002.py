
import MySQLdb
import sys
try:
	conn = MySQLdb.connect(
			host = 'localhost',
			port = 3306,
			user = 'root',
			passwd = '085418',
			db = 'test'
		)
except Exception, e:
    print e
    sys.exit()
cur = conn.cursor()

# sql = 'create table accode'
# cur.execute(sql)

# string = 'abcd'
# cur.execute("insert into accode(code) values ('%s')"%(string))

f = open('code.txt')
for line in f.readlines():
	cur.execute("insert into accode(code) values ('%s')"%(line[:-1]))

cur.close()
conn.commit()
conn.close()