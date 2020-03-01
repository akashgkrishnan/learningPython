import pymysql as sql

conn = sql.connect(host = 'localhost', user = 'root', password = 'Akash@1996', database = 'DUCAT', port = 3306)

roll = int(input("Enter roll number: "))
name= input("Enter name : ")
marks = int(input("ENter marks : "))
cur = conn.cursor()
cur.execute(f"INSERT INTO STUDENTS VALUES ({roll}, '{name}', {marks})")
cur.execute("INSERT INTO STUDENTS VALUES (%s, %s, %s)", (roll+1, name , marks))
conn.commit()
conn.close()
