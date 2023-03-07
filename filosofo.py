
import time
import random
import threading
from ventana import Ventana
import tkinter as tk

N = 5
TIEMPO_TOTAL = 3

class filosofo(threading.Thread):
    semaforo = threading.Lock() #SEMAFORO BINARIO ASEGURA LA EXCLUSION MUTUA
    estado = [] #PARA CONOCER EL ESTADO DE CADA FILOSOFO
    tenedores = [] #ARRAY DE SEMAFOROS PARA SINCRONIZAR ENTRE FILOSOFOS, MUESTRA QUIEN ESTA EN COLA DEL TENEDOR
    count=0

    def __init__(self,ventana):
        super().__init__()      #HERENCIA
        self.ventana=ventana
        self.veces=0
        self.id=filosofo.count #DESIGNA EL ID AL FILOSOFO
        filosofo.count+=1 #AGREGA UNO A LA CANT DE FILOSOFOS
        filosofo.estado.append('PENSANDO') #EL FILOSOFO ENTRA A LA MESA EN ESTADO PENSANDO
        filosofo.tenedores.append(threading.Semaphore(0)) #AGREGA EL SEMAFORO DE SU TENEDOR( TENEDOR A LA IZQUIERDA)
        print("FILOSOFO {0} - PENSANDO".format(self.id))
        self.ventana.visualizacion("FILOSOFO {0} - PENSANDO".format(self.id))

    def __del__(self):
        self.ventana.visualizacion("FILOSOFO {0} - Se para de la mesa".format(self.id))  #NECESARIO PARA SABER CUANDO TERMINA EL THREAD

    def codigoColores(self):
        self.ventana.lista4.config(bg= "blue")
        self.ventana.lista4.config(bg= "pink")
        self.ventana.lista4.config(bg= "white")
        self.ventana.lista4.config(bg= "yellow")
        self.ventana.lista4.config(bg= "greem")
        self.ventana.lista4.config(bg= "grey")

    def pensar(self):
        time.sleep(random.randint(0,5)) #CADA FILOSOFO SE TOMA DISTINTO TIEMPO PARA PENSAR, ALEATORIO

    def derecha(self,i):
        return (i-1)%N #BUSCAMOS EL INDICE DE LA DERECHA

    def izquierda(self,i):
        return(i+1)%N #BUSCAMOS EL INDICE DE LA IZQUIERDA

    def verificar(self,i):
        if filosofo.estado[i] == 'HAMBRIENTO' and filosofo.estado[self.izquierda(i)] != 'COMIENDO' and filosofo.estado[self.derecha(i)] != 'COMIENDO':
            filosofo.estado[i]='COMIENDO'
            filosofo.tenedores[i].release()  #SI SUS VECINOS NO ESTAN COMIENDO AUMENTA EL SEMAFORO DEL TENEDOR Y CAMBIA SU ESTADO A COMIENDO

    def tomar(self):
        self.ventana.lista2[self.id].config(bg= "pink")
        filosofo.semaforo.acquire() #SEÑALA QUE TOMARA LOS TENEDORES (EXCLUSION MUTUA)
        filosofo.estado[self.id] = 'HAMBRIENTO'
        self.ventana.lista2[self.id].config(bg= "blue")
        self.verificar(self.id) #VERIFICA SUS VECINOS, SI NO PUEDE COMER NO SE BLOQUEARA EN EL SIGUIENTE ACQUIRE
        filosofo.semaforo.release() #SEÑALA QUE YA DEJO DE INTENTAR TOMAR LOS TENEDORES (CAMBIAR EL ARRAY ESTADO)
        filosofo.tenedores[self.id].acquire() #SOLO SI PODIA TOMARLOS SE BLOQUEARA CON ESTADO COMIENDO

    def soltar(self):
        filosofo.semaforo.acquire() #SEÑALA QUE SOLTARA LOS TENEDORES
        filosofo.estado[self.id] = 'PENSANDO'
        self.ventana.lista2[self.id].config(bg= "white")
        self.verificar(self.izquierda(self.id))
        self.verificar(self.derecha(self.id))
        filosofo.semaforo.release() #YA TERMINO DE MANIPULAR TENEDORES

    def comer(self):
        self.ventana.visualizacion("FILOSOFO {} COMIENDO".format(self.id))
        self.ventana.lista2[self.id].config(bg= "yellow")
        self.ventana.lista3[self.id].config(bg= "green")
        self.ventana.lista3[(self.id+1)%N].config(bg= "green")
        time.sleep(2) #TIEMPO ARBITRARIO PARA COMER
        self.ventana.visualizacion("FILOSOFO {} TERMINO DE COMER".format(self.id))
        self.ventana.lista3[self.id].config(bg= "grey")
        self.ventana.lista3[(self.id+1)%N].config(bg= "grey")
        self.veces+=1
        self.ventana.lista[self.id].delete(0, tk.END)
        self.ventana.lista[self.id].insert(0, self.veces)
        self.ventana.lista2[self.id].config(bg= "light steel blue")

    def run(self):
        for i in range(TIEMPO_TOTAL):
            self.pensar() #EL FILOSOFO PIENSA
            self.tomar() #AGARRA LOS TENEDORES CORRESPONDIENTES
            self.comer() #COME
            self.soltar() #SUELTA LOS TENEDORES

