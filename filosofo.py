import random
import threading
import time

class Filosofo(threading.Thread):
    def __init__(self, num, tenedor):
        threading.Thread.__init__(self)
        self.tenedor = tenedor
        self.num = num
        self.temp = (self.num + 1) % 5

    def come(self):
        print ("El filosofo "+str(self.num+1)+" come")

    def piensa(self):
        print ("El filosofo "+str(self.num+1)+" piensa")

    def obtieneTenIzq(self):
        print ("El filosofo "+str(self.num+1)+" obtiene tenedor izquierdo")
        print ("obtiene el tenedor"+str(self.num+1))
        self.tenedor[self.num].acquire()

    def obtieneTenDer(self):
        print ("El filosofo "+str(self.num+1)+" obtiene tenedor derecho")
        print ("obtiene el tenedor"+str(self.temp+1))
        self.tenedor[self.temp].acquire()

    def liberaTenDer(self):
        print ("El filosofo "+str(self.num+1)+" libera tenedor derecho")
        self.tenedor[self.temp].release()

    def liberaTenIzq(self):
        print ("El filosofo "+str(self.num+1)+" libera tenedor izquierdo")
        self.tenedor[self.num].release()

    def run(self):
        while True:
            self.piensa()
            self.obtieneTenIzq()
            self.obtieneTenDer()
            self.come()
            self.liberaTenDer()
            self.liberaTenIzq()
