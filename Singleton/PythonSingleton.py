# -*- coding: utf-8 -*-
import threading

class ChocolateBoiler(object):
    def __init__(self):
        self._empty = True
        self._boiled = False
        self._locker = threading.Lock()

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

# クラス定義をオブジェクトで上書きして、
# 簡単に新しいオブジェクトを生成できないようにする
ChocolateBoiler = ChocolateBoiler()

if __name__ == '__main__':

    def Process(name):
        for i in range(3):
            print "\n* %s start processing..." % name
            ChocolateBoiler.fill()
            ChocolateBoiler.boil()
            ChocolateBoiler.drain()
            
            # Singleton パターンには従っているが、
            # 結局、各々のメソッドはスレッドセーフではない。
            # スレッドセーフにするためには、各スレッドに同期機構が必要。
            
    a = threading.Thread(target=Process, args="A")
    b = threading.Thread(target=Process, args="B")
    
    a.start()
    b.start()

    a.join()
    b.join()

    
   
