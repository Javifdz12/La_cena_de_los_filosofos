from filosofo import *
def lanzar():
    Nfilosofos = 5

    tenedor = [1,1,1,1,1]

    for i in range(Nfilosofos):
        tenedor[i] = threading.BoundedSemaphore(1)

    for i in [0,1,2,3,4]:
        t = Filosofo(i, tenedor)
        t.start()
        time.sleep(0.5)