# Source d'inspiration : https://python-django.dev/page-apprendre-listes-list-tableaux-tableaux-liste-array-python-cours-debutant

l = [1, 2, 3, 45, 12, 1]

def copier(l):
    # Recopie l dans une nouvelle variable.
    n = len(l)
    t = [0]*n
    for i in range(n):
        t[i] = l[i]
    return t

# Test
print('copier(',l,')=', copier(l))
 
def retourne(l):
    # Recopie l dans une nouvelle variable,
    # dans le sens inverse.
    n = len(l)
    t = [0]*n
    for i in range(n-1, -1, -1):
        t[i] = l[n - i - 1]
    return t

# Test
print('retourne(',l,')', retourne(l))

def sous_tableau(l, i, j):
    # Extrait le sous tableau constitué des éléments
    # d'indice compris entre i et j (exclu) du tableau
    # i, j < len(l) : sinon IndexError
    n = j - i
    t = [0]*n
    for k in range(n):
        t[k] = l[k + i]
    return t

print('sous_tableau(',l,', 2, 4)=', sous_tableau(l, 2, 4))

def concatene(l1, l2):
    # Renvoie le tableau constitué des éléments de la 
    # liste l1 puis des éléments de la liste l2.
    # Marche aussi avec des listes vides (merci Python)
    n1 = len(l1)
    n2 = len(l2)
    t = [0]*(n1 + n2)
    for i in range(n1):
        t[i] = l1[i]
    for j in range(n2):
        t[n1 + j] = l2[j]
    return t

print('concatene(',l,',',l,') =',concatene(l,l))

def applatir(L):
    # L est une liste de liste : applatir(L) renvoie
    # la concaténation de toutes les listes de L
    # Un peu compliqué.... ?
    if L == []:
        return []
    else:
        t = []
        for i in range(len(L)):
            t = concatene(t, L[i])
        return t

print('applatir([[4,5,6,7], [4,1,8,9], [7,8,1]])=',applatir([[4,5,6,7], [4,1,8,9], [7,8,1]]))

def insere(l, i, e):
    # Insère l'élément e à l'indice i dans la liste l.
    # i <= len(l) : sinon IndexError.
    # i = 0 : e inséré en début de liste
    # i = len(l) : e inséré en fin de liste
    avant = sous_tableau(l, 0, i)
    apres = sous_tableau(l, i, len(l))
    return applatir([avant, [e], apres])
    
print('insere([4,5,55,7,6,5,7], 2, 100)=',insere([4,5,55,7,6,5,7], 2, 100))
print('insere([], 0, 100)=',insere([], 0, 100))
print('insere([4,5,55,7,6,5,7], 0, 100)=',insere([4,5,55,7,6,5,7], 0, 100))
print('insere([4,5,55,7,6,5,7], 7, 100)=',insere([4,5,55,7,6,5,7], 7, 100))
    
def rajouter(l, a):
    # Renvoie une copie de la liste l dans laquelle
    # on a rajouté a comme dernier élément.
    n = len(l)
    t = [0]*(n+1)
    for i in range(n):
        t[i] = l[i]
    t[n] = a
    return t

print('rajouter(',l,', 4)=',rajouter(l, 4))

def supprimer_indice(l, k):
    # Renvoie une copie de l dans laquelle l'élément
    # d'indice k a été supprimé.
    # k < len(l) sinon IndexError.
    n = len(l)
    t = [0]*(n-1)
    for i in range(k):
        t[i] = l[i]
    for i in range(k+1, n):
        t[i-1] = l[i]
    return t

print('supprimer_indice(',l,', 2)=', supprimer_indice(l, 2))

def supprimer_indice2(l, k):
    # Renvoie une copie de l dans laquelle l'élément
    # d'indice k a été supprimé.
    # k < len(l) sinon IndexError.
    l1 = sous_tableau(l, 0, k)
    l2 = sous_tableau(l, k+1, len(l))
    return concatene(l1, l2)


def est_dans(l, a):
    # Retourne True si a est dans l, False sinon.
    # Attention à la liste vide !
    if l == []:
        return False
    # On n'a pas besoin de la ligne 100 mais pour les élèves si.
    # (au début du moins)
    else:
        i = 0
        while i < len(l) and l[i] != a:
            i = i + 1
        if i < len(l):
            return True
        else:
            return False

print('est_dans(',l,', 1) = ', est_dans(l, 1))
print('est_dans(',l,', 1564) = ', est_dans(l, 1564))
print('est_dans([], 3) =', est_dans([], 3))


