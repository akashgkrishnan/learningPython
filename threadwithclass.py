from threading import Thread

class MyThread(Thread):
    def run(self):
        for i in range(5):
            print(f"Being executed in the thread class {i}")

t = MyThread()
t.start()
for i in range(5):
    print("in child class", i)