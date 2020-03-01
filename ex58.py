import pymysql as sql

conn = sql.connect(host = 'localhost', user = 'root', password = 'Akash@1996', database = 'DUCAT', port = 3306)

cur = conn.cursor()
cur.execute("select * from STUDENTS")
row = cur.fetchone()
print(row)
row = cur.fetchmany(2)
print(row, sep= '\n')


cur.scroll(1, mode = 'absolute')

row = cur.fetchall()
print(row)

conn.close()


