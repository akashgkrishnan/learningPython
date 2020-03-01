import pymysql as sql
from datetime import datetime

conn = sql.connect(host = 'localhost', user = 'root', password = 'Akash@1996', database = 'DUCAT', port = 3306)

cur = conn.cursor()
file = open("11.jpg", "rb")
img = file.read()
file.close()
cur.execute("INSERT INTO image_db VALUES(%s, %s)",(img, datetime.now()))

conn.commit()
conn.close()