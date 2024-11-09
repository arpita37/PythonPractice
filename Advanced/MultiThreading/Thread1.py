from threading import *
from time import *

class One(Thread):
    def run(self):
        for i in range(8):
            print("This is my first class")
            sleep(0.7)


class Two(Thread):
    def run(self):
        for i in range(8):
            print("This is my second class")  
            sleep(0.3)


c1 = One()
c2 = Two()
c1.start()
c2.start()

c1.join()
c2.join()

print("this is the end")