def premier_indice(l,a):
    # Renvoie le premier indice pour lequel l[i] = a
    # Renvoie False si a n'est pas présent dans la liste
    compteur = 0
    # Ne fonctionne pas !!
    # while (l[compteur] != a) and (compteur < len(l)):
    # Fonctionne grâce à l'évaluation paresseuse !!
    while (compteur < len(l)) and (l[compteur] != a):
        compteur = compteur + 1
    if compteur < len(l):
        return compteur
    else:
        return False

print('premier_indice(',l,', 4)', premier_indice(l, 4))

# Autre méthode : (moins bien pour les élèves je pense : une boucle for
# c'est quand on parcourt tous les éléments de la liste)
def premier_indice2(l,a):
    # Renvoie le premier indice pour lequel l[i] = a
    # Renvoie False si a n'est pas présent dans la liste
    # Utilisation avancée : pas demamdée aux élèves.
    for i in range(len(l)):
        if (l[i] == a):
            return i
    return False

print('premier_indice2(',l, ', 3)=', premier_indice2(l, 3))

def tous_indices(l, e)
    indices = []
    for i in range(l):
        if l[i] == e:
            indices = rajouter(indices, i)
    return indices

def nombre_occurence(l, a):
    # Compte le nombre d'occurence de l'élément a
    # dans la liste l
    nb = 0
    for i in range(len(l)):
        if (l[i] == a):
            nb = nb+1
    return nb

print("nombre_occurence(",l,", 1)=",nombre_occurence(l, 1))

def est_dans2(l, a):
    return (nombre_occurence(l, a) > 0)

print('est_dans2(',l,', 1) = ', est_dans2(l, 1))
print('est_dans2(',l,', 1564) = ', est_dans2(l, 1564))
print('est_dans2([], 3) =', est_dans2([], 3))


def supprimer_element(l, a):
    # Supprime l'élément a de la liste l
    # Renvoie False si a n'appartient pas à l
    if est_dans(l, a):
        indice_a = premier_indice(l, a)
        return supprimer_indice(l, indice_a)
    else:
        return False

print("supprimer_element(", l,", 1) = ", supprimer_element(l, 1))

def sans_doublons(l):
    # Renvoie une copie du tableau l
    # dans laquelle chacun des éléments de l
    # n'apparait qu'une seule fois.
    t = []
    for i in range(len(l)):
        if not est_dans(t, l[i]):
           t = rajouter(t, l[i]) 
           # Ou rajouter(t, l[i]) ? Je ne sais pas 
           # quelle est la version la plus claire.
           # Je préfère t = rajouter(t, l[i]) : ils font déjà
           # n'importe quoi avec les appels de fonction.
    # Autre méthode : itérer sur les éléments
    # for e in l:
        # if not est_dans(t, e):
            # t = rajouter(t, e)
    return t

print('sans_doublons([4,4,4,4,45,5,8,5,65,4,1,1,5]) = ', sans_doublons([4,4,4,4,45,5,8,5,65,4,1,1,5]))

# Opérations sur les listes booléennes.
def tout_vrai(l):
    # Renvoie True ssi tous les éléments de l sont True, 
    # False sinon.
    # Par convention : tout_vrai([]) = True
    compteur = 0
    que_vrai = True
    while compteur < len(l) and que_vrai:
        que_vrai = que_vrai and l[compteur]
        compteur = compteur + 1
    return que_vrai

print('tout_vrai([True, True, True, True])=', tout_vrai([True, True, True, True]))
print('tout_vrai([True, False, True, True])=',tout_vrai([True, False, True, True]))


# On appelle "ensemble" un tableau sans doublons.
# L'ordre des éléments dans un tableau n'est pas important.
def est_sous_ensemble(A, B):
    # A et B sont deux ensembles
    # Renvoie True si tous les éléments de A sont 
    # des éléments de B
    compteur = 0
    est_sous_ens = True
    while compteur < len(A) and est_sous_ens:
        est_sous_ens = est_sous_ens and est_dans(B, A[compteur])
        compteur = compteur + 1
    return est_sous_ens

