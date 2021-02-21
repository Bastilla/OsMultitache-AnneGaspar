#Anne Gaspar
#TP5
#2021-02-21

from threading import Thread, Event, Lock
from glob import glob
import time, string

verrou = Lock()
event = Event()
listeCompteur = []
files = glob(r'D:\01_DATA_PERSO\Desktop\TpAnne\*.txt')
print(files)

N_Thread = len(files)

i = 0

def read_file(files,i):
    verrou.acquire()
    #mise en place du verrou pour ne pas lancer des thread en parallele pour la meme action
    with open(files,'r') as f:
        #lecture du fichier texte et comptage des lettres
        d = f.read()
        print("++++++++++++++++++++++++++++++++++++++++++++++")
        print(" lecture du fichier texte : ")
        count = len(d)
        print(d)
        print("          ----------------------              ")
        print(" le fichier texte numero {} contient {} lettres".format(i+1, count))
        print("          ----------------------              ")
        print(" fin de lecture du fichier texte")
        listeCompteur.append(count)
    time.sleep(2)
    verrou.release()

def counter(l):
    verrou.acquire()
    print("++++++++++++++++++++++++++++++++++++++++++++++")
    print("Le nombre total de lettres dans les fichers texte est {} " .format(sum(l)))
    verrou.release()

T1 = [Thread(target=read_file, args=(files[i], i)) for i in range(N_Thread)]
for i in T1:
    i.start()


T2 = Thread(target=counter, args=(listeCompteur,))
T2.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        event.set()
        break
