import threading
import sys

def logg():
    while 1:
        x=input()
        print(x)
myThread = threading.Thread(target=logg)
myThread.start
print('lol')