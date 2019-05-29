import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'ercess-event')

a = conn.cursor()

sql = 'SELECT * from `articles2`;'
a.execute(sql)

countrow = a.execute(sql)
print("Number of rows: ", countrow)
data = a.fetchall()
print(data)