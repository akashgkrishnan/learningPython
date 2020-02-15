from datetime import datetime as dt
file = open('mylog.txt', 'a')
print('hello')
d = dt.now()
file.write("_"*100)
file.write("\nDate " +str(d))
file.write("\n")
file.write("_"*100)
file.close()