from filosofo import *
from ventana import *

def lanzar():

    N = 5

    ventana= Ventana()
    lista=[]
    for i in range(N):
        lista.append(filosofo(ventana)) #AGREGA UN FILOSOFO A LA LISTA

    for f in lista:
        f.start() #ES EQUIVALENTE A RUN()
    ventana.run()
    for f in lista:
        f.join() #BLOQUEA HASTA QUE TERMINA EL THREAD