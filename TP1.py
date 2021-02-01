#Anne GASPAR
#Tp1 en python

import time, random, threading
N = int(input('Donner une valeur pour N ')) #role ajout
N2 = int(input('Donner une valeur pour N2 ')) #role sup

def creationlist(): # creation de la fonction parametrant la liste sur laquelle nous allons travailler
    liste = []
    for i in range(10):
        liste.append(random.randint(0, 100)) # on remplit la liste de dix parametre aleatoirement choisi entre 0 et 100
    return liste


class addThread(threading.Thread): # creation de la classe ajout elements
    def __init__(self, name, liste):
        super().__init__()
        self.liste = liste
        self.name = name
    def run(self): # definiton de la fonction d execution
        self.liste.append(random.randint(0, 100))
        print(self.liste)

class supThread(threading.Thread):# creation de la classe suppression elements
    def __init__(self, name, liste):
        super().__init__()
        self.name = name
        self.liste = liste
    def run(self):
        self.liste.pop() #suppression de l element du dernier index
        print(self.liste)

# creation de la liste L
L = creationlist()
print(L)

T = [addThread('{}'.format(i), L) for i in range(N)]
T2 = [supThread('{}'.format(i), L) for i in range(N2)]
print(T)

for i,j in zip(T,T2):
    i.start()
    j.start()
    time.sleep(0.5)

# le probleme ici est que le programme s execute et que nos thread dit de suppression essayent de
#supprimer des elements de la liste qui elle est vide et donc ne possede pas d element a supprimer
