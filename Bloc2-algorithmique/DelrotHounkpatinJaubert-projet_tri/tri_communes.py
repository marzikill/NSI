#-*- coding: Utf-8 -*-

'''
Prgramme de tri appliqué à une liste de commune de France enregistrée au fromat CSV
conversion de fichiers CSV en tuples
fonctions de tri par insertion et sélection
Appel des fonctions et mesure du temps de traitement.

Auteurs : Groupe
juillet 2019
'''
from time import time


######################################################
# fonctions de lecture/ecriture de fichiers          #
######################################################

def lecture_fichier(filename):
    ''' ouvre un fichier de type CSV et convertit chaque ligne
    en N° de département, nom de la commune, population
    le séparateur attendu est la virgule
    la fonction retourne une liste de tuples (dep, nom, population)
    '''
    
    commune=[]              # liste de tuples à remplir
      
    f = open(filename,"r")
    s='init'

    while s!='':                #si on est en fin de fichie la méthode readline retourne une chaîne vide
        s= f.readline()
        if s=='' :
            f.close()
            return commune
        ls=''
        i=0
        while (s[i]!=','):  # extraction du N° de département 
            ls= ls+s[i]
            i+=1
        dep=int(ls)
       
        i+=1
        ls=''
        while (s[i]!=','): # extraction du Nom de la commune 
            ls= ls+s[i]
            i+=1;
        nom=ls
        
        i+=1
        ls=''
        while (s[i]!='\n'): # extraction de la population
            # ATTENTION remember caractères blancs ?
            ls= ls+s[i]      
            i+=1
        
        population = int (ls)
       
        commune.append((dep, nom, population))
        
    f.close()
    return commune

def Ecriture_fichier(t,file_name):
    '''
    écriture au format csv, séparateur virgule
    N° de département, nom de la commune, population
    '''
    s=''
    
    for i in range (0,len(t)):
        s = s + str(t[i][0])+','+ t[i][1] + ','+ str(t[i][2])+ '\n'
    
    f = open(file_name,"w")
    f.write(s);
    f.close();
    return


######################################################
#           fonctions de tri                         #
######################################################


def tri_insertion(tableau_tuple):
   
    for i in range (1,len(tableau_tuple)):
        v= tableau_tuple[i] 
        j=i-1
        while( j>=0 and tableau_tuple[j][2]> v[2]):
            tableau_tuple[j+1] = tableau_tuple[j]
            j = j-1
        tableau_tuple[j+1] = v
    return tableau_tuple

def indice_min(tableau_tuple,j):
    #retour l'indice du minimum du sous tableau T[j:]
    mini = j
    for i in range(j+1,len(tableau_tuple)):
        if tableau_tuple[i][2] < tableau_tuple[mini][2]:
            mini = i
    return mini

# Nous pouvons maintenant implémenter facilement le tri par sélection
def tri_selection(tableau_tuple):
    for k in range(len(tableau_tuple)-1): # le dernier element sera forcement trie
        iMin = indice_min(tableau_tuple,k)
        if iMin != k: #A quoi ça sert ?
            tableau_tuple[iMin],tableau_tuple[k] = tableau_tuple[k],tableau_tuple[iMin]
    return tableau_tuple  #Par commodité (car T modifié)
       


######################################################
#           Programme principal / tests              #
######################################################
   

f = 'population_ain.csv'

c = lecture_fichier(f)
print (c, '\n')

start = time()
c2 = tri_insertion(c)
elapsed = time()-start
print (c2, '\n', 'temps de tri : ', elapsed)

''' mesure des temps de traitement releves pour tri insertion 
1 departement : 0.012 s
5 dpartements : 0.358 s
10 departement : 1.31 s
France entiere : 137 s

 mesure des temps de traitement releves pour  tri selection
1 departement : 0.019 s
5 dpartements : 0.310 s
10 departement : 1.14 s
France entiere : 
'''

Ecriture_fichier(c2,'population_triee.csv')

