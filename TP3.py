# Anne GASPAR
#TP3
from threading import Thread, Event, Lock
import queue, time, random

event = Event()
Qe = queue.Queue(5)
lock = Lock()

def ajout_queue(Qe, lock):
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

def supp_queue(Qe, lock):
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

T1 = Thread(target=ajout_queue, args=(Qe,lock)) #thread d ajout
T1.start()
T2 = Thread(target=supp_queue, args=(Qe,lock)) #thread d ajout
T2.start()

while True :
    try :
        print(Qe.queue)
        time.sleep(1)
    except KeyboardInterrupt:
        event.set()
        break



#avec lock pour organiser le passage des threads
