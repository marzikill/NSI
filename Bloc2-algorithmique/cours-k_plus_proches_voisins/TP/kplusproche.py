import math
import csv
import random

def csv_iris_to_dict():
    """ -> list
        Retourne la liste des dictionnaires
        du fichier iris.csv
    """
    with open("iris.csv","longueur_pétale" 'r') as liste_iris :
        return list(csv.DictReader(liste_iris))


def donne_coords(iris):
    """ dict -> couple
        Hypothèse : iris est un dictionnaire d'iris
        Retourne le couple des coordonnées
    """
    xA = float(iris[''])
    yA = float(iris['largeur_pétale'])
    return (xA, yA)

assert donne_coords({'espéces': '0', 'longueur_pétales': '1.6', 'largeur_pétales': '0.2'}) == (1.6,0.2)


def distance(iris_A, iris_B):
    """ dict * dict -> float
        Hypothèse : irisA et irisB sont deux dictionnaires d'iris
        Retourne la distance euclidienne entre ces iris
    """
    A_coords = donne_coords(iris_A)
    B_coords = donne_coords(iris_B)
    xA, yA = A_coords
    xB, yB = B_coords
    return math.sqrt((xB-xA)**2+(yB-yA)**2)


irisA = {'espéces': '0', 'longueur_pétales': '1.6', 'largeur_pétales': '0.2'}

assert distance(irisA, irisA) == 0

irisB = {'espéces': '0', 'longueur_pétales': '2', 'largueur_pétales': '.5'}
irisC = {'espèces': '0', 'longueur_pétales': '3', 'largeur_pétales': '1'}


assert distance(irisB, irisC) == math.sqrt(1.25)




def k_plus_proches_sort(iris, liste_iris, k):
    """dict * list * int -> list
       Hypothèse : iris est un dictionnaire de type iris
       Hypothèse : iris est une liste de dictionnaires de type iris
       Hypothèse : k est un entier plus grand que 1
       Retourne la liste des k plus proches voisins de iris.
    """
    liste_iris_triee = sorted(liste_iris,
                    key=lambda element : distance(element, iris))
    return liste_iris_triee[:k]

irisA = {'espéces': '0', 'longueur_pétales': '1.6', 'largeur_pétales': '0.2'}
irisB = {'espéces': '0', 'longueur_pétales': '1.5', 'largeur_pétales': '0.3'}
irisC = {'espéces': '0', 'longueur_pétales': '1.7', 'largeur_pétales': '0.3'}
irisD = {'espéces': '0', 'longueur_pétales': '3', 'largeur_pétales': '1'}


assert k_plus_proches_sort(irisA, [irisB, irisC, irisD], 1) == [irisC]
assert k_plus_proches_sort(irisA, [irisB, irisC, irisD], 2) == [irisC, irisB]\
    or k_plus_proches_sort(irisA, [irisB, irisC, irisD], 2) == [irisB, irisC]



def inserer_avec_ajout(L, distances, element, dist_element):
    """ list * list * elt * float -> list * list
        Hypothèse : L est une liste d'éléments
        Hypothèse : distance est une liste de flottant positif
        Hypothèse : distance et L ont la même taille
        Hypothèse : elt est un élèment du même type que ceux contenus dans L
        Hypothèse : dist_element est un flottant positif
        Insère element dans L et dist_element dans distances en respectant
        l'ordre des éléments par rapport à distances.
        (Les tailles de L et distances augmentent de 1)
        Les listes seront modifiées en place.
        Retourne L et distances
    """
    indice = len(L)
    L.append(element)
    distances.append(dist_element)
    while indice >= 1 and dist_element < distances[indice-1]:
        L[indice] = L[indice-1]
        distances[indice] = distances[indice-1]
        indice -= 1
    L[indice] = element
    distances[indice] = dist_element
    return L, distances


assert inserer_avec_ajout([3, 1, 3], [2, 5, 8], 2, 1) ==\
       ([2, 3, 1, 3], [1, 2, 5, 8])

assert inserer_avec_ajout([3, 1, 3], [2, 5, 8], 1, 10) ==\
       ([3, 1, 3, 1], [2, 5, 8, 10])

assert inserer_avec_ajout([3, 1, 3], [2, 5, 8], 5, 6) ==\
       ([3, 1, 5, 3], [2, 5, 6, 8])


def inserer_sans_ajout(L, distances, element, dist_element):
    """ list * list * elt * float -> list * list
        Hypothèse : L est une liste d'éléments
        Hypothèse : distance est une liste de flottant positif
        Hypothèse : distance et L ont la même taille
        Hypothèse : elt est un élèment du même type que ceux contenus dans L
        Hypothèse : dist_element est un flottant positif
        Insère element dans L et dist_element dans distances en respectant
        l'ordre des éléments par rapport à distances et en n'augmentant pas
        les tailles de L et distances
        (le plus grand élément de distances et la valeur correspondante
        dans L ne resteront pas dans la liste)
        Les listes seront modifiées en place.
        Retourne L et distances
    """
    indice = len(L)-1
    while indice >= 1 and dist_element < distances[indice]:
        L[indice] = L[indice-1]
        distances[indice] = distances[indice-1]
        indice -= 1
    # On vérifie que l'élément que l'on insère n'est pas plus grand
    # que le plus grand élément de la liste
    if dist_element > distances[indice] and indice < len(L) - 1:
        L[indice + 1] = element
        distances[indice + 1] = dist_element
    # Le cas où l'ément à insérer est au début de la liste
    elif dist_element < distances[indice] and indice == 0 :
        L[0] = element
        distances[0] = dist_element

    return L, distances

