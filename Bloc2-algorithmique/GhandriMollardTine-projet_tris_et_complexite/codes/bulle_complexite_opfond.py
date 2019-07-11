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

def tri_bulle(tableau):
    permutation = True
    passage = 0
    cpt = 0
    while permutation == True:
        permutation = False
        passage = passage + 1
        cpt+=1
        for en_cours in range(0, len(tableau) - passage):
            if tableau[en_cours] > tableau[en_cours + 1]:
                permutation = True
                # On echange les deux elements
                tableau[en_cours], tableau[en_cours + 1] = tableau[en_cours + 1],tableau[en_cours]
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
    cpt= tri_bulle(l)
    cpt_liste1.append(cpt)

    print("Taille de liste:", N, ", operations fondamentales:", cpt)
print(len(N_list),len(cpt_liste1))
#print(N_list[189])



#print N_list, time_list

plt.xlabel('N')
plt.ylabel('OP')
plt.title('Tris : nbre de comparaisons')
plt.plot(N_list, cpt_liste1, 'r^')
plt.grid()
plt.show()