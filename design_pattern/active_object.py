from threading import Thread
import queue


class ActiveObject:

    def __init__(self):
        self._q = queue.Queue()
        self._thread = Thread(target=self.__run)
    
    def __run(self):
        while True:
            self._q.get()()

    def start(self):
        self._thread.start()

    def run(self, func):
        self._q.put(func)

var = 0    

def test_print():
    global var
    print(var)
    var += 1


if __name__ == '__main__':
    import time
    import os
    ao = ActiveObject()
    ao.start()
    for _ in range(5):
        ao.run(test_print)
    time.sleep(1)
    os._exit(1)