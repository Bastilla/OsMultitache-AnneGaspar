#Anne GASPAR
# Projet 5 : simulation d enchere bourse

#importation des librairies
import random
import time
from threading import Thread, Lock, Event
import operator

#Initialisation
#creation dictionnaire
dicoRessource = {}
#Dictionnaire pour recap
dicoFinal = {}
#creation des verrou
lockOffer = Lock()
#variable pour duree de vie du thread server
decompteur = 10
#variable pour le nombre de thread Server
NS = 5
#variable pour le nombre de thread client
NC = 3
#nombre d offre maximum par client
NOffreClient = 3

#Definition des fonctions threads

#la fonction Server
    # creer une ressource qui se place dans le dictionnaire Ressources
    # renvoi le prix le plus eleves parmis les offres proposes et le client associe
    # meurt au bout de d un certaine delai decompteur
def Server(index, dicoRessource):
    while True:
        print ("thread server numero {}".format(index))
        # creation d une Ressource
        dicoRessource["nomRessource"] = "ressource{}".format(index)
        dicoRessource["prixbase"] = random.randint(10,20)
        print("ressource cree : {}".format(dicoRessource))
        # cas ou le decompteur est egale a 0
        #destruction du server
        #on va ici faire nos differente action du Server
        #intteroger le dictionnaire pour trouver l offre client la plus haute
        offreMax = max(dicoRessource.iteritems(), key=operator.itemgetter("offre"))
        print(" offre max : {}".format(offreMax))
        clientMax = max(dicoRessource.iteritems(), key=operator.itemgetter("client"))
        print(" client de l offre max : {}".format(clientMax))
        # on recupere la valeur maximale ansi que le nom du client qui l a donne
        #on met cette valeur maximale dans le dictionnaire final
        print("Sauvegarde des valeurs finales")
        dicoFinal["nomRessource"] = dicoRessource["nomRessource"]
        dicoFinal["prixBase"] = dicoRessource["prixbase"]
        dicoFinal["nomClient"] = clientMax
        dicoFinal["prix soumis"] = offreMax
        print("dicoFinal : {}".format(dicoFinal))
        break

# la fonction client
    # creation d une offre superieur au prix de base
    # adapter l offre pour qu elle soit superieur aux offres des autres clients
def Client(index, dicoRessource, NOffreClient):
    print("creation client numero : {}".format(index))
    while NOffreClient != 0:
        #mise en place du verrou pour qu un seul client puisse deposer une offre
        lockOffer.acquire(True)
        prixOffre = random.randint(5,15)
        #on va verifier le prix de base et si il y a le prix des offres
        # on regarde s il existe une cle offre existante
        if ("offre" in dicoRessource):
            prixRessource = max(dicoRessource.iteritems(), key=operator.itemgetter("offre"))
        else:
            prixRessource = dicoRessource["prixbase"]
        #prixRessource prend donc la derniere plus grande valeur d offre connu
        #test entre la valeur de dicoRessource et la proposition client
        if (prixRessource < prixOffre):
            dicoRessource["client"] = "client{}".format(index)
            dicoRessource["offre"] += prixRessource
            print(" apres test sur prix dico Ressource : {}".format(dicoRessource))
            return dicoRessource
        else:
            dicoRessource["client"] = "client{}".format(index)
            dicoRessource["offre"] = prixOffre
            return dicoRessource
        NOffreClient -= NOffreClient
        lockOffer.release()


#creation de NS thread Server
for i in range(1,NS+1):
    TServer = Thread(target=Server, args=(i,dicoRessource, decompteur))
    if (decompteur != 0) :
        TServer.start()
    else:
        TServer.stop()

#creation de NC thread Client
for i in range(1,NC+1):
    TClient = Thread(target=Client, args=(i, dicoRessource, NOffreClient))
    TClient.start()


#boucle principale d execution
while True:
    try :
        print(dicoFinal)
        time.sleep(1)
    except KeyboardInterrupt:
        event.set()
        break
