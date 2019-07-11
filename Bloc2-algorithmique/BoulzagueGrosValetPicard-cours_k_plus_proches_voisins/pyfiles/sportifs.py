# Fichier de cours pour l'exercice sur les sportifs. 
# J'ai repris le fichier kNN.py en l'adaptant pour le problème. 

from math import *
import numpy as np
import matplotlib.pyplot as plt

# Fonctions persos
def select(t, e):
    # t est un tableau et e un élément
    # renvoie les indices des éléments de t qui sont égaux à e
    return [ i for i in range(len(t)) if t[i] == e ]
def extract(t, l):
    # t est un tableau et l une liste d'indices,
    # renvoie le tableau constitué des éléments de t
    # d'indices présents dans l
    return [ t[i] for i in l ]
def tri_avec_indices(l):
    # On trie (selection parce que la flemme de faire dans la 
    # dentelle) le tableau l en conservant en mémoire 
    # la trace des permutations effectuées.
    permutation = list(range(len(l)))
    for i in range(len(l)):
        currentmin = l[i]
        indexmin = i
        for j in range(i, len(l)):
            if l[j] < currentmin:
                currentmin = l[j]
                indexmin = j
        l[i], l[indexmin] = currentmin, l[i]
        permutation[i], permutation[indexmin] = permutation[indexmin], permutation[i]
    return permutation, l

# Test
# l = [5, 7, 2, 6, 0, 7]
# print(tri_avec_indices(l))

def dict_max(d):
    # Trouve la valeur maximale dans un dictionnaire
    # et renvoie cette valeur ainsi que la clé associée
    cles = list(d.keys())
    clemax = cles[0]
    maximum = d[cles[0]]
    for cle in cles:
        if d[cle] > maximum:
            clemax = cle
            maximum = d[cle]
    return clemax, maximum

# d = {'S': 5, 'PS': -5, 'T':8}
# print(dict_max(d))


# Si c'était à refaire... Meilleure structure de données ?
# banque = {'S':[[50, 48], [45, 30], [60, 24]], 'PS': [[40, 36], [30,96], [18, 24]]}
# categories = banque.keys()
# clients = banque['S'] + banque['PS']
# clients_safe = banque['S']
# clients_notsafe = banque['PS']
# etiquettes = ['S']*len(clients_safe) + ['PS']*len(clients_notsafe)
# Pas sûr que ça soit plus simple...


# Distances entre deux points (en dimension N)
def euclidienne(A, B):
    assert len(A) == len(B)
    # Le zip n'est pas obligatoire. On peut aussi utiliser :
    # sqrt(sum([(a[i] - b[i])**2 for i in range(len(A))]))
    return sqrt(sum([(ai - bi)**2 for (ai, bi) in zip(A, B)]))

# Test
# A = (0, 0)
# B = (1, 1)
# print(euclidienne(A, B))
# print(sqrt(2))

def hamming(A, B):
    assert len(A) == len(B)
    return sum([1 for (ai, bi) in zip(A, B) if ai != bi])

# Test
# A = (0, 0, 0, 1, 1, 1, 1)
# B = (1, 1, 0, 1, 0, 1, 1)
# print(hamming(A, B))
# Ne semble pas très utile pour ces données ? (pb d'échelle)

def manhattan(A, B):
    assert len(A) == len(B)
    return sum([abs(ai - bi) for (ai, bi) in zip(A, B)])

# Test
# A = (0, 0)
# B = (1, 1)
# print(manhattan(A, B))

def infinie(A, B):
    assert len(A) == len(B)
    return max([abs(ai - bi) for (ai, bi) in zip(A, B)])

def circle_param(center, r, distance):
    # Cercle de rayon r (en dimension 2) associé à une distance.
    # Renvoie une paramétrisiation du cercle de centre
    # centre, de rayon r associé distance.
    # On peut surement faire plus estéthique.
    param = np.arange(0, 2*np.pi, 0.01)
    x = np.cos(param)
    y = np.sin(param)
    norm = [ distance([x[i], y[i]], [0, 0]) for i in range(len(x))]
    # x = [ center[0] + x[i]/norm[i] for i in range(len(x))]
    # y = [ center[1] + y[i]/norm[i] for i in range(len(y))]
    return [ center[0] + r*x[i]/norm[i] for i in range(len(x))],[ center[1] + r*y[i]/norm[i] for i in range(len(y))]

def kNN(data, etiquettes, categories, k, client, distance):
    # On calcule les distances du nouveau client par rapport à ceux
    # de notre base de données
    tableau_distance = [distance(client, di) for di in data]
    # On trie les distances en conservant en mémoire à quel client
    # de la base de donnée cela correspond.
    indices, distances_triees = tri_avec_indices(tableau_distance)
    # les clients de la base de donnée qui sont à une distance inférieure
    # à radius sont pris en compte comme plus proches voisins.
    radius = distances_triees[k - 1]
    # Chacun des voisins vote en incrémentant son classificateur.
    vote = { cat:0 for cat in categories}
    print("Les coordonnées du client sont :", client)
    print("Les", k, "plus proches voisins sont :")
    for i in range(k):
        vote[etiquettes[indices[i]]] += 1
        print(data[indices[i]])
    # On récupère le vote majoritaire parmis les voisins.
    clemax, maximum = dict_max(vote)
    print("Le nouveau client est étiquetté :", clemax, "(votes :", vote, ")")
    return radius



x = [ 9.7, 9.85, 9.9, 10, 10.1, 10.1 ,10.2, 10.2, 10.3, 10.5, 10.8, 11]
y = [ 23, 26, 18, 15, 25, 31, 16, 33, 28, 32, 39, 34 ]
etiquettes =  ["S", "S", "S", "S", "S", "PS", "S", "PS", "PS", "PS", "PS", "PS"]
tout = list(zip(x, y, etiquettes))
data = list(zip(x, y))

# Exécution de l'algorithme
categories = ["S", "PS"]
k = 3
client = [ 10, 30 ]
distance_selectionnee = euclidienne
radius = kNN(data, etiquettes, categories, k, client, distance_selectionnee)
xcircle, ycircle = circle_param(client, radius*1.05, distance_selectionnee) 


plt.scatter(extract(x, select(etiquettes, "S")), extract(y, select(etiquettes, "S")), color="green", label="Sportifis")
plt.scatter(extract(x, select(etiquettes, "PS")), extract(y, select(etiquettes, "PS")), color="blue", label="Non sportif")
plt.scatter(client[0], client[1], color="black", label="À classifier")

plt.plot(xcircle,ycircle)
# plt.title("Résultats des prélèvements sur le terrain.")
plt.xlim(min(x)*0.95, max(x)*1.05)
plt.ylim(min(y)*0.95, max(y)*1.05)
plt.legend()
plt.show()
