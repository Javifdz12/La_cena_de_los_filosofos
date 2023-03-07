from otro_formato import *

def lanzar():
    Nfilosofos = 5

    tenedor = [1,1,1,1,1]

    for i in range(Nfilosofos):
        tenedor[i] = threading.BoundedSemaphore(1)

    for i in range(0,4):
        t = Filosofo(i, tenedor)
        t.start()
        time.sleep(0.5)