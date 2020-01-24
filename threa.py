import threading
print(threading.current_thread().getName())
def mythread(n):
    for i in range(n):
        print(f" Thread is exexcuting me: {i}")
    print("current thread : ",threading.current_thread().getName())

n = int(input("enter number: "))
t = threading.Thread(target=mythread, args= (n,))
t.start()
print(" i am running on a different thread: ")
for i in range(n):
    print(i)

