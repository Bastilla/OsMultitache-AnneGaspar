#TP4
#Anne GASPAR
import queue
import random
import time
from threading import Event


from threading import Thread, Lock

N=int(input("Donner un nombre de thread : "))
Qe = queue.Queue(5)
lock = Lock()

def producteur(Qe, lock):
    while True:
        lock.acquire(True)
        # if not Qe.full():
        if Qe.empty():
            while not Qe.full():
                Qe.put(random.randint(0,10))
                time.sleep(1)
            #print(list(Qe.queue))
            print("queue pleine")
        lock.release()
        if event.is_set():
            break

def consommateur(Qe, lock):
    while True:
        lock.acquire(True)
        if Qe.full():
            while not Qe.empty():
                Qe.get()
                time.sleep(1)
            #print(list(Qe.queue))
            print("queue vide")
        lock.release()
        if event.is_set():
            break
for i in range(0,N):
    T1 = Thread(target=producteur, args=(Qe,lock)) #thread d ajout
    T1.start()
    T2 = Thread(target=consommateur, args=(Qe,lock)) #thread d ajout
    T2.start()


while True :
    try :
        print(Qe.queue)
        time.sleep(1)
    except KeyboardInterrupt:
        event.set()
        break
