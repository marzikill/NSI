# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:22:08 2019

@author: magali.sauvergeat
"""
# Variable globale permettant de paramétrer le nombre d'érreurs possibles
ERREURMAX=12

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

def prog_principal():

    # la version 1
    # la liste contenant les lettres du mot à trouver   
    motcache= list("octogone")
    # liste contenant les lettres déjà propsées
    lettresProp=[]
    # compteur du nombre d'érreurs
    nberreur=0
    # génère une liste de tirets correspondant au mot à chercher
    devine=genere_tirets(len(motcache))
    # Trouve : variable de la boucle permettant de sortir 
    Trouve = False
    while (Trouve == False) and (nberreur < ERREURMAX): # boucle par proposition de lettre 
        #saisir une lettre
        lettre=list(input("Faire une proposition de lettre :"))
        lettresProp.append(lettre[0])
        if(lettre_presente(motcache,lettre)==True):
            devoiler_lettre(motcache,devine,lettre)
            print("Trouvé",lettresProp, "   ",''.join(devine)) # join permet d'afficher la liste devine sous forme de mot 
            Trouve =test_gagner(motcache,devine) 
        else:
            nberreur=nberreur+1
            print("Pas Trouvée",lettresProp, "   ",''.join(devine))   
    if Trouve == True:
        print("Bravo c'est gagné en ",nberreur," érreurs")
    else:
        print("Perdu !!!  ",nberreur," érreurs")
    print("La solution était :",motcache)
    
if __name__ == '__main__':
    """ Fonction spéciale débutant tous les programmes
    """    
    prog_principal()