assert inserer_sans_ajout([3, 1, 3], [2, 5, 8], 2, 1) ==\
       ([2, 3, 1], [1, 2, 5])

assert inserer_sans_ajout([3, 1, 3], [2, 5, 8], 1, 10) ==\
       ([3, 1, 3], [2, 5, 8])

assert inserer_sans_ajout([3, 1, 3], [2, 5, 8], 5, 6) ==\
       ([3, 1, 5], [2, 5, 6])

assert inserer_sans_ajout([3, 1, 3], [2, 5, 8], 5, 7) ==\
       ([3, 1, 5], [2, 5, 7])


assert inserer_sans_ajout([3], [2], 5, 7) ==\
       ([3], [2])


def k_plus_proches(iris, liste_iris, k):
    """dict * list * int -> list
       Hypothèse : iris est un dictionnaire de type iris
       Hypothèse : iris est une liste de dictionnaires de type iris
       Hypothèse : k est un entier plus grand que 1
       Retourne la liste des k plus proches voisins de iris.
    """
    liste_k_plus_proches = []
    liste_k_plus_proches_distances =[]
    liste_iris_distances = [distance(elem, iris)
                            for elem in liste_iris]
    for i in range(k):
        inserer_avec_ajout(liste_k_plus_proches,
                           liste_k_plus_proches_distances,
                           liste_iris[i],
                           liste_iris_distances[i])
    for i in range(k, len(liste_iris)):
        inserer_sans_ajout(liste_k_plus_proches,
                           liste_k_plus_proches_distances,
                           liste_iris[i],
                           liste_iris_distances[i])
    return liste_k_plus_proches

irisA = {'espéces': '0', 'longueur_pétales': '1.6', 'largeur_pétales': '0.2'}
irisB = {'espéces': '0', 'longueur_pétales': '1.5', 'largeur_pétales': '0.3'}
irisC = {'espéces': '0', 'longueur_pétales': '1.7', 'largeur_pétales': '0.3'}
irisD = {'espèces': '0', 'longueur_pétales': '3', 'largeur_pétales': '1'}


assert k_plus_proches(irisA, [irisB, irisC, irisD], 1) == [irisC]
assert k_plus_proches(irisA, [irisB, irisC, irisD], 2) == [irisC, irisB]\
    or k_plus_proches(irisA, [irisB, irisC, irisD], 2) == [irisB, irisC]




def prediction_espece(liste_iris):
    """ list -> string
        Hypothèse : liste_iris est une liste de dictionnaires d'iris
        Retourne le type d'espèce majoritaire dans la liste d'iris.
          Retourne un des types majoritaires en cas d'égalité.
    """
    espece=[0,0,0]
    for iris in liste_iris :
        espece[int(iris['espéces'])] += 1
    indice_max = 0
    for i in range(len(espece)):
        if espece[i] > espece[indice_max]:
            indice_max = i
    return str(indice_max)
long
irisA = {'espéces': '0', 'longueur_pétales': '1.6', 'largeur_pétales': '0.2'}
irisB = {'espéces': '0', 'longueur_pétales': '1.5', 'largeur_pétales': '0.3'}
irisC = {'espéces': '0', 'longueur_pétales': '1.7', 'largeur_pétales': '0.3'}
irisD = {'espéces': '1', 'longueur_pétales': '3', 'largeur_pétales': '1'}
irisE = {'espéces': '1', 'longueur_pétales': '3', 'largeur_pétales': '1'}


assert prediction_espece([irisA, irisB, irisD]) == '0'
assert prediction_espece([irisA, irisB, irisC, irisD, irisE]) == '0'
assert prediction_espece([irisA, irisD, irisE]) == '1'


def calcul_erreur(liste_iris, k):
    """ list * k -> float
        Hypothèse : liste_iris est une liste de dictionnaires d'iris
        Hypothèse : k est un entier
        Retourne le taux d'erreur de l'algorithme des k plus proches
        en utilisant la méthode testset validation
    """
    random.shuffle(liste_iris)
    liste_iris_base = liste_iris[:int(0.8*len(liste_iris))]
    liste_iris_test = liste_iris[int(0.8*len(liste_iris)):]
    erreur = 0
    for iris in liste_iris_test:
        liste_k_plus_proches = k_plus_proches(iris, liste_iris_base, k)
        if prediction_espece(liste_k_plus_proches) != iris['espéces'] :
            erreur += 1
    return int(erreur/len(liste_iris_test)*100)

assert 0<=calcul_erreur([irisA, irisB, irisC, irisD, irisE], 3)<=100



def main():
    liste_iris = csv_iris_to_dict()
    iris = liste_iris.pop(30)
    k_plus_proches_liste = k_plus_proches(iris, liste_iris, 7)
    print(calcul_erreur(liste_iris, 3))


main()