print('est_sous_ensemble([75, 1, 0], [1,2,8,4,5,75,6,0])=',est_sous_ensemble([75, 1, 0], [1,2,8,4,5,75,6,0]))
print('est_sous_ensemble([75, 1, -1], [1,2,8,4,5,75,6,0])=',est_sous_ensemble([75, 1, -1], [1,2,8,4,5,75,6,0]))
print('est_sous_ensemble([], [1,2,8,4,5,75,6,0])=',est_sous_ensemble([], [1,2,8,4,5,75,6,0]))
print('est_sous_ensemble([], [])=',est_sous_ensemble([], []))
print('est_sous_ensemble([75, 1, -1], [])=',est_sous_ensemble([75, 1, -1], []))

def sont_egaux(A, B):
    # A et B sont deux ensembles
    # Renvoie True ssi tous les éléments de A sont des éléments de B
    # et si tous les éléments de B sont des éléments de A.
    return est_sous_ensemble(A, B) and est_sous_ensemble(B, A)

def sont_egaux2(A, B):
    # A et B sont deux ensembles
    # Renvoie True ssi tous les éléments de A sont des éléments de B
    # et si tous les éléments de B sont des éléments de A.
    return est_sous_ensemble(A, B) and len(A) == len(B)

def intersection(A, B):
    # A et B sont deux ensembles. 
    # Renvoie l'ensemble constitué des éléments présents à la fois 
    # dans A et dans B
    inter = []
    for i in range(len(A)):
        if est_dans(B, A[i]):
            inter = rajouter(inter, A[i])
    return inter

print('intersection([0,1,2,7,6,4], [7,0,2,10, 35])=',intersection([0,1,2,7,6,4], [7,0,2,10, 35]))
print('intersection([], [7,0,2,10, 35])=',intersection([], [7,0,2,10, 35]))
print('intersection([0,1,2,7,6,4], [])=',intersection([0,1,2,7,6,4], []))

def union(A, B):
    # A et B sont deux ensembles.
    # Renvoie l'ensemble constitué des éléments présents soit dans A
    # soit dans B
    return sans_doublons(concatene(A, B))

print('union([1,2,8,5,6], [1,3,5,78,6,0])=',union([1,2,8,5,6], [1,3,5,78,6,0]))

def difference(A, B):
    # A et B sont deux ensembles. 
    # Renvoie l'ensemble constitué des éléments de B qui ne
    # sont pas des éléments de A
    dif = []
    for i in range(len(B)):
        if not est_dans(A, B[i]):
            dif = rajouter(dif, B[i])
    return dif

print('difference([1,2,5,7,123], [2,5,41,325,74, 30])=',difference([1,2,5,7,123], [2,5,41,325,74, 30]))

def ne_fait_rien(A, B):
    # A et B sont deux ensembles.
    C = intersection(A, B)
    D = difference(A, B)
    E = union(C, D)
    return E

# Que fait la fonction ne_fait_rien ? Pouvez vous le prouver ?
print('ne_fait_rien([1,2,5,7,123], [2,5,41,325,74, 30])=',ne_fait_rien([1,2,5,7,123], [2,5,41,325,74, 30]))

def minimum(l):
    # Retourne le minimum de la liste l
    # Renvoie False si l = []
    if l == []:
        return False
    else:
        mini = l[0]
        mini_index = 0
        for i in range(len(l)):
            if l[i] < mini:
                mini = l[i]
                mini_index = i
        return mini, mini_index

print('minimum([4,5,7,2,0,9,-1,66,8])=', minimum([4,5,7,2,0,9,-1,66,8]))

def maximum(l):
    # Retourne le maximum de la liste l
    # ainsi que l'indice où est atteint le maximum.
    # Renvoie False si l = []
    if l == []:
        return False
    else:
        maxi = l[0]
        maxi_index = 0
        for i in range(len(l)):
            if l[i] > maxi:
                maxi = l[i]
                maxi_index = i
        return maxi, maxi_index

print('maximum([4,5,7,2,0,9,-1,66,8])=', maximum([4,5,7,2,0,9,-1,66,8]))

def total(l):
    # Renvoie la somme de tous les élément de l
    panier = 0
    for i in range(len(l)):
        panier = panier + l[i]
    # Ou encore
    # for e in l:
        # panier = panier + e
    return panier

print('total(range(11))=',total(range(11)))

def moyenne(valeurs, coefficients):
    # valeurs et coefficients sont deux tableaux de même taille
    # Renvoie la moyenne des valeurs affectées des coefficients correspondants
    panier = 0
    for i in range(len(valeurs)):
        panier = panier + valeurs[i]*coefficients[i]
    return panier/total(coefficients)

print('moyenne([10, 12, 15, 8], [8, 8, 1, 4])=',moyenne([10, 12, 15, 8], [8, 8, 1, 4]))
