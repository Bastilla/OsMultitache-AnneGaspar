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
dicoRessource['offreclient'] = {}
dicoRessource['offreclient']['client'] = {}
dicoRessource['offreclient']['offre'] = {}
#Dictionnaire pour recap
dicoFinal = {}
#nombre d offre maximum par client
NOffreClient = 3


#Definition des fonctions threads
#la fonction Server
    # creer une ressource qui se place dans le dictionnaire Ressources
    # renvoi le prix le plus eleves parmis les offres proposes et le client associe
    # meurt au bout de d un certaine delai decompteur
def Server(dicoRessource, dicoFinal ):
    print("vous etes dans le server")
    while True:
        # creation d une Ressource
        dicoRessource['nomRessource'] = "ressource"
        dicoRessource['prixbase'] = random.randint(10,20)
        print("ressource cree : {}".format(dicoRessource))

        #on met cette valeur maximale dans le dictionnaire final
        print("Sauvegarde des valeurs finales")
        dicoFinal['nomRessource'] = dicoRessource['nomRessource']
        dicoFinal['prixBase'] = dicoRessource['prixbase']
        dicoFinal['offreclient'] = dicoRessource['offreclient']
        print("dicoFinal : {}".format(dicoFinal))
        break

# la fonction client
    # creation d une offre superieur au prix de base
    # adapter l offre pour qu elle soit superieur aux offres des autres clients
def Client(dicoRessource, NOffreClient):
    print("vous etes dans le client")
    while True:
        if (NOffreClient == 0):
            return dicoRessource
        else:
            NOffreClient -= NOffreClient
            prixOffre = random.randint(5,15)
            #on va verifier le prix de base et si il y a le prix des offres
            # on regarde s il existe une cle offre existante
            if 'offre' in dicoRessource['offreclient']:
                prixRessource = max(dicoRessource['offreclient']['offre'])
            else:
                prixRessource = dicoRessource['prixbase']
            print("prixressou {}".format(prixRessource))
            #prixRessource prend donc la derniere plus grande valeur d offre connu
            #test entre la valeur de dicoRessource et la proposition client
            if prixRessource < prixOffre:
                dicoRessource['offreclient']['client'] = "client"
                prixRessource += prixRessource
                dicoRessource['offreclient']['offre'].append(prixRessource)
                print(" apres test sur prix dico Ressource : {}".format(dicoRessource))
            else:
                dicoRessource['offreclient']['client'] = "client"
                dicoRessource['offreclient']['offre'].append(prixOffre)
            return dicoRessource
            break


#creation thread Server
TServer = Thread(target=Server, args=(dicoRessource, dicoFinal))
#creation thread Client
TClient = Thread(target=Client, args=(dicoRessource, NOffreClient))

#boucle principale d execution
while True:
    try :
        TServer.start()
        time.sleep(0.3)
        TClient.start()
        print("le dictionnaire finale est : {}".format(dicoFinal))
        print("-----------------------------------------------")
        break
    except KeyboardInterrupt:
        event.set()
        break
