# -*- coding: utf-8 -*-

#import threading
import multiprocessing 

class ChocolateBoiler(object):
    def __init__(self):
        self._empty = True
        self._boiled = False
        self._locker = multiprocessing.Lock()

    def fill(self):
        with self._locker:
            if self._empty:
                self._empty = False
                self._boiled = False
                print '[1] Chocolate has been filled in boiler.'

    def drain(self):
        with self._locker:
            if not self._empty and self._boiled:
                self._empty = True
                print '[3] Chocolate has been drained from boiler.'

    def boil(self):
        with self._locker:
            if not self._empty and not self._boiled:
                self._boiled = True
                print '[2] Chocolate has been boiled.'

# Overwrite the class definition with its object
# to make it difficult to create another object.
ChocolateBoiler = ChocolateBoiler()

def func(name):
    for i in range(100):
        print "\n* %s start funcing..." % name
        ChocolateBoiler.fill()
        ChocolateBoiler.boil()
        ChocolateBoiler.drain()

if __name__ == '__main__':
  
    a = multiprocessing.Process(target=func, args="A")
    b = multiprocessing.Process(target=func, args="B")
    
    a.start()
    b.start()

    a.join()
    b.join()

    
   
