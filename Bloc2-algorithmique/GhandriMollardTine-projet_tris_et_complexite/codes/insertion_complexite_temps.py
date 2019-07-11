# Créé par mollardb, le 25/06/2019 en Python 3.4
import random
from random import shuffle

random.seed(a=0)

def genere_liste(min, max, N, dup = True):
    # faut pas rÃªver
    if not dup and N > max - min + 1 :
        N = max - min + 1

    liste = []
    while len(liste) < N:
        curr = random.randint(min, max)
        if (not curr in liste) or dup:
            liste.append(curr)
    return liste

liste = genere_liste(0, 100, 30, True)

listeTriee = sorted(liste)

listeTrieeInv = sorted(liste, reverse = True)

listepermu = liste[:]
shuffle(listepermu)

def declasser_listeTriee(listeTriee, M):
    l = listeTriee[:]
    for _ in range(M):
        i = random.randint(0, len(l)-1)
        j = random.randint(0, len(l)-1)
        l[i], l[j] = l[j], l[i]
    return l

def tri_insertion(tableau):
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        #dÃ©calage des Ã©lÃ©ments du tableau }
        while j>0 and tableau[j-1]>en_cours:
            tableau[j]=tableau[j-1]
            j = j-1
        #on insÃ¨re l'Ã©lÃ©ment Ã  sa place
        tableau[j]=en_cours

import time
import matplotlib.pyplot as plt

N_list = range(100,2000,10)
Time_list1 = []
print("listes quelconques")
for N in N_list:
    l = genere_liste(0,2**32, N)

    ti = time.clock()
    tri_insertion(l)
    ts = time.clock()

    print("Taille de liste:", N, ", temps de calcul:",ts - ti)
    Time_list1.append(ts - ti)

#print N_list, time_list
plt.xlabel('N')
plt.ylabel('T')
plt.plot(N_list, Time_list1,'r^')
plt.show()

