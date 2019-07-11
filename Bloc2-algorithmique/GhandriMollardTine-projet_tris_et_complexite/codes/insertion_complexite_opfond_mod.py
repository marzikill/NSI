# Créé par mollardb, le 25/06/2019 en Python 3.4
import random
from random import shuffle

random.seed(a=0)

def genere_liste(min, max, N, dup = True):
    # faut pas réver
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
    cpt = 0
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        #décalage des éléments du tableau }
        while j>0 and tableau[j-1]>en_cours:
            tableau[j]=tableau[j-1]
            j = j-1
            cpt+=1
        #on insère l'élément à sa place
        tableau[j]=en_cours
        cpt+=1
    return cpt

#import time
import matplotlib.pyplot as plt

N_list = range(100,2000,10)
#Time_list1 = []
cpt_liste1 = []
print("listes quelconques")
for N in N_list:
    l = genere_liste(0, 2**32, N)
    cpt = tri_insertion(l)
    cpt_liste1.append(cpt)
    print("Taille de liste:", N, ", operations fondamentales:", cpt)
print(len(N_list),len(cpt_liste1))
print(N_list[189])
#print N_list, time_list
plt.xlabel('N')
plt.ylabel('OP')
plt.title("tri insertion: complexité")
plt.plot(N_list, cpt_liste1, 'r^')
plt.grid()
plt.show()