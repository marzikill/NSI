# -*- coding: utf-8 -*-

""" Correction du TP listes """

# Exercice 1

def moyenne(l):
	somme = 0
	for i in range (0,len(l)):
		somme = somme + l[i]
	return somme/len(l)

# Test qui ne tombe pas sur un entier (pour vérifier que la moyenne n'est pas tronquée)
#print(moyenne([2,5,-4,2]))


# Exercice 2

def contient(l,x):
    for i in range (0,len(l)):
        if l[i] == x :
            return True
    return False

# Tests où l'élément n'est pas présent, est en 1ere place, est en dernière place
#print(contient([-4,7,46,-17],10))
#print(contient([-4,7,46,-17],-4))
#print(contient([-4,7,46,-17],-17))

def premierIndice(l,x):
	for i in range (0,len(l)):
		if l[i] == x:
			return i
	return False

# Tests où l'élément est présent plusieurs fois, ou n'est pas présent
#print(premierIndice([3,7,-4,7,9],7))
#print(premierIndice([3,7,-4,7,9],0))

def dernierIndice(l,x):
    indice = False
    for i in range (0,len(l)):
        if l[i] == x:
            indice = i
    return indice

#print(dernierIndice([3,7,-4,7,9],7))
#print(dernierIndice([3,7,-4,7,9],0))

def nbOccurrences(l,x):
    nb = 0
    for i in range (0,len(l)):
        if l[i] == x:
            nb = nb+1
    return nb

#print(nbOccurrences([3,7,-4,7,9,7,7],7))
#print(nbOccurrences([3,7,-4,7,9],0))


# Exercice 3

def maximum(l,x):
    max = l[0]
    for i in range (1,len(l)):
        if l[i] > max:
            max = l[i]
    return max

# Test où tous les nombres sont négatifs (pour éviter l'erreur de l'initialisation du max à 0)
# De plus tests où le maximum est en 1ere / dernière place (cas limites)
#print(max([-3,-7,-4,-7,-9]))
#print(max([3,7,4,7,9]))


# Exercice 4

def testTri(l):
    for i in range(1,len(l)):
        if l[i-1] > l[i]:
            return False
    return True

# Tests d'une liste triée et de listes presque triées sauf au début / à la fin
#print(testTri([-4,2,3,4,16]))
#print(testTri([2,1,3,4,6]))
#print(testTri([2,3,5,9,6]))


# Exercice 5

def dichotomie(t,v):
    p = 0
    g = len(t)-1
    while p <= g: # quand p = g c'est qu'il y a une case, et il faut alors continuer pour regarder si ce qu'on cherche se trouve dans la case !
        m = (p+g) // 2
        if t[m] == v:
            return m
        elif t[m] < v:
            p = m+1 # Ici le +1 évite que p reste le même (ce qui conduirait à boucle infinie)
        else:
            g = m-1 # Ici le -1 évite que g reste le même (ce qui conduirait à boucle infinie)
    return False

# Tests où l'élément n'est pas présent, est en 1ere place, est en dernière place, est en plein milieu
#print(dichotomie([1,3,5,6,9,12,14],10))
#print(dichotomie([1,3,5,6,9,12,14],1))
#print(dichotomie([1,3,5,6,9,12,14],14))
#print(dichotomie([1,3,5,6,9,12,14],6))


# Exercice 6

def liste():
    n = int(input("Entrer la taille de la liste : "))
    l = []
    for i in range(1,n+1):
        print("Entrer l'entier numéro ",i)
        k = int(input())
        l.append(k)
    return l

#print(liste())

def inverse(l):
    l2 = []
    n = len(l)    
    for i in range(0,n):
        l2.append(l[n-1-i])
    return l2

#print(inverse([1,2,7,5]))

# correction dernière question:
#print(inverse(liste()))


# Exercice 7

def fusion(t1,t2):
    l1,l2 = len(t1),len(t2) # Stocker ces longueurs permet d'être plus efficace en évitant les appels multiples à la fonction len à chaque tour de boucle
    t=[]
    i,j=0,0
    while i < l1 and j < l2: # 1ere partie : on n'a fini aucun des deux tableaux
    # Si on met un or au lieu du and dans la condition du while, alors il y aura une erreur
    # dans le test ci-dessous quand on sera à la fin d'un tableau et pas de l'autre.
        if t1[i]<=t2[j]:
            t.append(t1[i])
            i=i+1
        else:
            t.append(t2[j])
            j=j+1
    # 2e partie : on complète tant qu'il reste des éléments
    # On remarque qu'une seule des 2 boucles while ci-dessous sera réellement effectuée
    # (l'autre aura sa condition fausse dès le début) mais on ne peut pas savoir d'avance laquelle
    while i < l1:
        t.append(t1[i])
        i=i+1
    while j < l2:
        t.append(t2[j])
        j=j+1
    return t

