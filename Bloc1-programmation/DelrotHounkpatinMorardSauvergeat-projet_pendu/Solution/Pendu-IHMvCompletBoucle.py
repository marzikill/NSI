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
# partie 3
def gen_html(frequence,alpha,nomfichier): 
  """ créé et génére un fichier html présentant le tableau des fréquences 
      de l'alphabet donné en entrée
        :param frequence: dictionnaire associant une lettre avec sa fréquence 
        :type frequence: dictionnaire    
        :param alpha: la liste des lettres de l'alphabet
        :type alpha: liste   
        :param nomfichier: le nom du fichier à créer
        :type nomfichier:  String
  """        
  try:  
        #nomfichier="pageFrequence.html"
        print(nomfichier)
        fichier= open(nomfichier,"w")    
        print("""<!DOCTYPE html> <!DOCTYPE html><html lang=\"fr\"><head>  <meta charset="UTF-8">  <meta name="author" content="msauver">
        <title>Table des fréquences de l'alphabet en français </title> <link rel="stylesheet" type="text/css" href="mystyle.css">
        </head><body><h1> Table des fréquences de l'alphabet en français </h1>
        <section><table><tr class="lumiere"><th>Lettre</th> <th> % de Fréquence</th> <th>Lettre</th> <th>% de Fréquence</th></tr>""",end='\n',file=fichier )
        for i in range(len(alpha)//2):
            print('<tr><td class="lumiere">',alpha[i],end='\n',file=fichier ) 
            print('</td><td> %.2f</td><td class="lumiere">'%(frequence[alpha[i]]*100),end='\n',file=fichier ) 
            print(alpha[i+(len(alpha)//2)],end='\n',file=fichier ) 
            print('</td><td>%.2f</td></tr>' %(frequence[alpha[i+(len(alpha)//2)]]*100),end='\n',file=fichier )            
          
        print('</table></section>',end='\n',file=fichier )    
        print('<footer>DIU-Bloc1  </footer></body></html>',end='\n',file=fichier )
        fichier.close()
  except FileNotFoundError:
        print("Erreur ouverture de Fichier")
        
def gen_htmlP(frequence,alpha,nomfichier): 
  """ créé et génére un fichier html présentant le tableau des probabilité d'apparition
      d'une lettre dans un mot
        :param frequence: dictionnaire associant une lettre avec sa probabilité d'apparition dans un mot
        :type frequence: dictionnaire    
        :param alpha: la liste des lettres de l'alphabet
        :type alpha: liste   
        :param nomfichier: le nom du fichier à créer
        :type nomfichier:  String
  """      
  try:  
        #nomfichier="pageFrequence.html"
        print(nomfichier)
        fichier= open(nomfichier,"w")    
        print("""<!DOCTYPE html> <!DOCTYPE html><html lang=\"fr\"><head>  <meta charset="UTF-8">  <meta name="author" content="msauver">
        <title>Table des probabilités d'apparition d'une lettre dans un mot</title> <link rel="stylesheet" type="text/css" href="mystyle.css">
        </head><body><h1> Probabilité d'apparition d'une lettre dans un mot </h1>""",end='\n',file=fichier )
      #  print("<h1> dans le fichier de test </h1>",end='\n',file=fichier )
        print("""<section><table><tr class="lumiere"><th>Lettre</th> <th>% de Probabilité</th> <th>Lettre</th> <th>% de Probabilité</th></tr>""",end='\n',file=fichier )      
        for i in range(len(alpha)//2):
            print('<tr><td class="lumiere">',alpha[i],end='\n',file=fichier ) 
            print('</td><td> %.2f</td><td class="lumiere">'%(frequence[alpha[i]]*100),end='\n',file=fichier ) 
            print(alpha[i+(len(alpha)//2)],end='\n',file=fichier ) 
            print('</td><td>%.2f</td></tr>' %(frequence[alpha[i+(len(alpha)//2)]]*100),end='\n',file=fichier )            
          
        print('</table></section>',end='\n',file=fichier )    
        print('<footer>DIU-Bloc1  </footer></body></html>',end='\n',file=fichier )
        fichier.close()
  except FileNotFoundError:
        print("Erreur ouverture de Fichier")
      

def gen_dico_vide(freqalpha,alpha):
    """générer un dictionnaire vide associant 0 avec les lettres présentes dans 
        la liste alpha
        :param freqalpha: dictionnaire vide en entrée modifié dans la fonction
                            associant une lettre de alpha avec la valeur 0                 
        :type freqalpha: dictionnaire  
        :param alpha: la liste des lettres de l'alphabet
        :type alpha: liste                
    """   
    for i in range(len(alpha)):
         freqalpha[alpha[i]] = 0
    print(freqalpha)
         
         
def calcul_frequence(freqalpha, nomfichier):
    """ compléter le dictionnaire vide de fréquence d'une lettre en utilisant 
        un fichier de mots pour la fréquence
        :param nomFichier: le nom du fichier à lire
        :type nomFichier:  String
        :param freqalpha: dictionnaire vide en entrée modifié dans la fonction
                            associant une lettre avec sa fréquence dans le fichier
        :type freqalpha: dictionnaire                 
    """       
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
    """ compléter le dictionnaire vide de probabilité d'une lettre en utilisant 
        un fichier de mots pour la probabilité
        :param nomFichier: le nom du fichier à lire
        :type nomFichier:  String
        :param probaalpha: dictionnaire vide en entrée modifié dans la fonction
                            associant une lettre avec sa probabilité d'apparition dans un mot
        :type probaalpha: dictionnaire                 
    """     
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
   
def demo_v2(lettres, frequence ):
    """ Trouver la lettre dont la fréquence est maximum, qui n'a pas déjà été proposée.
        :param lettres: la liste des lettres déjà proposées
        :type lettres: liste 
        :param frequence: dictionnaire associant une lettre avec sa fréquence
        :type frequence: dictionnaire         
        :return l:  la lettre 
        :rtype: string          
    """ 
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

def demo_v1(lettres):
    """ tire une lettre au hasard vérifie qu'elle n'a pas été proposée
        retourne la lettre
        :param lettres: la liste des lettres déjà proposées
        :type lettres: liste 
        :return l:  la lettre 
        :rtype: string          
    """ 
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

def choisi_mot(nbmax,nomfichier):
    """ ouvre et lit le fichier contenant des mots francais
        tire un mot au hasard vérifie qu'il ne dépasse pas nbmax en longueur 
        élimine les accents et retourne le mot
        :param nbmax: le nombre de lettre maximum du mot
        :type nbmax:  entier integer        
        :param nomfichier: le nom du fichier à lire
        :type nomFichier:  String
        :return: inconnu le mot à deviner ou vide si fichier n'existe pas
        :rtype: string          
    """      
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
    """ prend un mot avec accent et autres lettres spéciales 
        retourne le mot sans accent
        :param inconnu: le mot avec accent 
        :type inconnu:  string   
        :return: inconnu le mot sans accent
        :rtype: string      
    """    
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
   
def genere_tirets(n):
    """ permet de générer une liste de tirets représentant les lettres à trouver
        :return: ch 
        :rtype: liste       
    """
    ch=[]   
    for i in range(n):
        ch.append("-")
    return ch

def lettre_presente(tab,l):    
    """ vérifier si la lettre proposée est dans le mot à trouver
        :param tab: la liste des lettres du mot à trouver
        :type tab:  list
        :param l: la proposition dans la première position d'une liste
        :type l: list 
        :rtype: booleen   
    """
    for i in range(len(tab)):
        if(tab[i]==l[0]):
            return True
    return False
    
def devoiler_lettre(sol,prop,l):
    """ Montre la lettre dans le tableau de proposition
        :param sol: la liste des lettres du mot à trouver
        :type sol:  list
        :param prop: cette liste sera modifiée en remplaçant les tirets par la lettre 
        :type prop:  list        
        :param l: la proposition dans la première position d'une liste
        :type l: list 
    """
    for i in range(len(sol)):
        if(sol[i]==l[0]):
            prop[i]=sol[i]

def test_gagner(sol,prop): # if(sol == prop)
    """ Vérifie si la proposition est bonne 
        :param sol: la liste des lettres du mot à trouver
        :type sol:  list
        :param prop: cette liste sera modifiée en remplaçant les tirets par la lettre 
        :type prop:  list        
        :rtype: booleen 
    """     
    for i in range(len(sol)):
        if(sol[i]!=prop[i]):
            return False
    return True

def dessin_pendu(feutre,etape, placement): 
    """ dessine la partie du pendu correspondant à l'étape
        avec l'objet feutre permettant de tracer le pendu.
        :param feutre: l'objet permettant de dessiner sur la fenêtre
        :type feutre:  objet turtle    
        :param etape: le numéro de l'étape correspondant aux nombres d'érreurs
        :type etape:  entier integer        
        :param placement: liste des coordonnées des traits(segements) du pendu
        :type placement:  list        
    """       
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
    """ dessine du texte sur l'écran à une position, avec une couleur
        efface l'ancien message par defaut
        :param stylo: l'objet permettant de dessiner sur la fenêtre
        :type stylo:  objet turtle 
        :param texte: le message à écrire sur la fenêtre
        :type texte:  string
        :param position: une coordonnées de centrage du texte
        :type position: couple d'entiers (x,y)       
        :param couleur: mot représentant une couleur par defaut "black"
        :type couleur:  string       
        :param efface: précise si l'ancien message doit être éffacé par defaut True
        :type efface:  booleen     
    """  
    stylo.goto(position)
    if efface:
        stylo.clear()
    stylo.color(couleur)
    stylo.write(''.join(texte), align="center", font=(None, 16, "bold")) 

########################## PROG PRINCIPAL EN BOUCLE #####################################################"

def prog_principal(ihm,probaalpha):
    #liste des coordonées des segments du pendu
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

    mode=0    # variable permettant de dire si mode utilisateur 0 ou mode démo 1 et 2
    feutre= turtle.Turtle() # pour le dessin du pendu
    feutre.hideturtle() # cache le pointeur permettant de suivre la position de tracage
    stylo= turtle.Turtle() # pour afficher le tableaux de tirets
    stylo.hideturtle()# cache le pointeur permettant de suivre la position de tracage    
    stylo2= turtle.Turtle() # pour afficher les lettres déjà proposées
    stylo2.hideturtle()# cache le pointeur permettant de suivre la position de tracage     
    while mode != 3 :       # boucle pour rejouer  
        # fenetre pour le choix du mode
        msg="Choisir Mode :\n 0 - utilisateur \n 1 - demo_v1\n 2 - demo_v2 \n 3 - Quitter "
        mode = int(ihm.numinput("Mode de Jeu ", msg,minval = 0, maxval = 3))
        if mode == 3:
            return 
        # liste contenant les lettres déjà propsées
        lettresP=[]
        # compteur du nombre d'érreurs
        nberreur=0
        #partie 1
        motcache= choisi_mot(7,"liste_francaisU.txt")
        feutre.penup()
        feutre.pensize(8)       
        #pour le rebouclage
        feutre.clear()
        stylo.clear()
        stylo2.clear() 
        # Titre 
        msg ="Le Pendu DIU-Bloc1 Orsay"
        dessin_texte(feutre,msg,(-50,170),'blue',False)                   
        feutre.color("black")        
        # génère une liste de tirets correspondant au mot à chercher
        devine=genere_tirets(len(motcache))
        #partie 2
        dessin_texte(stylo,devine,placement[0])
        Trouve = False
        while (Trouve == False) and (nberreur <ERREURMAX):  # boucle par proposition de lettre 
            if mode == 0 :
                saisieCorrecte = False
                while saisieCorrecte != True :
                    msg="Lettres déjà proposées"+str(lettresP)+"\nProposition de lettre: "
                    lettre = ihm.textinput("Devinez !!!", msg)
                    if lettre != None and len(lettre) >0 and lettre[0]>='a' and lettre [0]<='z':
                        lettre = list(lettre)
                        saisieCorrecte = True          
            #partie 1
            elif mode == 1 :
                lettre = demo_v1(lettresP)
            elif mode == 2 :
                lettre = demo_v2(lettresP,probaalpha)
            lettresP.append(lettre[0])
            if(lettre_presente(motcache,lettre)==True):
                devoiler_lettre(motcache,devine,lettre)
                dessin_texte(stylo,devine,placement[0])
                msg = "lettres proposées :"+''.join(lettresP)
                dessin_texte(stylo2,msg,placement[1])
                #print("Trouvé",lettresP, "   ",''.join(devine))
                Trouve =test_gagner(motcache,devine) 
            else:
                nberreur=nberreur+1
                dessin_pendu(feutre,nberreur,placement) # dessine la partie du pendu correspondant
                dessin_texte(stylo,devine,placement[0])
                msg = "lettres proposées :"+''.join(lettresP)
                dessin_texte(stylo2,msg,placement[1])
                #print("Pas Trouvée",lettresP, "   ",''.join(devine))   
        if Trouve == True:
                msg = "Gagné ! \n La solution était : "+motcache
                dessin_texte(stylo2,msg,placement[1],'red')
        else:
                msg = "Perdu ! \n La solution était : "+motcache
                dessin_texte(stylo2,msg,placement[1],'red')

def init_fenetre():
    """ permet d'initialiser la fenêtre avec une taille sa position sur l'écran son titre
        :return: ihm l'objet de type screen permettant de faire des actions sur la fenêtre 
        :rtype: TurtleScreen        
    """
    ihm =turtle.Screen()
    ihm.setup(640, 480, 100, 100)  #Largeur : 640px, Hauteur : 480px, pos x : 100px, pos y : 100px
    ihm.setup(200, 200)  #Largeur : 200px, Hauteur : 200px, position centrée
    ihm.setup(startx = 0, starty = 0)  #Largeur : 50%, Hauteur : 75%, position : coin haut gauche écran
    ihm.setup()  #Largeur : 50%, Hauteur : 75%, position centrée
    ihm.title("Le Pendu ")  #Change le titre
    return ihm

########################## LANCEMENT DU PROG ET INITIALISATION #####################################################"
if __name__ == '__main__':
    """ Fonction spéciale débutant tous les programmes
    """  
    # dictionnaire des fréquences des lettres dans un texte en français      
    frequence = {'a' : 0.083944, 'b' : 0.007669,  'c' : 0.033297, 'd' : 0.040699, 'e' : 0.145037,
              'f' : 0.012109, 'g' : 0.009495, 'h' : 0.007973, 'i' : 0.081828, 'j' : 0.006377, 'k' : 0.000638, 'l' : 0.058405,
              'm' : 0.029355, 'n' : 0.075570, 'o' : 0.053669, 'p' : 0.032087, 'q' : 0.012613, 'r' : 0.070209, 's' : 0.080091,
              't' : 0.074775, 'u' : 0.059808, 'v' : 0.015791, 'w' : 0.000067, 'x' : 0.004098, 'y' : 0.003155, 'z' : 0.001240}              

    freqalpha = {}
    probaalpha = {}
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    

    #partie 3
    gen_dico_vide(freqalpha,alpha)
    calcul_frequence(freqalpha,"liste_francaisU.txt")
    gen_dico_vide(probaalpha,alpha)
    calcul_proba_lettre(probaalpha,"liste_francaisU.txt")
    gen_htmlP(probaalpha,alpha,"pageFrequenceProba.html")    
    gen_html(freqalpha,alpha,"pageFrequenceCalcul.html")
    gen_html(frequence,alpha,"pageFrequence.html")
    
#    #partie 2
    ihm=init_fenetre()
    prog_principal(ihm,probaalpha)
    
    ihm.exitonclick()
    turtle.bye()
