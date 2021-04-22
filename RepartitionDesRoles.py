import random, os
import time as tm
from math import *
# Les variables numériques
Nbr_Diapos = 0
Nbr_Eleves_par_diapo = 0 
# Les listes
Liste_Eleves = []
Repartition = []
# --------------------------------------------------------------------------------------- DEF

def renit():
    # Les variables numériques
    Nbr_Diapos = 0
    Nbr_Eleves_par_diapo = 0
    # Les listes
    Liste_Eleves = []

def RandomEleve(Liste_Eleves):
    r = random.randint(0, len(Liste_Eleves)-1)
    return Liste_Eleves[r]

def NbrRecurenceNom(Liste, ItemAChercher):
    c = 0
    # print(Liste, ItemAChercher)
    for i in range(len(Liste)):
        if Liste[i] == ItemAChercher:
            #print("Trouver : ", ItemAChercher)
            c += 1
            #print(c)    
    return c

def Rep_SansLim(Liste_Eleves, Nbr_Diapos):
    Repartition = []
    #print("Liste_Eleves :", Liste_Eleves, "\nNbr_Diapos :", Nbr_Diapos)
    for i in range(Nbr_Diapos):
        r = random.randint(0, len(Liste_Eleves)-1)
        Repartition.append(Liste_Eleves[r])
    os.system("cls")
    print("Generation de la liste ... ")
    tm.sleep(5)
    return Repartition

def Rep_AvecLim(Liste_Eleves, Nbr_Diapos, Nbr_Eleves_par_diapo):
    Repartition = []
    #print("Liste_Eleves :", Liste_Eleves, "\nNbr_Diapos :", Nbr_Diapos, "\nNbr_Eleves_par_diapo", Nbr_Eleves_par_diapo)
    while len(Repartition) != Nbr_Diapos:
        eleve = RandomEleve(Liste_Eleves)
        recurenceEleve = NbrRecurenceNom(Repartition, eleve)

        if int(recurenceEleve) >= int(Nbr_Eleves_par_diapo):
            pass
        elif len(Repartition) > 0 and Repartition[len(Repartition)-1] == eleve:
            pass
        else: 
            Repartition.append(eleve)
        print("A")
    os.system("cls")
    print("Generation de la liste ... ")
    tm.sleep(5) 
    return Repartition

def MiseEnPageDeLaListe(Liste, eleve):
    print("|| ============================================================== ||")
    print("|| Copier Coller la liste dans un channel discord de vôtre groupe ||")
    print("|| ============================================================== ||\n")    
    for i in range(len(Liste)):
        if i > 9: print("__Diapo__ **", i+1, "** :", Liste[i])
        else:     print("__Diapo__ **", i+1, "** :", Liste[i])
    compteur = []
    for i in range(len(eleve)):
        if eleve[i] in Liste:
            n = NbrRecurenceNom(Liste, eleve[i])
            compteur.append(n)
            compteur.append(eleve[i])
    print("|| ============================================================== ||")
    print("|| Nombre de diapo par personne :                                 ||")    
    a = [ print("||", compteur[i],":",compteur[i+1]) for i in range(0, len(compteur), 2) ]
    print("|| ============================================================== ||")
    # Ajouter les fréquence d'apparition des personnes dans le groupe

def RemplissageListeEleve(Nbr_Eleves_par_diapo):
    Liste = []
    os.system("cls")
    print("||                                  ENTREZ LES PARTICIPANTS                              ||")
    nom = ""
    # Renssignement des participants
    if Nbr_Eleves_par_diapo > 0:
        print("||", Nbr_Pers_Groupe, ": Nombre de personnes dans le groupe                              ||")
    print("|| ===================================================================================== ||")
    print("|| Entrez le nom des élèves. Puis tapez 'fin' pour confirmer la fin de l'enregistrement. ||")
    print("|| ===================================================================================== ||")
    while nom != "fin":
        nom = input("--> ")
        Liste.append(nom)
    del Liste[len(Liste)-1]
    os.system("cls")
    return Liste

# --------------------------------------------------------------------------------------- Boucle

while True:
    os.system("cls")
    print("|| == Répartition des rôles == ||")
    renit()
    Nbr_Diapos = int(input("|| Nombre de diapo.\n**> "))
    os.system("cls")
    print(Nbr_Diapos, ": Nombre de diapos")
    choix = 0

    while choix == 0:
        os.system("cls")
        print("|| == Répartition des rôles == ||")
        choix = int(input("|| Avec ou sans limite de diapo par personnes ? 1 = Oui 2 = Non ?\n**> "))

        if choix == 1:
            os.system("cls")
            print("|| ==== Répartition des rôles ==== ||")
            print("||", Nbr_Diapos, "diapos")
            print("|| Avec limite de diapos           ||")
            print("|| 1 ============================= ||")
            Nbr_Pers_Groupe = int(input("|| Nombre de personnes dans le groupe\n**> "))
            print("|| Le nombre minimum de diapo par personnes es de :", ceil(round((Nbr_Diapos/Nbr_Pers_Groupe),1)))
            print("|| 2 ======================= ||")
            Nbr_Eleves_par_diapo = int(input("|| Nombre de personne par diapo \n**> "))
            os.system("cls")
            while len(Liste_Eleves) != int(Nbr_Pers_Groupe):
                Liste_Eleves = RemplissageListeEleve(Nbr_Eleves_par_diapo)
            print("Enregistrement de vôtre demande ...")
            tm.sleep(1)

        if choix == 2:
            os.system("cls")
            print("|| ====== Répartition des rôles ====== ||")
            print("||",Nbr_Diapos, "Nombre de diapos")
            print("|| Sans limite de diapos               ||")
            Nbr_Eleves_par_diapo = 0
            Liste_Eleves = RemplissageListeEleve(Nbr_Eleves_par_diapo)
            print("Enregistrement de vôtre demande ...")
            tm.sleep(3)

    # Génération de la répartition selon les paramètres entrés
    if Nbr_Eleves_par_diapo == 0:
        os.system("cls")
        print("|| ======================================== ||")
        print("|| Calcule de la répartition SANS limite... ||")
        print("|| ======================================== ||")
        ListeRoles = Rep_SansLim(Liste_Eleves, Nbr_Diapos)
        tm.sleep(2)
    else:
        os.system("cls")
        print("|| ======================================== ||")
        print("|| Calcule de la répartition AVEC limite... ||")
        print("|| ======================================== ||")
        ListeRoles = Rep_AvecLim(Liste_Eleves, Nbr_Diapos, Nbr_Eleves_par_diapo)
        tm.sleep(2)
    

    # print("ListeRoles :\n", ListeRoles)
    print("|| ================================== ||")
    print("|| Compilation de la mise en page ... ||")
    print("|| ================================== ||")
    tm.sleep(2)
    os.system("cls")
    MiseEnPageDeLaListe(ListeRoles, Liste_Eleves)
    print("|| Le programme vas se fermer dans 2 minutes ||\n|| Pour refaire une répartition relancer le programme ||")
    print("|| ============================================================== ||")
    tm.sleep(120)