import pymysql as sql
conn = sql.connect(host = 'localhost', user = 'root', password = 'Akash@1996', database = 'DUCAT', port = 3306)
cur = conn.cursor()
cur.execute("INSERT INTO STUDENTS VALUES (202, 'PYTHON', 99)")
conn.commit()
conn.close()

'''
parametrised query 
it comtains parameters to represent runtime values
we may use any type of values
no chance of sql injection attacks
a parameter in a query is denoted by db dpendant symbols ( in mysql it is %s in sqlite it is ? )

Non parametrised query


'''
