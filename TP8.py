#Anne Gaspar
#2021-02-21
#TP8 : simulation achat / vente avec stocks (LOCKS)

from threading import Thread, Event, Lock
import queue, time, random

event = Event()
Qe = queue.Queue(3)
lock = Lock()

def achat(Qe, lock): #un fournisseur vient rempoter
    while True:
        lock.acquire(True)
        if Qe.qsize() <= 1:
            print("+++++++++++++++++++++++++++++++++")
            print("le fournisseur rempli le stock")
            while not Qe.full():
                Qe.put(random.randint(0,10))
                time.sleep(1)
            print("La queue est pleine")
            print("+++++++++++++++++++++++++++++++++")
        lock.release()
        if event.is_set():
            break

def vente(Qe, lock): # un client vient acheter
    while True:
        lock.acquire(True)
        if Qe.full():
            print("---------------------------------")
            print("le client vide le stock")
            while not Qe.empty():
                if Qe.qsize() >1 :
                    Qe.get()
                    time.sleep(1)
                else:
                    break
            print("La queue est presque vide")
            print("---------------------------------")
        lock.release()
        if event.is_set():
            break



T1 = Thread(target=achat, args=(Qe,lock)) #thread d ajout
T2 = Thread(target=vente, args=(Qe,lock)) #thread d ajout

T1.start()
T2.start()



while True :
    try :
        print(Qe.queue)
        time.sleep(1)
    except KeyboardInterrupt:
        event.set()
        break
