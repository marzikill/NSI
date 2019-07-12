"""
Created on Fri Jun 21 13:39:28 2019

@author: jperron
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from tkinter import *
from tkinter.filedialog import *
import time



# -*- coding: utf-8 -*-


import random


random.seed(a=1)        # pour avoir la même graine (valeur de a) ou pas
"""
Générations des listes
"""
def genere_liste(min,max,N,dup=True):
    if not dup and N>max-min+1:
        N=max-min+1
    liste=[]
    while len(liste)<N:
        current=random.randint(min,max)
        if (not current in liste) or dup:
            liste.append(current)          
    return liste

def declasser_listeTriee(listeTriee,M):
    listedeclassee=listeTriee[:]
    for i in range(0,M):
        a=random.randint(0,len(listeTriee)-1)
        b=random.randint(0,len(listeTriee)-1)
        listedeclassee[a],listedeclassee[b]=listedeclassee[b],listedeclassee[a]
    return listedeclassee


"""
algorithmes de tris
"""
def tri_bulle (L) :
    permutation = True
    #L=liste[:]
    n=len(L)
    while permutation==True : #on répéte la procédure tant qu'on a trouvé une permutation (c-à-d L[i]&gt;L[i+1] l'élément e de la liste est plus grand que l'élément qui le suit)
     
        permutation = False # on considère qu'il n'existe aucune permutation (c-à-d la liste est triée)
     
        for  i  in range( n-1) : # on parcour la liste pour chercher s'il y une permutation
            if L[i] > L[i+1] :
                permutation = True # permutation existe on change la variable permutation en True
                L[i],L[i+1]= L[i+1],L[i] # on met L[i] et L[i+1] en ordre
                 
    return L

def tri_bulle_ce (L) :
    permutation = True
    #L=liste[:]          # 
    n=len(L)
    c=0
    e=0
    while permutation==True : #on répéte la procédure tant qu'on a trouvé une permutation (c-à-d L[i]&gt;L[i+1] l'élément e de la liste est plus grand que l'élément qui le suit)
     
        permutation = False # on considère qu'il n'existe aucune permutation (c-à-d la liste est triée)
     
        for  i  in range( n-1) : # on parcour la liste pour chercher s'il y une permutation
            if L[i] > L[i+1] :
                permutation = True # permutation existe on change la variable permutation en True
                L[i],L[i+1]= L[i+1],L[i] # on met L[i] et L[i+1] en ordre
                c=c+1
                e=e+1
    return c,e

#fonction qui retourne une liste triée à partir de deux liste triée (liste_gauche et liste_droite) 
def fusion(Liste_gauche,Liste_droite): 
 
    resultat = [] #initiation de la liste resultat
    index_gauche, index_droite = 0, 0
    while index_gauche < len(Liste_gauche) and index_droite < len(Liste_droite):
 
        if Liste_gauche[index_gauche] <= Liste_droite[index_droite]:
            resultat.append(Liste_gauche[index_gauche])
            index_gauche += 1
 
        else:
            resultat.append(Liste_droite[index_droite])
            index_droite += 1
 
    if Liste_gauche:
        resultat.extend(Liste_gauche[index_gauche:])
 
    if Liste_droite:
        resultat.extend(Liste_droite[index_droite:])
    return resultat
  
def tri_fusion(L):
 
    if len(L) <= 1:
        return L
 
    milieu = len(L) // 2
 
    #decoupe de la liste L en deux sous liste Liste_gauche et Liste_droite
    Liste_gauche = L[:milieu] 
    Liste_droite = L[milieu:]
     
    Liste_gauche = tri_fusion(Liste_gauche)# la même chose pour Liste_gauche
    Liste_droite = tri_fusion(Liste_droite)# la même chose pour Liste_droite
     
    return fusion(Liste_gauche, Liste_droite) #fusionner Liste_gauche et Liste_droite


def Tri_par_insertion(L):
    #L=l[:]
    for i in range(1, len(L)):  
        temp=L[i] # à l'itération i la liste L de l'indice 0 à j=i-1 est trié et on insert L[i]=temp
        j = i - 1
         
        while   j >=0 and L[j] > temp: # on cherche l'indice de 0 à i-1 où il faut inserer L[i]=temp
            L[j+1] = L[j]
            j -= 1
         
        L[j+1] = temp  # on insert L[i] à sa position 
         
    return L

def Tri_par_insertion_ce(L):
    c=0
    e=0
    #L=l[:]
    for i in range(1, len(L)):  
        temp=L[i] # à l'itération i la liste L de l'indice 0 à j=i-1 est trié et on insert L[i]=temp
        j = i - 1
        e=e+1 
        while   j >=0 and L[j] > temp: # on cherche l'indice de 0 à i-1 où il faut inserer L[i]=temp
            L[j+1] = L[j]
            j -= 1
            c=c+2
            e=e+1
         
        L[j+1] = temp  # on insert L[i] à sa position 
        e=e+1
    return c,e

def tri_rapide(L):
    """trirapide(L): tri rapide (quicksort) de la liste L"""
    def trirap(L, g, d):
        pivot = L[(g+d)//2]
        i = g
        j = d
        while True:
            while L[i]<pivot:
                i+=1
            while L[j]>pivot:
                j-=1
            if i>j:
                break
            if i<j:
                L[i], L[j] = L[j], L[i]
            i+=1
            j-=1
        if g<j:
            trirap(L,g,j)
        if i<d:
            trirap(L,i,d)
 
    g=0
    d=len(L)-1
    trirap(L,g,d)

def tri_rapide_ce(L):
    
    """trirapide(L): tri rapide (quicksort) de la liste L"""
    def trirapce(L, g, d):
        global ct
        global et
        pivot = L[(g+d)//2]
        i = g
        j = d
        while True:
            while L[i]<pivot:
                i+=1
                ct=ct+1
            while L[j]>pivot:
                j-=1
                ct=ct+1
            if i>j:
                break
            if i<j:
                L[i], L[j] = L[j], L[i]
            i+=1
            j-=1
            ct=ct+2
            et=et+3
            
        if g<j:
            ct=ct+1
            trirapce(L,g,j)
        if i<d:
            ct=ct+2
            trirapce(L,i,d)
 
    g=0
    d=len(L)-1
    trirapce(L,g,d)
    
def fusionce(Liste_gauche,Liste_droite): 
    global cf
    global ef
    resultat = [] #initiation de la liste resultat
    index_gauche, index_droite = 0, 0
    while index_gauche < len(Liste_gauche) and index_droite < len(Liste_droite):
        cf=cf+2
        if Liste_gauche[index_gauche] <= Liste_droite[index_droite]:
            resultat.append(Liste_gauche[index_gauche])
            index_gauche += 1
            cf=cf+1
            ef=ef+1
 
        else:
            resultat.append(Liste_droite[index_droite])
            index_droite += 1
            cf=cf+1
            ef=ef+1
    if Liste_gauche:
        resultat.extend(Liste_gauche[index_gauche:])
        cf=cf+1
        ef=ef+len(Liste_gauche)-index_gauche
    if Liste_droite:
        resultat.extend(Liste_droite[index_droite:])
        cf=cf+2
        ef=ef+len(Liste_droite)-index_droite
    return resultat
  
def tri_fusionce(L):
    global cf
    global ef
    
    if len(L) <= 1:
        return L
 
    milieu = len(L) // 2
 
    #decoupe de la liste L en deux sous liste Liste_gauche et Liste_droite
    Liste_gauche = L[:milieu] 
    Liste_droite = L[milieu:]
    ef=ef+len(L)
    Liste_gauche = tri_fusionce(Liste_gauche)# la même chose pour Liste_gauche
    Liste_droite = tri_fusionce(Liste_droite)# la même chose pour Liste_droite
     
    return fusionce(Liste_gauche, Liste_droite) #fusionner Liste_gauche et Liste_droite


def calculs():
    # récupérations de l'état des boutons
    tri_insertion_on=btri_insertion_on.get()
    tri_bulle_on=btri_bulle_on.get()
    tri_rapide_on=btri_rapide_on.get()
    tri_fusion_on=btri_fusion_on.get()
    aff_qcq_on=baff_qcq_on.get()
    aff_trie_on=baff_trie_on.get()
    aff_psqtrie_on=baff_psqtrie_on.get()
    aff_inverse_on=baff_inverse_on.get()
    comp_on=baff_comp_on.get()
    taille_big=baff_taille_big.get()
    nb_repet=baff_repet.get()
    
    global N_list
    """
    Génération des nombres N utilisés
    """
    N_list=[0]*21
    for p in range(0,21):
        if taille_big:
            N_list[p]=int(10**(p/8+1))
        else:
            N_list[p]=p*5+5
    
    """
    création des listes de temps et nombre de tests pour
    les différentes valeurs de N
    """
    global Time_qcq_i,Time_qcq_b,Time_qcq_r,Time_qcq_f 
    global Time_trie_i,Time_trie_b,Time_trie_r,Time_trie_f
    global Time_inverse_i,Time_inverse_b,Time_inverse_r,Time_inverse_f
    global Time_psqtrie_i,Time_psqtrie_b,Time_psqtrie_r,Time_psqtrie_f
    global c_qcq_i,c_qcq_b,c_qcq_r,c_qcq_f    
    global c_trie_i,c_trie_b,c_trie_r,c_trie_f
    global c_inverse_i,c_inverse_b,c_inverse_r,c_inverse_f
    global c_psqtrie_i,c_psqtrie_b,c_psqtrie_r,c_psqtrie_f     
    global e_qcq_i,e_qcq_b,e_qcq_r,e_qcq_f 
    global e_trie_i,e_trie_b,e_trie_r,e_trie_f
    global e_inverse_i,e_inverse_b,e_inverse_r,e_inverse_f
    global e_psqtrie_i,e_psqtrie_b,e_psqtrie_r,e_psqtrie_f      
    global ct,et,cf,ef
        
    Time_qcq_i,Time_qcq_b,Time_qcq_r,Time_qcq_f = [],[],[],[]    
    Time_trie_i,Time_trie_b,Time_trie_r,Time_trie_f=[],[],[],[]  
    Time_inverse_i,Time_inverse_b,Time_inverse_r,Time_inverse_f=[],[],[],[]
    Time_psqtrie_i,Time_psqtrie_b,Time_psqtrie_r,Time_psqtrie_f = [],[],[],[]       
    c_qcq_i,c_qcq_b,c_qcq_r,c_qcq_f = [],[],[],[]
    c_trie_i,c_trie_b,c_trie_r,c_trie_f=[],[],[],[]
    c_inverse_i,c_inverse_b,c_inverse_r,c_inverse_f=[],[],[],[]
    c_psqtrie_i,c_psqtrie_b,c_psqtrie_r,c_psqtrie_f=[],[],[],[]       
    e_qcq_i,e_qcq_b,e_qcq_r,e_qcq_f = [],[],[],[]
    e_trie_i,e_trie_b,e_trie_r,e_trie_f=[],[],[],[]   
    e_inverse_i,e_inverse_b,e_inverse_r,e_inverse_f=[],[],[],[]
    e_psqtrie_i,e_psqtrie_b,e_psqtrie_r,e_psqtrie_f=[],[],[],[] 

    for N in N_list:
        
        tp_i,tp_b,tp_r,tp_f=0,0,0,0              
        ctp_i,ctp_b,ctp_r,ctp_f=0,0,0,0     
        etp_i,etp_b,etp_r,etp_f=0,0,0,0
        
        
        
        for i in range(nb_repet):
                    
            l = genere_liste(0, 2**32, N)
            
            li,lb,lr,lf=l[:],l[:],l[:],l[:]                       
            lci,lcb,lcr,lcf=l[:],l[:],l[:],l[:]
                        
            if tri_insertion_on:
            
                ti = time.perf_counter()
                Tri_par_insertion(li)
                ts = time.perf_counter()
                tp_i=tp_i+ts-ti
                if comp_on:
                    c,e=Tri_par_insertion_ce(lci)
                    ctp_i=ctp_i+c
                    etp_i=etp_i+e
                
            if tri_bulle_on:
            
                ti = time.perf_counter()
                tri_bulle(lb)
                ts = time.perf_counter()
                tp_b=tp_b+ts-ti
                if comp_on:
                    c,e=tri_bulle_ce(lcb)
                    ctp_b=ctp_b+c
                    etp_b=etp_b+e
               
            if tri_rapide_on:
            
                ti = time.perf_counter()
                tri_rapide(lr)
                ts = time.perf_counter()
                tp_r=tp_r+ts-ti
                if comp_on:
                    ct=0
                    et=0
                    tri_rapide_ce(lcr)
                    ctp_r=ctp_r+ct
                    etp_r=etp_r+et
               
            if tri_fusion_on:
            
                ti = time.perf_counter()
                tri_fusion(lf)
                ts = time.perf_counter()
                tp_f=tp_f+ts-ti
                if comp_on:
                    cf=0
                    ef=0
                    tri_fusionce(lcf)
                    ctp_f=ctp_f+cf
                    etp_f=etp_f+ef
               
    
        Time_qcq_i.append(tp_i/nb_repet)
        Time_qcq_b.append(tp_b/nb_repet)
        Time_qcq_r.append(tp_r/nb_repet)
        Time_qcq_f.append(tp_f/nb_repet)
        
        c_qcq_i.append(ctp_i/nb_repet)
        c_qcq_b.append(ctp_b/nb_repet)
        c_qcq_r.append(ctp_r/nb_repet)
        c_qcq_f.append(ctp_f/nb_repet)
        
        e_qcq_i.append(etp_i/nb_repet)
        e_qcq_b.append(etp_b/nb_repet)
        e_qcq_r.append(etp_r/nb_repet)
        e_qcq_f.append(etp_f/nb_repet)
             
        l.sort()                        # l contient la liste triée
    
        if tri_insertion_on:
            ti = time.perf_counter()
            Tri_par_insertion(l)
            ts = time.perf_counter()
            Time_trie_i.append(ts-ti)
        
            l.reverse()         # attention l devient trié dans le sens inverse
            ti = time.perf_counter()
            Tri_par_insertion(l)                    # l redevient trié
            ts = time.perf_counter()
            Time_inverse_i.append(ts-ti)
            if comp_on:
                    c,e=Tri_par_insertion_ce(l)
                    c_trie_i.append(c)
                    e_trie_i.append(e)
                    l.reverse()
                    c,e=Tri_par_insertion_ce(l)
                    c_inverse_i.append(c)
                    e_inverse_i.append(e)

        if tri_bulle_on:
            ti = time.perf_counter()
            tri_bulle(l)
            ts = time.perf_counter()
            Time_trie_b.append(ts-ti)
        
            l.reverse()         # attention l devient trié dans le sens inverse
            ti = time.perf_counter()
            tri_bulle(l)
            ts = time.perf_counter()
            Time_inverse_b.append(ts-ti)
            if comp_on:
                c,e=tri_bulle_ce(l)
                c_trie_b.append(c)
                e_trie_b.append(e)                  
                l.reverse()
                c,e=tri_bulle_ce(l)
                c_inverse_b.append(c)
                e_inverse_b.append(e)

        if tri_rapide_on:
            ti = time.perf_counter()
            tri_rapide(l)
            ts = time.perf_counter()
            Time_trie_r.append(ts-ti)
        
            l.reverse()         # attention l devient trié dans le sens inverse
            ti = time.perf_counter()
            tri_rapide(l)
            ts = time.perf_counter()
            Time_inverse_r.append(ts-ti)
            if comp_on:
                    ct=0
                    et=0
                    tri_rapide_ce(l)
                    c_trie_r.append(ct)
                    e_trie_r.append(et)
                    l.reverse()
                    ct=0
                    et=0
                    tri_rapide_ce(l)
                    c_inverse_r.append(ct)
                    e_inverse_r.append(et)

        if tri_fusion_on:
            ti = time.perf_counter()
            tri_fusion(l)
            ts = time.perf_counter()
            Time_trie_f.append(ts-ti)
        
            l.reverse()         # attention l devient trié dans le sens inverse
            ti = time.perf_counter()
            tri_fusion(l)
            ts = time.perf_counter()
            Time_inverse_f.append(ts-ti)
            if comp_on:
                    cf=0
                    ef=0
                    tri_fusionce(l)
                    c_trie_f.append(cf)
                    e_trie_f.append(ef)
                    l.reverse()
                    cf=0
                    ef=0
                    tri_fusionce(l)
                    c_inverse_f.append(cf)
                    e_inverse_f.append(ef)

    """
    Variante pour avoir plusieurs % de déclassement

    
    Time_psqtri1,Time_psqtri5,Time_psqtri10 = [],[],[]
    c_psqtri=[]                 
    for N in N_list:
        tp1,tp5,tp10=0,0,0
        cpt=0
        for i in range(nb_repet):
            l = genere_liste(0, 2**32, N)
            l.sort()
            l1 = declasser_listeTriee(l, int(N/100))  # 99%
            l5 = declasser_listeTriee(l, int(N/20))   # 95%
            l10 = declasser_listeTriee(l, int(N/10))  # 90%
            #lc=l[:]
            ti = time.perf_counter()
            tri_bulle(l1)
            ts = time.perf_counter()
            tp1=tp1+ts-ti
            ti = time.perf_counter()
            tri_bulle(l5)
            ts = time.perf_counter()
            tp5=tp5+ts-ti
            ti = time.perf_counter()
            tri_bulle(l10)
            ts = time.perf_counter()
            tp10=tp10+ts-ti
            cpt=cpt+tri_bulle_ce(lc)
            Time_psqtri1.append(tp1/nb_repet)
            Time_psqtri5.append(tp5/nb_repet)
            Time_psqtri10.append(tp10/nb_repet)
            c_psqtri.append(cpt/nb_repet)
    """
    av=0               
    for N in N_list:
        
        tp_i,tp_b,tp_r,tp_f=0,0,0,0              
        cpt_i,cpt_b,cpt_r,cpt_f=0,0,0,0
        ept_i,ept_b,ept_r,ept_f=0,0,0,0
        av=av+1
        avancement.set(str(av))        
        for i in range(nb_repet):
            l = genere_liste(0, 2**32, N)
            l.sort()
            #l1 = declasser_listeTriee(l, int(N/100))   1%
            l5 = declasser_listeTriee(l, int(N/20))     # 5%
            #l10 = declasser_listeTriee(l, int(N/10))   10%
            
            li,lb,lr,lf=l5[:],l5[:],l5[:],l5[:]                      
            lci,lcb,lcr,lcf=l5[:],l5[:],l5[:],l5[:]
            
            if tri_insertion_on: 
                ti = time.perf_counter()
                Tri_par_insertion(li)
                ts = time.perf_counter()
                tp_i=tp_i+ts-ti
                if comp_on:
                    c,e=Tri_par_insertion_ce(lci)
                    cpt_i=cpt_i+c
                    ept_i=ept_i+e
                
            if tri_bulle_on: 
                ti = time.perf_counter()
                tri_bulle(lb)
                ts = time.perf_counter()
                tp_b=tp_b+ts-ti
                if comp_on:
                    c,e=tri_bulle_ce(lcb)
                    cpt_b=cpt_b+c
                    ept_b=ept_b+e
                    
            if tri_rapide_on: 
                ti = time.perf_counter()
                tri_rapide(lr)
                ts = time.perf_counter()
                tp_r=tp_r+ts-ti
                if comp_on:
                    ct=0
                    et=0
                    tri_rapide_ce(lcr)
                    cpt_r=cpt_b+ct
                    ept_r=ept_b+et
                    
            if tri_fusion_on: 
                ti = time.perf_counter()
                tri_fusion(lf)
                ts = time.perf_counter()
                tp_f=tp_f+ts-ti
                if comp_on:
                    cf=0
                    ef=0
                    tri_fusionce(lcf)
                    cpt_f=cpt_f+cf
                    ept_f=ept_f+ef
    
        Time_psqtrie_i.append(tp_i/nb_repet)
        Time_psqtrie_b.append(tp_b/nb_repet)
        Time_psqtrie_r.append(tp_r/nb_repet)
        Time_psqtrie_f.append(tp_f/nb_repet)
        
        if comp_on:
            c_psqtrie_i.append(cpt_i/nb_repet)
            c_psqtrie_b.append(cpt_b/nb_repet)
            c_psqtrie_r.append(cpt_r/nb_repet)
            c_psqtrie_f.append(cpt_f/nb_repet)
            
            e_psqtrie_i.append(ept_i/nb_repet)
            e_psqtrie_b.append(ept_b/nb_repet)
            e_psqtrie_r.append(ept_r/nb_repet)
            e_psqtrie_f.append(ept_f/nb_repet)
    
           
        """
        Sauvegarde des données temps dans tri.csv
        """
        """
        fichierCsv = open("tri.csv", "w")       # crée le fichier tri.csv
        fichierCsv.write("N,Aléatoires,Presques_triées,Triées,Inversées\n")   # on passe les entêtes du fichier csv et \n pour indiquer la fin de ligne (on passe à la ligne suivante dans le fichier csv)
        fichierCsv.close()
        fichierCsv = open("tri.csv", "a")
        for p in range(0,21):
            fichierCsv = open("tri.csv", "a")
            fichierCsv.write(str(N_list[p])+","+str(Time_qcq[p])+","+str(Time_psqtri5[p])+","+str(Time_trie[p])+","+str(Time_inverse[p])+"\n")
            fichierCsv.close()

            """
    """
    sans variable globale
    
    return Time_qcq_i,Time_qcq_b,Time_qcq_r,Time_qcq_f,\
    Time_trie_i,Time_trie_b,Time_trie_r,Time_trie_f,\
    Time_inverse_i,Time_inverse_b,Time_inverse_r,Time_inverse_f,\
    Time_psqtrie_i,Time_psqtrie_b,Time_psqtrie_r,Time_psqtrie_f
    """ 
    graphique()
    return

def graphique():
    # récupérations de l'état des boutons
    tri_insertion_on=btri_insertion_on.get()
    tri_bulle_on=btri_bulle_on.get()
    tri_rapide_on=btri_rapide_on.get()
    tri_fusion_on=btri_fusion_on.get()
    aff_qcq_on=baff_qcq_on.get()
    aff_trie_on=baff_trie_on.get()
    aff_psqtrie_on=baff_psqtrie_on.get()
    aff_inverse_on=baff_inverse_on.get()
    
    aff_loglog=baff_loglog.get()
    print("aff_loglog",aff_loglog)
    comp_on=baff_comp_on.get()
    ex_on=baff_ex_on.get()
    """
    Génération du graphique
    """
    
    ax1.clear()
    ax1.set_xlabel('N')
    ax1.set_ylabel('Temps (s) -')    
    
    
    if aff_loglog==1:
        ax1.set_yscale("log")
        ax1.set_xscale("log")
        
    else:
        ax1.set_yscale("linear")
        ax1.set_xscale("linear")
        
    
    #fig,ax1=plt.subplots() 


    if tri_insertion_on:
        if aff_qcq_on:
            ax1.plot(N_list, Time_qcq_i,label="Aléatoires insertion")
        if aff_psqtrie_on:
            ax1.plot(N_list, Time_psqtrie_i,label="presques triées insertion")
        if aff_trie_on:
            ax1.plot(N_list, Time_trie_i,label="triées insertion")
        if aff_inverse_on:
            ax1.plot(N_list, Time_inverse_i,label="inversées insertion")

    if tri_bulle_on:
        if aff_qcq_on:
            ax1.plot(N_list, Time_qcq_b,label="Aléatoires bulle")
        if aff_psqtrie_on:
            ax1.plot(N_list, Time_psqtrie_b,label="presques triées bulle")
        if aff_trie_on:
            ax1.plot(N_list, Time_trie_b,label="triées bulle")
        if aff_inverse_on:
            ax1.plot(N_list, Time_inverse_b,label="inversées bulle")
   
    if tri_rapide_on:
        if aff_qcq_on:
            ax1.plot(N_list, Time_qcq_r,label="Aléatoires rapide")
        if aff_psqtrie_on:
            ax1.plot(N_list, Time_psqtrie_r,label="presques triées rapide")
        if aff_trie_on:
            ax1.plot(N_list, Time_trie_r,label="triées rapide")
        if aff_inverse_on:
            ax1.plot(N_list, Time_inverse_r,label="inversées rapide")
   
    if tri_fusion_on:
        if aff_qcq_on:
            ax1.plot(N_list, Time_qcq_f,label="Aléatoires fusion")
        if aff_psqtrie_on:
            ax1.plot(N_list, Time_psqtrie_f,label="presques triées fusion")
        if aff_trie_on:
            ax1.plot(N_list, Time_trie_f,label="triées fusion")
        if aff_inverse_on:
            ax1.plot(N_list, Time_inverse_f,label="inversées fusion")    

    legend=ax1.legend(loc=2)
    
    """
    variantes plusieurs % de presques triées
    ax1.plot(N_list, Time_qcq,label="Aléatoires")
    ax1.plot(N_list, Time_psqtri1,label="Presque triées 99%")
    ax1.plot(N_list, Time_psqtri5,label="Presque triées 95%")
    ax1.plot(N_list, Time_psqtri10,label="Presque triées 90%")
    ax1.plot(N_list, Time_trie,label="triées")
    ax1.plot(N_list, Time_inverse,label="inversées")
    """
    
    if comp_on or ex_on:
                  
        
       
        if comp_on and ex_on==False:
            ax2.set_ylabel('nb comparaisons --')
        if comp_on==False and ex_on:
            ax2.set_ylabel('nb échanges :')
        if comp_on and ex_on:
            ax2.set_ylabel('nb échanges /comparaisons --')
        ax2.clear()
        if aff_loglog==1:
            ax2.set_yscale("log")
            ax2.set_xscale("log")
        
        else:
            ax2.set_yscale("linear")
            ax2.set_xscale("linear")
        
            
        if tri_insertion_on and comp_on:
            if aff_qcq_on:
                ax2.plot(N_list, c_qcq_i,'--',label="Aléatoires insertion")
            if aff_psqtrie_on:
                ax2.plot(N_list, c_psqtrie_i,'--',label="presques triées insertion")
            if aff_trie_on:
                ax2.plot(N_list, c_trie_i,'--',label="triées insertion")
            if aff_inverse_on:
                ax2.plot(N_list, c_inverse_i,'--',label="inversées insertion")

        if tri_bulle_on and comp_on:
            if aff_qcq_on:
                ax2.plot(N_list, c_qcq_b,'--',label="Aléatoires bulle")
            if aff_psqtrie_on:
                ax2.plot(N_list, c_psqtrie_b,'--',label="presques triées bulle")
            if aff_trie_on:
                ax2.plot(N_list, c_trie_b,'--',label="triées bulle")
            if aff_inverse_on:
                ax2.plot(N_list, c_inverse_b,'--',label="inversées bulle")
   
        if tri_rapide_on and comp_on:
            if aff_qcq_on:
                ax2.plot(N_list, c_qcq_r,'--',label="Aléatoires rapide")
            if aff_psqtrie_on:
                ax2.plot(N_list, c_psqtrie_r,'--',label="presques triées rapide")
            if aff_trie_on:
                ax2.plot(N_list, c_trie_r,'--',label="triées rapide")
            if aff_inverse_on:
                ax2.plot(N_list, c_inverse_r,'--',label="inversées rapide")
   
        if tri_fusion_on and comp_on:
            if aff_qcq_on:
                ax2.plot(N_list, c_qcq_f,'--',label="Aléatoires fusion")
            if aff_psqtrie_on:
                ax2.plot(N_list, c_psqtrie_f,'--',label="presques triées fusion")
            if aff_trie_on:
                ax2.plot(N_list, c_trie_f,'--',label="triées fusion")
            if aff_inverse_on:
                ax2.plot(N_list, c_inverse_f,'--',label="inversées fusion")
    
        
        if tri_insertion_on and ex_on:
            if aff_qcq_on:
                ax2.plot(N_list, e_qcq_i,':',label="Aléatoires insertion")
            if aff_psqtrie_on:
                ax2.plot(N_list, e_psqtrie_i,':',label="presques triées insertion")
            if aff_trie_on:
                ax2.plot(N_list, e_trie_i,':',label="triées insertion")
            if aff_inverse_on:
                ax2.plot(N_list, e_inverse_i,':',label="inversées insertion")

        if tri_bulle_on and ex_on:
            if aff_qcq_on:
                ax2.plot(N_list, e_qcq_b,':',label="Aléatoires bulle")
            if aff_psqtrie_on:
                ax2.plot(N_list, e_psqtrie_b,':',label="presques triées bulle")
            if aff_trie_on:
                ax2.plot(N_list, e_trie_b,':',label="triées bulle")
            if aff_inverse_on:
                ax2.plot(N_list, e_inverse_b,':',label="inversées bulle")
   
        if tri_rapide_on and ex_on:
            if aff_qcq_on:
                ax2.plot(N_list, e_qcq_r,':',label="Aléatoires rapide")
            if aff_psqtrie_on:
                ax2.plot(N_list, e_psqtrie_r,':',label="presques triées rapide")
            if aff_trie_on:
                ax2.plot(N_list, e_trie_r,':',label="triées rapide")
            if aff_inverse_on:
                ax2.plot(N_list, e_inverse_r,'--',label="inversées rapide")
   
        if tri_fusion_on and ex_on:
            if aff_qcq_on:
                ax2.plot(N_list, e_qcq_f,':',label="Aléatoires fusion")
            if aff_psqtrie_on:
                ax2.plot(N_list, e_psqtrie_f,':',label="presques triées fusion")
            if aff_trie_on:
                ax2.plot(N_list, e_trie_f,':',label="triées fusion")
            if aff_inverse_on:
                ax2.plot(N_list, e_inverse_f,':',label="inversées fusion")                    

        legend=ax2.legend(loc=1)  
        
    canvas.draw()     
    
    #fig.tight_layout()
  
    
    #plt.savefig("graphique.png")
    #plt.close()
    #canevas.delete("all")
    #photo = PhotoImage(file="graphique.png")
    #canevas.create_image(0, 0, anchor=NW, image=photo)
   # return

  
fenetre = Tk()

fenetre.title('Comparaison de tris')
fenetre['bg']='grey'

choix=Frame(fenetre,borderwidth=2,relief=GROOVE)
choix.pack(side=RIGHT,padx=10,pady=10)
choix2=Frame(choix,borderwidth=2,relief=GROOVE)
choix2.pack(side=BOTTOM,padx=10,pady=10)

# Tri 
Tri = Frame(choix, borderwidth=2, relief=GROOVE)
Tri.pack(side=LEFT, padx=10, pady=10)
# Ajout de labels
Label(Tri, text="Choix du tri",font='helvetica 8 bold').pack(padx=10, pady=10)

# checkbutton
btri_insertion_on=IntVar()
b_i = Checkbutton(Tri, text="Insertion",variable=btri_insertion_on)
btri_bulle_on=IntVar()
b_b = Checkbutton(Tri, text="Bulle      ",variable=btri_bulle_on)
btri_rapide_on=IntVar()
b_r = Checkbutton(Tri, text="Rapide   ",variable=btri_rapide_on)
btri_fusion_on=IntVar()
b_f = Checkbutton(Tri, text="Fusion   ",variable=btri_fusion_on)
b_i.pack()
b_b.pack()
b_r.pack()
b_f.pack()

# Type
Type_liste = Frame(choix, borderwidth=2, relief=GROOVE)
Type_liste.pack(side=LEFT, padx=10, pady=10)
Label(Type_liste, text="Type de listes",font='helvetica 8 bold').pack(padx=10, pady=10)

# checkbutton
baff_qcq_on=IntVar()
b_qcq = Checkbutton(Type_liste, text="Aléatoires        ",variable=baff_qcq_on)
baff_psqtrie_on=IntVar()
b_psqtrie = Checkbutton(Type_liste, text="Presques triées",variable=baff_psqtrie_on)
baff_trie_on=IntVar()
b_trie = Checkbutton(Type_liste, text="Triées                ",variable=baff_trie_on)
baff_inverse_on=IntVar()
b_inverse = Checkbutton(Type_liste, text="Inversées          ",variable=baff_inverse_on)
b_qcq.pack()
b_psqtrie.pack()
b_trie.pack()
b_inverse.pack()

#echelle
echelle=Frame(choix2, borderwidth=2, relief=GROOVE)
echelle.pack(side=LEFT, padx=10, pady=10)
Label(echelle, text="Echelle",font='helvetica 8 bold').pack(padx=10, pady=10)
baff_loglog=IntVar()
R1=Radiobutton(echelle,text='linéaire',variable=baff_loglog,value=0)
R1.pack()
R2=Radiobutton(echelle,text='Log     ',variable=baff_loglog,value=1)
R2.pack()

#Tailel liste
taille=Frame(choix2, borderwidth=2, relief=GROOVE)
taille.pack(side=RIGHT, padx=10, pady=10)
Label(taille, text="Taille liste",font='helvetica 8 bold').pack(padx=10, pady=10)
baff_taille_big=IntVar()
R3=Radiobutton(taille,text='Petite  ',variable=baff_taille_big,value=0)
R3.pack()
R4=Radiobutton(taille,text='Grande',variable=baff_taille_big,value=1)
R4.pack()

# test temps / comparaisons
tc=Frame(choix, borderwidth=2, relief=GROOVE)
tc.pack(side=LEFT, padx=10, pady=10)
Label(tc, text="Opérations",font='helvetica 8 bold').pack(padx=10, pady=10)
baff_comp_on=IntVar()
b_comp_on = Checkbutton(tc, text="Comparaisons",variable=baff_comp_on)
b_comp_on.pack()
baff_ex_on=IntVar()
b_ex_on = Checkbutton(tc, text="Echanges        ",variable=baff_ex_on)
b_ex_on.pack()

#nb repet
nbrepet=Frame(choix2, borderwidth=2, relief=GROOVE)
nbrepet.pack(side=RIGHT, padx=10, pady=10)
Label(nbrepet, text="Nombre de répétitions",font='helvetica 8 bold').pack(padx=10, pady=10)
baff_repet=IntVar()
baff_repet.set(1)
t1=Radiobutton(nbrepet,text='1  ',variable=baff_repet,value=1)
t1.pack()
t5=Radiobutton(nbrepet,text='5  ',variable=baff_repet,value=5)
t5.pack()
t20=Radiobutton(nbrepet,text='20 ',variable=baff_repet,value=20)
t20.pack()
t100=Radiobutton(nbrepet,text='100',variable=baff_repet,value=100)
t100.pack()
t500=Radiobutton(nbrepet,text='500',variable=baff_repet,value=500)
t500.pack()

#cadre du graphique

figure=plt.Figure((7,4),dpi=72)

canvas = FigureCanvasTkAgg(figure, master=fenetre)

ax1 = figure.add_subplot(111)
ax2=ax1.twinx()
#toolbar = NavigationToolbar2Tk(canvas, fenetre).pack()
canvas._tkcanvas.pack(side=LEFT, fill=BOTH, expand=1)
avancement=StringVar()
avancement.set("avancement")
aff_avancement=Label(fenetre,textvariable=avancement)
aff_avancement.pack(side=BOTTOM)

"""
photo = PhotoImage(file="graphique.png")
canevas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="black")
canevas.create_image(0, 0, anchor=NW, image=photo)
canevas.pack()
"""
Boutoncalcul = Button(fenetre, text ='Recalculer', command = calculs)
Boutoncalcul.pack(side = BOTTOM, padx = 10, pady = 10)
Boutongraphique = Button(fenetre, text ='Graphique', command = graphique)
Boutongraphique.pack(side = LEFT, padx = 10, pady = 10)
Boutonaide = Button(fenetre, text ='Aide', command = calculs)
Boutonaide.pack(side = RIGHT, padx = 10, pady = 10)
fenetre.mainloop()









