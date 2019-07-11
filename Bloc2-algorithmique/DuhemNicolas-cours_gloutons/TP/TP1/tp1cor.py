#Partie I
#question 1
#définition de la caisse
caisse=[200,100,50,20,10,5,2,1]
#question 2
def rendmonnaie(s,c):
    n=len(c)
    rendu=len(c)*[0]
    somme_a_rendre=s*100
    i=0
    while somme_a_rendre>0 and i<=n-1:
        while somme_a_rendre>=c[i] :
            somme_a_rendre=somme_a_rendre-c[i]
            rendu[i]=rendu[i]+1
        i=i+1
    return rendu
#version bis
def rendmonnaie2bis(s,c):
    n=len(c)
    rendu=[[c[i],0] for i in range(len(c))]
    somme_a_rendre=s*100
    i=0
    while somme_a_rendre>0 and i<=n-1:
        if somme_a_rendre>=c[i] :
            rendu[i][1]=int(somme_a_rendre//c[i])
            somme_a_rendre=somme_a_rendre%c[i]
        i=i+1
    return rendu

#test
print(rendmonnaie(2.34,caisse))
print(rendmonnaiebis(2.34,caisse))
#reponse dans les deux cas  [1, 0, 0, 1, 1, 0, 2, 0]

#Partie II
def rendmonnaie2(s,c):
    n=len(c)
    rendu=[[c[i],0] for i in range(len(c))]
    somme_a_rendre=s*100
    i=0
    while somme_a_rendre>0 and i<=n-1:
        while somme_a_rendre>=c[i] :
            somme_a_rendre=somme_a_rendre-c[i]
            rendu[i][1]=rendu[i][1]+1       
        i=i+1
    return rendu
#version bis
def rendmonnaie2bis(s,c):
    n=len(c)
    rendu=[[c[i],0] for i in range(len(c))]
    somme_a_rendre=s*100
    i=0
    while somme_a_rendre>0 and i<=n-1:
        if somme_a_rendre>=c[i] :
            rendu[i][1]=int(somme_a_rendre//c[i])
            somme_a_rendre=somme_a_rendre%c[i]
        i=i+1
    return rendu
#test
print(rendmonnaie2(2.34,caisse))
print(rendmonnaie2bis(2.34,caisse))
#reponse [[[200, 1], [100, 0], [50, 0], [20, 1], [10, 1], [5, 0], [2, 2], [1, 0]]
print(rendmonnaie2(5.71,caisse))
print(rendmonnaie2bis(5.71,caisse))
#reponse [[200, 2], [100, 1], [50, 1], [20, 1], [10, 0], [5, 0], [2, 0], [1, 1]]

#Partie III
#question 1
#Création d'un dictionnaire contenant une quantité aléatoire de pièce
import random
#Création d'un dictionnaire contenant une quantité aléatoire de pièce
caisse2={caisse[i] : random.randint(0,5)  for i in range(len(caisse))}
print(caisse2)
#reponse {200: 3, 100: 5, 50: 3, 20: 4, 10: 3, 5: 5, 2: 0, 1: 5}


#question 2
def rendmonnaie3(s,d):
    somme_a_rendre=s*100
    rendu={i:0 for i in d}
    for i in caisse:
        while somme_a_rendre>=i and caisse2[i]>0:
            somme_a_rendre=somme_a_rendre-i
            rendu[i]=rendu[i]+1
            caisse2[i]=caisse2[i]-1
    if somme_a_rendre>0:
           return print("il n'y a plus assez de monnaie")
    return rendu
#test
print("caisse à notre disposition :",caisse2)
print("rendu : ",rendmonnaie3(2.34,caisse2))
#reponse
#caisse à notre disposition : {200: 3, 100: 5, 50: 3, 20: 4, 10: 3, 5: 5, 2: 0, 1: 5}
#rendu :  {200: 1, 100: 0, 50: 0, 20: 1, 10: 1, 5: 0, 2: 0, 1: 4}
print("caisse à notre disposition :",caisse2)
print("rendu :",rendmonnaie3(4.54,caisse2))
#reponse
#caisse à notre disposition : {200: 2, 100: 5, 50: 3, 20: 3, 10: 2, 5: 5, 2: 0, 1: 1}
#il n'y a plus assez de monnaie
#rendu : None

