#-*- coding: Utf-8 -*-

''' Retouche d'images au format PGM ascii
    Auteur P. Jaubert juin 2019 '''

def lecture_fichier(filename):
    ''' teste si le fichier de depart est un fichier pgm (1ere ligne = P2)
    et retourne les 3 lignes d'entete du fichier puis la chaine des pixels en forme string.
    L'intensite max, hauteur et largeur sont retournee sous type int 
    pre-conditions : le fichier est code en pgm ascii
        entete attendue :
        P2
        # commentaire ou non
        largeur et hauteur en pixels
        intensite entre 0 et 255
        les pixels avec espace ou lf (\n) comme separateurs'''


    f = open(filename,"r")
    ligne1= f.readline()
    if ligne1=='P2\n' :
        ligne2=  f.readline()
        while ligne2[0] =='#' :           # vérifie si il n'y a pas un commentaire.
            ligne2=  f.readline()
        (largeur, hauteur) =  taille_img(ligne2)
        intensite= int (f.readline())
        s= f.read()
        f.close()
        return largeur, hauteur, intensite, s
    else :
        print ("ce n'est pas un fichier pgm ascii")
        f.close()
        return '-1'


def taille_img(s):
    """ extrait sous forme int largeur et hauteur de la chaine s (ligne 2 du fichier)"""

    ls=''
    hs=''
    i=0
    while (s[i]!=' '):
        ls= ls+s[i]
        i+=1
    l=int(ls)
    while (s[i]!='\n'):
        hs= hs+s[i]
        i+=1
    h=int(hs)

    return l,h

def lecture_photo(s,l,h, table) :
    """ lit les differentes valeurs ASCII et les place dans un tableau de h lignes sur l colonnes"""
    i=0

# remplissage du tableau
    for j in range (0,h):
        for k in range (0,l) :
            temp=""
            while s[i]!=' ' and s[i] !='\n' :
                temp=temp+s[i]
                i+=1
            table[j][k]=int(temp)
            i+=1

    return table

def ecriture_photo(filename,l,h, intens,table) :
    """ remplit les 3 premieres lignes puis ecrit differentes valeurs ASCII en fonction du tableau de h lignes sur l colonnes"""

    f = open(filename,"w")
    s="P2\n"+str(l)+' '+str(h)+'\n'+str(intens)+'\n'

    # remplissage du tableau
    for j in range (0,h):
        for k in range (0,l) :
            s= s + str(table[j][k])+' '
    f.write(s)
    f.close()

#  _______________________________________________________________________
# traitements

def NB_photo(l,h,lum,photo):
    for j in range (0,h):
        for k in range (0,l) :
            if photo[j][k]>lum//2 :
                photo[j][k]=lum
            else :
                photo[j][k]=0
    return photo


def negatif(l,h,lum,photo):

    for j in range (0,h):
        for k in range (0,l) :
            photo[j][k]=lum- photo[j][k]
    return photo


def floute(l,h,lum,photo):
    for j in range (0,h):
        for k in range (0,l-1) :
            photo[j][k+1]=(photo[j][k]+photo[j][k+1])//2;
    return(photo);


def miroir(l,h,photo):
    for j in range (0,h):
        for k in range (0,int(l/2)):
            droite = photo[j][k]
            gauche = photo[j][l-k-1]
            photo[j][k] = gauche
            photo[j][l-k-1] = droite

    return photo


def rotation(l,h,photo):
    ''' rotation horaire de 90 degres
    on cree une matrice vide  avec les dimensions interverties.
    on recopie element par element en modifiant les indices.
    '''
    #creation matrice vide
    ligne=[0]*h
    p2=[ligne[:] for i in range (0,l)]

    for i in range (0,h):
        for j in range(0,l):
            p2[j][i]=photo[h-1-i][j]

    return p2

def photomaton(l,h,photo):

    if h%2!=0:
        h -=1

    if l%2!=0:
        l -=1

    #creation matrice vide
    ligne=[0]*l
    p2=[ligne[:] for i in range (0,h)]

    for j in range (0,h,2):
        for k in range (0,l,2):
            couleur = int((photo[j][k]+photo[j+1][k]+photo[j][k+1]+photo[j+1][k+1])/4)

            haut=int(j/2)
            bas=int(j/2)+int(h/2)
            gauche=int(k/2)
            droite=int(k/2)+int(l/2)

            p2[haut][gauche] = couleur
            p2[bas][gauche] = couleur
            p2[haut][droite] = couleur
            p2[bas][droite] = couleur

    return p2,l,h

def zoom(l,h,photo):

    #creation matrice vide (2xZ fois plus grande)
    ligne=[0]*l*2
    p2=[ligne[:] for i in range (0,h*2)]

    #version 1
    for j in range (0,h):
        for k in range (0,l):
            p2[j*2][k*2]=photo[j][k]
            p2[j*2+1][k*2]=photo[j][k]
            p2[j*2][k*2+1]=photo[j][k]
            p2[j*2+1][k*2+1]=photo[j][k]

    #version 2
    for j in range (1,h-1):
        for k in range (1,l-1):
            p2[j*2][k*2]=int((photo[j][k]+photo[j-1][k]+photo[j][k-1]+photo[j-1][k-1])/4)    #haut gauche
            p2[j*2+1][k*2]=int((photo[j][k]+photo[j+1][k]+photo[j][k-1]+photo[j+1][k-1])/4)  #haut droite
            p2[j*2][k*2+1]=int((photo[j][k]+photo[j-1][k]+photo[j][k+1]+photo[j-1][k+1])/4)  #bas gauche
            p2[j*2+1][k*2+1]=int((photo[j][k]+photo[j+1][k]+photo[j][k+1]+photo[j+1][k+1])/4)  #bas droite

    return p2,l*2,h*2

# Programme principal
#  _______________________________________________________________________
#if __name__ == "__main__":


# fichier cible
f2 = "image_modifiee.pgm"

# liste des fichiers pgm presents dans le dossier courant et menu de choix

liste_pgm=[]
import os
for element in os.listdir():
    if element.endswith('.pgm'):
        liste_pgm.append(element)

for i in range (0, len(liste_pgm)):
    print (i, ' : ', liste_pgm[i])

a= -1
while a >= len(liste_pgm) or a < 0 :
    a = int(input("entrez votre choix d'image à  traiter\n" ))
f= liste_pgm[a]
print (f)

#lecture du fichier.
l,h, intensite, s = (lecture_fichier(f))
#print (intensite)
#print (l,h)

#intialisation de la matrice photo avec des 0
# pour creer la matrice il faut mettre le [:] sur la seconde ligne sinon on ne copie pas la liste ligne, on indexe la meme.
ligne=[0]*l
photo=[ligne[:] for i in range (0,h)]

# chargement de la matrice avec les pixels
photo=lecture_photo(s,l,h,photo)

#appel des traitements
print ('\nchoisissez le traitement a effectuer : \n')
choix= int (input("negatif : 1, NB : 2,  flou : 3, rotation horaire 90 Â° : 4, miroir : 5, photomaton : 6, zoom : 7\n"))
if choix==1 :
    photo= negatif(l,h,intensite,photo)
if choix==2 :
    photo= NB_photo(l,h,intensite,photo)
if choix==3 :
    photo= floute(l,h,intensite,photo)
if choix==4 :
    photo= rotation(l,h,photo)
    l,h= h,l
if choix==5 :
    photo= miroir(l,h,photo)
if choix==6 :
    photo,l,h= photomaton(l,h,photo)
if choix==7 :
    photo,l,h= zoom(l,h,photo)

ecriture_photo(f2,l,h,intensite, photo)
