# -*- coding: utf-8 -*-

# Correction du TP 3

"""
Dans tout ce fichier, les I indiquent la version itérative,
et les R indiquent la version récursive.

Pour les fonctions récursives,
il est bon de s'arranger pour qu'un appel de la fonction
ne mène jamais à un calcul infini,
même si l'utilisateur entre un nombre négatif.
Il vaut donc mieux prévoir les cas négatifs.

Par convention mathématique, une somme vide vaut 0
et un produit vide vaut 1.
Ceci donne les valeurs pour n négatif
des fonctions des exercices 1, 2, 3, 9 et 10.
"""

# Exercice 1

def sommeI(n):
    s = 0    
    for i in range(1,n+1):
        s = s+i
    return s
#print(sommeI(7))
""" Complexité : O(n) """  

def sommeR(n):
    if n <= 0:
        return 0
    else:
        return n + sommeR(n-1)
#print(sommeR(7))
""" Complexité : O(n) """
   

# Exercice 2
     
def factorielleI(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
#print(factorielleI(7))
""" Complexité : O(n) """

def factorielleR(n):
    if n <= 0:
        return 1
    else:
        return n * factorielleR(n-1)
#print(factorielleR(7))
""" Complexité : O(n) """


# Exercice 3

def sommeCarreI(n):
    s = 0
    for i in range(1,n+1):
        s = s + i**2
    return s
#print(sommeCarreI(4))
""" Complexité : O(n) """

def sommeCarreR(n):
    if n <= 0:
        return(0)
    else:
        return n**2 + sommeCarreR(n-1)
#print(sommeCarreR(4))
""" Complexité : O(n) """


# Exercice 4

def puissanceI(x,n):
    p = 1
    if n > 0:    
        for i in range(n):
            p = p*x
    else:
        for i in range(-n):
            p = p/x
    return p
#print(puissanceI(-2.5,3))
#print(puissanceI(2.5,-3))
""" Complexité : O(n) """

def puissanceR(x,n):
    if n == 0:
        return 1
    elif n > 0:
        return x * puissanceR(x,n-1)
    else:
        return 1 / puissanceR(x,-n)
#print(puissanceR(-2.5,3))
#print(puissanceR(2.5,-3))
""" Complexité : O(n) """


# Exercice 5

def termeI(n):
    if n < 0:
        return "Erreur, n négatif"
    else :
        u = 2
        for i in range (1,n+1):
            u = 1/2*(u+3/u)
        return u
#print(termeI(5))
""" Complexité : O(n) """
  
def termeR(n):
    if n == 0:
        return 2
    elif n < 0 :
        return "Erreur, n négatif"
    else :
        return 1/2*(termeR(n-1) + 3/termeR(n-1))
#print(termeR(5))
""" Complexité : O(2^n) donc exponentielle.
Si vous lancez cette fonction pour n autour de 25,
vous pouvez déjà voir que le temps de calcul est long
"""

# Version plus efficace :
def termeR2(n):
    if n == 0:
        return 2
    elif n < 0 :
        return "Erreur, n négatif"
    else :
        u = termeR2(n-1)
        return 1/2*(u+3/u)
#print(termeR2(5))
""" Complexité : O(n) """


# Exercice 6

def compterI(n):
    for i in range(1,n+1):
        print(i)
#compterI(4)
""" Complexité : O(n) """
        
def compterR(n):
    if n >= 1:
        compterR(n-1)
        print(n)
#compterR(4)
""" Complexité : O(n) """


# Exercice 7

def reboursI(n):
    for i in range(0,n+1):
        print(n-i)
#reboursI(4)
""" Complexité : O(n) """

def reboursR(n):
    if n >= 0:
        print(n)
        reboursR(n-1)
#reboursR(4)
""" Complexité : O(n) """
      

# Exercice 8

# Solution avec une liste :
def fibonacci(n):
    u=[]
    u.append(0)
    u.append(1)
    for i in range(2,n+1):
        u.append(u[i-1]+u[i-2])
    return u[n]
#print(fibonacci(7))
""" Complexité en temps : O(n) """
""" Complexité en espace : O(n) """

# Solution sans liste :
def fibonacciI(n):
    if n == 0:
        return 0
    F0=0
    F1=1
    for i in range(2,n+1):
        F=F1+F0
        F0=F1
        F1=F
    return F1
#print(fibonacciI(7))
""" Complexité en temps : O(n) """
""" Complexité en espace : O(1), meilleure """


def fibonacciR(n):
    if n==0 :
        return 0
    if n==1 :
        return 1
    return fibonacciR(n-1) + fibonacciR(n-2)
#print(fibonacciR(7))
""" Complexité : O(c^n) donc exponentielle,
où c = (1+racine(5))/2 est le nombre d'or.
Complexité exponentielle qu'on ne peut pas contourner comme dans l'exercice 5,
car les 2 appels sont sur des valeurs différentes.
On peut contourner cela en utilisant des techniques hors programme de prépa.
"""
        

# Exercice 9

def doubleFactorielleI(n):
    f = 1
    i = n    
    while i > 0:
        f = f*i
        i = i-2
    return f
#print(doubleFactorielleI(5))
#print(doubleFactorielleI(6))
""" Complexité : O(n) """

# Autre solution:
def doubleFactoI(n):
    x=1
    for i in range(n,0,-2):
        x=x*i
    return x   
#print(doubleFactoI(5))
#print(doubleFactoI(6))
""" Complexité : O(n) """

def doubleFactorielleR(n):
    if n <= 1:
        return 1
    else:
        return n * doubleFactorielleR(n-2)
#print(doubleFactorielleR(5))
#print(doubleFactorielleR(6))
""" Complexité : O(n) """


# Exercice 10

"""On remarque que la double factorielle correspond
à la multifactorielle avec k = 2."""

def multiFactorielleI(n,k):
    f = 1
    i = n
    while i > 0:
        f = f*i
        i = i-k
    return f
#print(multiFactorielleI(6,3))
#print(multiFactorielleI(7,3))
#print(multiFactorielleI(8,3))
""" Complexité : O(n/k)
Si k est grand, par exemple de l'ordre de racine de n,
une complexité en O(n/k) est meilleure qu'en O(n).
"""

# Autre solution
def multifactoI(n,k):
    x=1
    for i in range(n,0,-k):
        x=x*i
    return x   
    
#print(multifactoI(6,3))
#print(multifactoI(7,3))
#print(multifactoI(8,3))
""" Complexité : O(n/k)"""
    
def multiFactorielleR(n,k):
    if n <= 1:
        return 1
    else:
        return n * multiFactorielleR(n-k,k)
#print(multiFactorielleR(6,3))
#print(multiFactorielleR(7,3))
#print(multiFactorielleR(8,3))
""" Complexité : O(n/k)"""


# Exercice 11

def partieEntiereI(x):
    e = 0
    if x >= 0:
        while e <= x-1:
            e = e+1
        return e
    else:
        while e > x:
            e = e-1
        return e
#print(partieEntiereI(6.4))
#print(partieEntiereI(-6.4))
""" Complexité : O(x) """
        
def partieEntiereR(x):
    if x >= 0 and x < 1:
        return 0
    elif x > 0:
        return 1 + partieEntiereR(x-1)
    else:
        return -1 + partieEntiereR(x+1)
#print(partieEntiereR(6.4))
#print(partieEntiereR(-6.4))
""" Complexité : O(x) """


# Exercice 12

def pgcdI(a,b):
    while a % b != 0:
        a, b = b, a%b
    return b
#print(pgcdI(24,42))

def pgcdR(a,b):
    if b==0:
        return a
    return pgcdR(b,a%b)
#print(pgcdR(24,42))
"""
La complexité de la fonction pgcd n'était pas demandée
car elle est n'est pas facile à évaluer.
"""


# Exercice 13

def briquesR(n):
    if n <= 1:
        return 0
    if n == 2 or n == 3:
        return 1
    return briquesR(n-2) + briquesR(n-3)

#print(briquesR(14))
"""
Principe : un mur commence soit par une brique de taille 2, et alors il reste
à faire un mur de taille n-2, soit par une brique de taille 3, et alors il
reste à faire un mur de taille n- 3 
"""


# Exercice 14

def ackR(m,n):
    if m < 0 or n < 0:
        return "Erreur : entier négatif"
    if m == 0:
        return n+1
    if n == 0:
        return ackR(m-1,1)
    return ackR(m-1,ackR(m,n-1))
    
#print(ackR(1,3))
#print(ackR(2,3))
#print(ackR(3,2))