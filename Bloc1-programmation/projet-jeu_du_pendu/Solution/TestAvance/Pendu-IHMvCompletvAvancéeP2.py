# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:22:08 2019

@author: magali.sauvergeat
"""
from random import randint
from random import choice
import turtle
import os.path

ERREURMAX =12
     

def gen_dico_vide(freqalpha,alpha):
     for i in range(len(alpha)):
         freqalpha[alpha[i]] = 0
     print(freqalpha)
         
         
def calcul_frequence(freqalphal, nomfichier):
    
        #nomfichier="liste_francaisU.txt"
        if os.path.isfile(nomfichier): # retourne vrai si le fichier existe
            print(nomfichier)
            fichier= open(nomfichier,"r")
            mot ="debut"
            nbl = 0
            while mot !="" : 
                mot = fichier.readline()
                mot=normalise(mot)
                for lettre in mot:
                    if lettre in freqalpha.keys():
                        freqalpha[lettre]=freqalpha[lettre]+1
                        nbl= nbl+1
            print(freqalpha)     
            print("nombre de lettres",nbl)
            fichier.close()   
            if nbl>0:
                for l in freqalpha.keys():
                    freqalpha[l] = freqalpha[l]/nbl
                print(freqalpha)     
        
def calcul_proba_lettre(probaalpha,nomfichier):
    
        #nomfichier="liste_francaisU.txt"
        if os.path.isfile(nomfichier): # retourne vrai si le fichier existe
            print(nomfichier)
            fichier= open(nomfichier,"r")
            mot ="init"
            nbm = -1 # compteur de mot
            while mot !="" : 
                mot = fichier.readline()
                mot=normalise(mot)
                unique=set(mot) # enlève les lettres redondantes
                nbm= nbm+1
                for lettre in unique:
                    if lettre in probaalpha.keys():
                        probaalpha[lettre] = probaalpha[lettre]+1
                        
            print(probaalpha)     
            print("nombre de mots",nbm)
            fichier.close()   
            if nbm>0:
                for l in probaalpha.keys():
                    probaalpha[l] = probaalpha[l]/nbm
                print(probaalpha)     

# Trouver la lettre dont la fréquence est maximum, qui n'a pas déjà été proposée.   
def demo_v2(lettres, frequence ):
    maxF=0.0
    maxL=""
    for clef, valeur in frequence.items():
        #test clef n'est pas dans lettres
        Trouve=False
        for i in range(len(lettres)):
            if clef == lettres[i]:
                Trouve=True
        if (maxF < valeur) and (Trouve == False):
            maxF=valeur
            maxL=clef
    return maxL

# Proposer une lettre aléatoire
def demo_v1(lettres):
    l=""
    Trouve=True
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while Trouve==True:
        Trouve=False
        l=choice(alpha) #tirer aléatoirement une lettre
        for i in range(len(lettres)):
            if l == lettres[i]:
                Trouve=True
    return l

#choisi un mot au hasard dans la liste des mots du français et élimine
#les accents et autres lettres spéciales
def choisi_mot(nbmax, nomfichier):
    #ouvre et lit le fichier contenant tout les mots francais
#    nomfichier="liste_francaisU.txt"
    if os.path.isfile(nomfichier): # retourne vrai si le fichier existe
        fichier=open(nomfichier)
        texte=fichier.readlines()  #lit toutes les lignes du fichier texte
        fichier.close()
        taille=len(texte)
    
        longueur=-1
        #tirage au sort d'un mot inconnu entre 6 et 3 lettres
        while (longueur>nbmax) or (longueur<3):
            nombre = randint(0,taille-1)
            inconnu=texte[nombre]
            inconnu=normalise(inconnu) # enlève les accents
            inconnu=inconnu.strip() #retire le \n final 
            longueur=len(inconnu)
        return inconnu
    else: 
        return "vide"
    
def normalise(inconnu):
        inconnu=inconnu.lower()
        inconnu=inconnu.replace('é','e')
        inconnu=inconnu.replace('ê','e')
        inconnu=inconnu.replace('î','i')
        inconnu=inconnu.replace('ï','i')
        inconnu=inconnu.replace('è','e')
        inconnu=inconnu.replace('û','u')
        inconnu=inconnu.replace('à','a')
        inconnu=inconnu.replace('ç','c')
        inconnu=inconnu.replace('ô','o')
        # réfléchir au carctère e dans l'o
        return inconnu

   
# Génère un tableau de tirets
def genere_tirets(n):
    ch=[]   
    for i in range(n):
        ch.append("-")
    return ch
# vérifier si la lettre l est dans le mot à trouver
def lettre_presente(tab,l):    
    for i in range(len(tab)):
        if(tab[i]==l[0]):
            return True
    return False
#Montre la lettre dans le tableau de proposition    
def devoiler_lettre(sol,prop,l):
    for i in range(len(sol)):
        if(sol[i]==l[0]):
            prop[i]=sol[i]
#Vérifie si la proposition est bonne 
def test_gagner(sol,prop): # if(sol == prop)
    for i in range(len(sol)):
        if(sol[i]!=prop[i]):
            return False
    return True

placement = [(0,-70), (0,-100), # placement du texte
            (-150,-30),(50,-30),#plancher
             (-50,-30),(-50,150),#barre verticale
             (-50,150),(80,150),#barre horirontale haute
             (-50,100),(30,150),#barre oblique
             (80,150),(80,120),#haut corde
             (80,110),(80,110),#tete
            (80,100),(80,30), #colonne vertébrale
            (80,30),(60,10),#jambe droite
            (80,30),(100,10),#jambe gauche
            (80,90),(60,70),  #bras droit
            (80,90),(100,70) ]  #bras gauche
#dessine le pendu avec l'objet feutre permettant de tracer le pendu.
# prend en entrée l'objet feutre, le numéro de l'étape, et le tableau des coordonnées
def dessin_pendu(feutre,etape, placement): 
    if etape < 12:
        feutre.penup()
        if etape != 6 :
            feutre.goto(placement[etape*2])
            feutre.pendown()
            feutre.goto(placement[etape*2+1])
        else:               # cas de la tête
            feutre.goto(placement[etape*2])
            feutre.pendown()
            feutre.dot(30)
            feutre.pensize(5)  # pour le corps on passe à un trait plus fin 

def dessin_texte(stylo,texte,position,couleur="black",efface=True): 
            stylo.goto(position)
            if efface:
                stylo.clear()
            stylo.color(couleur)
            stylo.write(''.join(texte), align="center", font=(None, 16, "bold")) 

###############################################################################"
lettresP=[]
stylo2= turtle.Turtle() # pour afficher les lettres déjà proposées
stylo2.hideturtle()# cache le pointeur permettant de suivre la position de tracage     
nberreur=0
feutre= turtle.Turtle() # pour le dessin du pendu
feutre.hideturtle() # cache le pointeur permettant de suivre la position de tracage
stylo= turtle.Turtle() # pour afficher le tableaux de tirets
stylo.hideturtle()# cache le pointeur permettant de suivre la position de tracage    
stylo2= turtle.Turtle() # pour afficher les lettres déjà proposées
stylo2.hideturtle()# cache le pointeur permettant de suivre la position de tracage   
feutre.penup()
feutre.pensize(8)       
motcache= ""

def prog_principal(ihm,probaalpha):
    global lettresP
    global stylo2
    global stylo
    global feutre
    global devine
    global motcache
    global nberreur


    motcache= choisi_mot(7,"liste_francaisU.txt")
    devine=genere_tirets(len(motcache)) 
    dessin_texte(stylo,devine,placement[0])
    feutre.penup()
    msg ="Le Pendu"
    dessin_texte(feutre,msg,(-50,170),'blue',False)        
    msg ="Taper une lettre \n click gauche -> quitter \n click milieu -> recommencer"
    dessin_texte(feutre,msg,(-150,-200),'blue',False) 
    feutre.color("black")       
    turtle.listen()  
    turtle.onscreenclick(quitter, 3)
    turtle.onscreenclick(reinit, 2)
#    turtle.onkeypress(gestion_evea, "a")  


    for c in alpha:
        fct="gestion_eve"+c
        turtle.onkeypress(eval(fct), c)  


def gestion_evea():
    gestion_eve("a")
def gestion_eveb():
    gestion_eve("b")
def gestion_evec():
    gestion_eve("c")
def gestion_eved():
    gestion_eve("d")
def gestion_evee():
    gestion_eve("e")
def gestion_evef():
    gestion_eve("f")
def gestion_eveg():
    gestion_eve("g")
def gestion_eveh():
    gestion_eve("h")
def gestion_evei():
    gestion_eve("i")  
def gestion_evej():
    gestion_eve("j")
def gestion_evek():
    gestion_eve("k")
def gestion_evel():
    gestion_eve("l")   
def gestion_evem():
    gestion_eve("m")
def gestion_even():
    gestion_eve("n")
def gestion_eveo():
    gestion_eve("o")    
def gestion_evep():
    gestion_eve("p")
def gestion_eveq():
    gestion_eve("q")
def gestion_ever():
    gestion_eve("r")
def gestion_eves():
    gestion_eve("s")
def gestion_evet():
    gestion_eve("t")
def gestion_eveu():
    gestion_eve("u")
def gestion_evev():
    gestion_eve("v")
def gestion_evew():
    gestion_eve("w")
def gestion_evex():
    gestion_eve("x")
def gestion_evey():
    gestion_eve("y")
def gestion_evez():
    gestion_eve("z") 

def gestion_eve(lettre):
    #lettre ="a"
    global lettresP
    global stylo2
    global stylo
    global feutre
    global devine
    global motcache
    global nberreur
    lettresP.append(lettre) 
    Trouve = False
    if(lettre_presente(motcache,lettre)==True):
        devoiler_lettre(motcache,devine,lettre)
        dessin_texte(stylo,devine,placement[0])
        msg = "lettres proposées :"+''.join(lettresP)
        dessin_texte(stylo2,msg,placement[1])
        Trouve =test_gagner(motcache,devine) 
    else:
        nberreur=nberreur+1
        dessin_pendu(feutre,nberreur,placement) # dessine la partie du pendu correspondant
        dessin_texte(stylo,devine,placement[0])
        msg = "lettres proposées :"+''.join(lettresP)
        dessin_texte(stylo2,msg,placement[1])
    if Trouve == True:
        msg = "Gagné ! \n La solution était : "+motcache
        dessin_texte(stylo2,msg,placement[1],'red') 
    elif nberreur==12:
        msg = "Perdu ! \n La solution était : "+motcache
        dessin_texte(stylo2,msg,placement[1],'red') 

        
def reinit(x=0,y=0):
    global stylo2
    global stylo
    global feutre
    global devine
    global motcache
    global nberreur
    global lettresP
    lettresP=[]
    nberreur = 0
    stylo.clear()
    feutre.clear()
    stylo2.clear()
    feutre.pensize(8) 
    feutre.penup()     
    motcache= choisi_mot(7,"liste_francaisU.txt")
    devine=genere_tirets(len(motcache))
    dessin_texte(stylo,devine,placement[0])
    msg ="Le Pendu"
    dessin_texte(feutre,msg,(-50,170),'blue',False)            
    msg ="Taper une lettre \n click gauche -> quitter \n click milieu -> recommencer"
    dessin_texte(feutre,msg,(-150,-200),'blue',False)        
    feutre.color("black")
    
    
def quitter(x,y):
    ihm.exitonclick()
    turtle.bye()    

  


def init_fenetre():
    ihm =turtle.Screen()
    ihm.setup(640, 480, 100, 100)  #Largeur : 640px, Hauteur : 480px, pos x : 100px, pos y : 100px
    ihm.setup(200, 200)  #Largeur : 200px, Hauteur : 200px, position centrée
    ihm.setup(startx = 0, starty = 0)  #Largeur : 50%, Hauteur : 75%, position : coin haut gauche écran
    ihm.setup()  #Largeur : 50%, Hauteur : 75%, position centrée
    ihm.title("Le Pendu ")  #Change le titre
    return ihm

if __name__ == '__main__':
    global ihm    
    frequence = {'a' : 0.083944, 'b' : 0.007669,  'c' : 0.033297, 'd' : 0.040699, 'e' : 0.145037,
              'f' : 0.012109, 'g' : 0.009495, 'h' : 0.007973, 'i' : 0.081828, 'j' : 0.006377, 'k' : 0.000638, 'l' : 0.058405,
              'm' : 0.029355, 'n' : 0.075570, 'o' : 0.053669, 'p' : 0.032087, 'q' : 0.012613, 'r' : 0.070209, 's' : 0.080091,
              't' : 0.074775, 'u' : 0.059808, 'v' : 0.015791, 'w' : 0.000067, 'x' : 0.004098, 'y' : 0.003155, 'z' : 0.001240}              

    freqalpha = {}
    probaalpha = {}
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    #Candidat 3
    gen_dico_vide(freqalpha,alpha)
    calcul_frequence(freqalpha,"liste_francaisU.txt")
    gen_dico_vide(probaalpha,alpha)
    calcul_proba_lettre(probaalpha,"liste_francaisU.txt")

#    #Candidat 2
    ihm=init_fenetre()
    prog_principal(ihm,probaalpha)
    turtle.mainloop()
    ihm.exitonclick()
#    turtle.bye()
