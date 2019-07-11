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
    cpt = 0
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):
        #globale_cpt+=1
        if gauche[index_gauche] <= droite[index_droite]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            resultat.append(droite[index_droite])
            index_droite += 1
        cpt+=1    
    if gauche:
        resultat.extend(gauche[index_gauche:])
        cpt+=1
    if droite:
        resultat.extend(droite[index_droite:])
        cpt+=1
    return cpt
    return resultat

def tri_fusion(m):
    cpt =0
    if len(m) <= 1:
        return m
    milieu = len(m) // 2
    gauche = m[:milieu]
    droite = m[milieu:]
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    cpt += 1
    return cpt
    return list(fusion(gauche, droite)) 
    

#import time
import matplotlib.pyplot as plt

N_list = range(100,2000,10)
#Time_list1 = []
cpt_liste1 = []
print("listes quelconques")
for N in N_list:
    l = genere_liste(0, 2**32, N)
    #cpt = 0
    cpt= tri_fusion(l)
    cpt_liste1.append(cpt)

    print("Taille de liste:", N, ", operations fondamentales:", cpt)
print(len(N_list),len(cpt_liste1))
#print(N_list[189])


#print N_list, time_list
plt.xlabel('N')
plt.ylabel('OP')
plt.title("Tri fusion : opérations fondamentales")
plt.plot(N_list, cpt_liste1, 'r^')
plt.grid()
plt.show()
