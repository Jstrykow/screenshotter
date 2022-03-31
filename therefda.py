from threading import Thread
import time
class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            print('A\n')
            time.sleep(1)

class myClassB(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            print("B\n")
            time.sleep(2)


myClassA()
myClassB()
while True:
    pass
