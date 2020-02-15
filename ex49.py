
f2 = open('/home/akash/Desktop/hi2.jpg', 'rb')
data = f2.read()
print(data[-16:].decode())
f2.close()