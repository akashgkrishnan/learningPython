import mysql.connector as sql
conn = sql.connect(host = 'localhost', user = 'root', password = 'Akash@1996', database = 'DUCAT', port = 3306)
cur = conn.cursor()
cur.execute("INSERT INTO STUDENTS VALUES (201, 'PYTHON', 99)")
conn.commit()
conn.close()