#print(fusion([2,4],[1,3]))
#print(fusion([2,4,5,8,9],[1,3,6]))

def fusionBis(t1,t2):
    l1,l2 = len(t1),len(t2)
    i,j = 0,0
    t = []
    for k in range(0,l1+l2):
    # Ici on a un test plus compliqué qui tient compte des différents cas possibles (il reste des élements dans un seul des tableaux ou dans les deux).
    # Ce test utilise l'évaluation paresseuse des booléens : si on l'écrivait en changeant l'ordre, par exemple
    # ((t1[i]<=t2[j] or j == l2) and i<l1) alors on aurait des problèmes d'indices trop grands
        if (i<l1 and (j == l2 or t1[i]<=t2[j])):
            t.append(t1[i])
            i=i+1
        else:
            t.append(t2[j])
            j=j+1
    return t

#print(fusionBis([2,4],[1,3]))
#print(fusionBis([2,4,5,8,9],[1,3,6]))


# Exercice 8

def triSelection(t) :
    for i in range(len(t)-1) :
        petit = t[i]
        indice = i
        for j in range(i+1,len(t)) :
            if t[j] < petit :
                petit = t[j]
                indice = j
        t[indice] = t[i]
        t[i] = petit
#        print(t)
    return t
# L'instruction print(t) en commentaire ne fait pas partie du tri par selection
# mais vous pouvez la décommenter pour mieux voir ce qu'il se passe

#print(triSelection([15,4,2,9,9,55,0,1,9]))


# Exercice 9
      
def triInsertion(t):
    for i in range(1,len(t)):
        v = t[i]
#        print("v =",v)
        j = i-1
        while(j>=0 and t[j]>v):
            t[j+1] = t[j]
            j = j-1
#            print(t)
        t[j+1] = v
#        print(t)
    return t
# Les instruction print en commentaire dans la fonction ne font pas partie du tri par insertion
# mais vous pouvez les décommenter pour bien voir ce qu'il se passe à chaque étape.

#print(triInsertion([15,4,2,9,9,55,0,1,9]))


# Exercice 10

def incremente(l):
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            l[i][j] = l[i][j] + 1
    print(l)

#incremente([[3,6,5],[-2,-4,-1,-8],[7,9]])


# Exercice 11

def recherche2(l,x):
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            if l[i][j] == x:
                return True
    return False

#print(recherche2([[3,6,5],[-2,-4,-1,-8],[7,9]],-8))


# Exercice 12

#1
def carre(l):
    for i in range(0,len(l)):
        if len(l[i]) != len(l):
            return False
    return True

#print(carre([[0,0,0],[0,0],[0,0,0]]))

#2
def sommeLigne(l,i):
    s = 0
    for k in range(0,len(l[i])):
        s = s + l[i][k]
    return s
    
#print(sommeLigne([[3,6,5],[-2,-4,-1,-8],[7,9]],0))

def sommeColonne(l,i):
    s = 0
    for k in range(0,len(l)):
        s = s + l[k][i]
    return s
    
#print(sommeColonne([[3,6,5],[-2,-4,-1,-8],[7,9]],1))

#3
def sommeDiagonaleMajeure(l):
    s = 0
    for i in range(0,len(l)):
        s = s + l[i][i]
    return s
    
#print(sommeDiagonaleMajeure([[3,6,5],[-2,-4,-1],[-8,7,9]]))

def sommeDiagonaleMineure(l):
    s = 0
    for i in range(0,len(l)):
        s = s + l[i][len(l)-1-i]
    return s
    
#print(sommeDiagonaleMineure([[3,6,5],[-2,-4,-1],[-8,7,9]]))

#4
def carreMagique(l):
    if not carre(l):
        return False
    s = sommeDiagonaleMajeure(l)
    if sommeDiagonaleMineure(l) != s:
        return False
    for i in range(0,len(l)):
        if sommeLigne(l,i) != s:
            return False
        if sommeColonne(l,i) != s:
            return False
    return True

#print(carreMagique([[0,0,0],[0,0,0],[0,0,0]]))
#print(carreMagique([[0,0,0],[0,0,1],[0,0,0]]))

#5
def histogramme(t):
    h = []
    for i in range(0,len(t)**2+1):
        h.append(0)
    for i in range(0,len(t)):
        for j in range(0,len(t[i])):
            h[t[i][j]] = h[t[i][j]] + 1
    return h

#print(histogramme([[1,2,1],[9,6,2],[1,1,7]]))

#6
def carreMagiqueNormal(l):
    if not carreMagique(l):
        return False
    h = histogramme(l)
    for i in range(1,len(h)):
        if h[i] != 1:
            return False
    return True
    
#print(carreMagiqueNormal([[0,0,0],[0,0,0],[0,0,0]]))
#print(carreMagiqueNormal([[6,7,2],[1,5,9],[8,3,4]]))