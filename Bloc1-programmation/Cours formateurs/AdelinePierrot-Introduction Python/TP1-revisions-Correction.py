# -*- coding: utf-8 -*-
# Correction du TP 1

# Exercice 1

def bonjour():
    nom = input("Quel est votre prénom ? ")
    print("Bonjour", nom)
    
#bonjour()
    

# Exercice 2
    
def conversion(prix):
    return 9.13*prix
    
#print(conversion(2.5))


# Exercice 3
    
def examen():
    note = float(input("Entrez votre note : "))
    if note < 0 or note > 20:
        print("Erreur, note incohérente")
    elif note < 10:
        print("Votre note est", note, ", vous n'avez pas réussi l'examen")
    else:
        print("Votre note est", note, ", vous avez réussi l'examen")
        
#examen()        
    

# Exercice 4

def nombre2lettre(x):
    if 15 <= x <= 20:
        return "A"
    if 10 <= x < 15:
        return "B"
    if 5 <= x < 10:
        return "C"
    if 0 <= x < 5:
        return "D"
    else:
        return "E"
        
#print(nombre2lettre(13))  

# Autre solution:
def nombre2lettre2(x):
    if x < 0 or x > 20:
        return "E"
    elif 15 <= x:
        return "A"
    elif 10 <= x:
        return "B"
    elif 5 <= x:
        return "C"
    else:
        return "D"
        
#print(nombre2lettre2(17))  


# Exercice 5

def compter(n):
    for i in range(1,n+1):
        print(i)

#compter(5)


# Exercice 6

def triangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end='')
        print()

#triangle(4)

# triangle inversé:
def triangle2(n):
    for i in range(n):
        for j in range(1,n+1-i):
            print(j, end='')
        print()

#triangle2(4)

# Autre solution triangle inversé:
def triangleBis(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end='')
        print()
       
#triangleBis(4)
 

# Exercice 7

def continuer():
    reponse = input("continuer ? ")
    while reponse == "oui":
        reponse = input("continuer ? ")

#continuer()


# Exercice 8

def multiple():
    n = int(input("Combien de nombres ? "))
    produit = 1
    for i in range(1,n+1):
        print("Nombre",i,":")
        nombre = float(input())
        produit = nombre * produit
    print("Le produit vaut ",produit)

#multiple()


# Exercice 9

def produit():
    resultat = 1
    print("Entrez les nombres à multiplier en terminant par 0 :")
    nombre = float(input())
    while nombre != 0:
        resultat = nombre * resultat
        nombre = float(input())
    print("le produit vaut ", resultat)

#produit()


# Exercice 10

def terme(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    u0 = 1
    u1 = 2
    for i in range(2,n+1):
        u = 3*u1+u0
        u0 = u1
        u1 = u
    return u

#print(terme(4))


# Exercice 11

def mult3pas9(n):
    return n%3 == 0 and n%9 != 0

#print(mult3pas9(18))


# Exercice 12

def premiers(n):
    for nombre in range(2,n+1):
        estPremier = True
        for i in range(2,nombre):
            if nombre % i == 0:
                estPremier = False
        if estPremier:
            print(nombre)
            
#premiers(30)


# Exercice 13

def premiers2(n):
    compteur = 0
    nombre = 2
    while(compteur < n):
        estPremier = True
        for i in range(2,nombre):
            if nombre % i == 0:
                estPremier = False
        if estPremier:
            print(nombre)
            compteur = compteur+1
        nombre = nombre+1

#premiers2(5)
