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

def fusion(gauche,droite):
    resultat = []
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):
        if gauche[index_gauche] <= droite[index_droite]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            resultat.append(droite[index_droite])
            index_droite += 1
    if gauche:
        resultat.extend(gauche[index_gauche:])
    if droite:
        resultat.extend(droite[index_droite:])
    return resultat

def tri_fusion(m):
    if len(m) <= 1:
        return m
    milieu = len(m) // 2
    gauche = m[:milieu]
    droite = m[milieu:]
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    return list(fusion(gauche, droite))



import time
import matplotlib.pyplot as plt

N_list = range(100,2000,10)
Time_list1 = []

print("listes quelconques")
for N in N_list:
    l = genere_liste(0, 2**32, N)

    ti = time.clock()
    tri_fusion(l)
    ts = time.clock()

    print("Taille de liste:", N, ", temps de calcul:", ts - ti)
    Time_list1.append(ts - ti)

#print N_list, time_list
plt.xlabel('N')
plt.ylabel('T')
plt.title("complexite temps tri fusion")
plt.plot(N_list, Time_list1, 'r^')
plt.grid()
plt.show()