# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:35:40 2019

@author: Groupe
"""
import random
from random import *

seed(1)
nb_operation=0 #nombre d'échange de valeur dans la liste lors du tri

def creer_donnees(v_min,v_max,N,dup = True):
    tabl=[]
    if(dup==False):
        tabl=[]
        for i in range(N):
            tabl.append(randint(v_min,v_max+1))
        
        #shuffle(tabl)
        for k in range(N):
            m=randint(0,taille)
            n=m
            while(m==n):
                n=randint(0,taille)
            tabl[m],tabl[n]=tabl[n],tabl[m]
    else:
        for i in range(N):
            tabl.append(randint(v_min,v_max+1))
    return(tabl)
    
#creation d'une liste partiellement triée par echange d'élément
#argument : liste triée
#M : nombre d'échange à réaliser
def declasser_liste(lis,M):
    l=lis[:]  #copie de la liste passée en paramètre
    for i in range(M):
        i=j=randint(0,len(l)-1)
        while(i==j):
            j=randint(0,len(lis)-1)
        lis[i],lis[j]=lis[j],lis[i]


def tri_insertion(tab):
    global nb_operation
    for i in range(1,len(tab)):
        j=i
        while(tab[j]<tab[j-1]):
            tab[j],tab[j-1]=tab[j-1],tab[j]
            nb_operation+=1
            j-=1
            if(j==0):
                break

def tri_selection(tab):
    global nb_operation
    for i in range(len(tab)):
        val_min=tab[i-1]
        i_min=i-1
        for j in range(i,len(tab)-1): #trouve valeur min
            nb_operation+=1
            if(tab[j]<val_min):
                val_min=tab[j]
                i_min=j
        nb_operation+=1
        tab[i],tab[i_min]=tab[i_min],tab[i]

def tri_bulle(tab):
    global nb_operation
    permut=True
    while permut:
        permut=False
        for i in range(0,len(tab)-1):
            if(tab[i]>tab[i+1]):
                nb_operation+=1
                tab[i+1],tab[i]=tab[i],tab[i+1]
                permut=True

#fonction qui retourne une liste triée à partir de deux liste triée (liste_gauche et liste_droite) 
def fusion(Liste_gauche,Liste_droite): 
    global nb_operation
    resultat = [] #creation de la liste resultat
    index_gauche, index_droite = 0, 0
    while index_gauche < len(Liste_gauche) and index_droite < len(Liste_droite):
 
        if Liste_gauche[index_gauche] <= Liste_droite[index_droite]:
            resultat.append(Liste_gauche[index_gauche])
            index_gauche += 1
 
        else:
            resultat.append(Liste_droite[index_droite])
            index_droite += 1
        nb_operation+=1
    if Liste_gauche:
        resultat.extend(Liste_gauche[index_gauche:])
 
    if Liste_droite:
        resultat.extend(Liste_droite[index_droite:])
    return resultat
  
def tri_fusion(L):
    global nb_operation
    if len(L) <= 1:
        return L
 
    milieu = len(L) // 2
 
    #decoupe de la liste L en deux sous liste Liste_gauche et Liste_droite
    Liste_gauche = L[:milieu] 
    Liste_droite = L[milieu:]
     
    Liste_gauche = tri_fusion(Liste_gauche)# la même chose pour Liste_gauche
    Liste_droite = tri_fusion(Liste_droite)# la même chose pour Liste_droite
     
    return fusion(Liste_gauche, Liste_droite) #fusionner Liste_gauche et Liste_droite        

#la segmentation du tableau autour d'un pivot choisi et
# il renvoie l'indice a où se trouve le pivot
def partition(t, i, j):
    global nb_operation
    p = t[j-1]  
    a = i
    for b in range(i, j-1):
        if t[b] < p:
            nb_operation+=1
            t[a], t[b] = t[b], t[a]
            a += 1
    nb_operation+=1
    t[a], t[j-1] = t[j-1], t[a]
    return a

#Les deux sous-tableaux de part et d'autre du pivot sont triés         
def triRapide(t, *args):
    global nb_operation
    if len(args) == 0:
        i, j = 0, len(t)
    else:
        i , j = args
    if i + 1 < j:
        a = partition(t, i, j)
        triRapide(t, i, a)
        triRapide(t, a + 1, j)


import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


N_list = range(100,2000,10)
Timelist1_insertion=[]
operationlist1_insertion=[]

Timelist1_selection=[]
operationlist1_selection=[]

Timelist1_fusion=[]
operationlist1_fusion=[]

Timelist1_bulle=[]
operationlist1_bulle=[]

Timelist1_rapide=[]
operationlist1_rapide=[]


print("listes quelconques")
for N in N_list:
    #print("taille de liste %d"%(N),end=' ')
    l_original=creer_donnees(0,2**32,N)
    
    
    l[:]=l_original[:]
    ti=time.process_time()  #temps écoulé pou le processus courant
    nb_operation=0
    tri_insertion(l)
    ts=time.process_time()
    Timelist1_insertion.append(ts-ti)
    operationlist1_insertion.append(nb_operation)


    l[:]=l_original[:]    
    ti=time.process_time()  #temps écoulé pou le processus courant
    nb_operation=0
    tri_selection(l)
    ts=time.process_time()
    Timelist1_selection.append(ts-ti)
    operationlist1_selection.append(nb_operation)
    

    l[:]=l_original[:]
    ti=time.process_time()  #temps écoulé pou le processus courant
    nb_operation=0
    tri_bulle(l)
    ts=time.process_time()
    print("DEBUG N=%d temps de tri = %f op=%d"%(N,ts-ti,nb_operation))
    Timelist1_bulle.append(ts-ti)
    operationlist1_bulle.append(nb_operation)

    
    l[:]=l_original[:]
    ti=time.process_time()  #temps écoulé pou le processus courant
    nb_operation=0
    tri_fusion(l)
    ts=time.process_time()
    Timelist1_fusion.append(ts-ti)
    operationlist1_fusion.append(nb_operation)
    
    l[:]=l_original[:]
    ti=time.process_time()  #temps écoulé pou le processus courant
    nb_operation=0
    triRapide(l)
    ts=time.process_time()
    Timelist1_rapide.append(ts-ti)
    print("list 1 N=%d nb_op=%d"%(N,nb_operation))
    operationlist1_rapide.append(nb_operation)
    

Timelist2_insertion=[]
operationlist2_insertion=[]

Timelist2_selection=[]
operationlist2_selection=[]

Timelist2_fusion=[]
operationlist2_fusion=[]

Timelist2_bulle=[]
operationlist2_bulle=[]

Timelist2_rapide=[]
operationlist2_rapide=[]

print("listes partiellement mélangées")
for N in N_list:
    #print("taille de liste %d "%(N),end='')
    l_original=[i for i in range(N)]
    declasser_liste(l_original,int(N/4))
   
    
    l[:]=l_original[:]
    ti=time.process_time()  #temps écoulé pou le processus courant
    nb_operation=0
    tri_insertion(l)
    ts=time.process_time()
    Timelist2_insertion.append(ts-ti)
    operationlist2_insertion.append(nb_operation)


    l[:]=l_original[:]    
    ti=time.process_time()  #temps écoulé pou le processus courant
    nb_operation=0
    tri_selection(l)
    ts=time.process_time()
    Timelist2_selection.append(ts-ti)
    operationlist2_selection.append(nb_operation)
    

    l[:]=l_original[:]
    ti=time.process_time()  #temps écoulé pou le processus courant
    nb_operation=0
    tri_bulle(l)
    ts=time.process_time()
    print("DEBUG N=%d temps de tri = %f op=%d"%(N,ts-ti,nb_operation))
    Timelist2_bulle.append(ts-ti)
    operationlist2_bulle.append(nb_operation)

    
    l[:]=l_original[:]
    ti=time.process_time()  #temps écoulé pou le processus courant
    nb_operation=0
    tri_fusion(l)
    ts=time.process_time()
    Timelist2_fusion.append(ts-ti)
    operationlist2_fusion.append(nb_operation)
    
    l[:]=l_original[:]
    ti=time.process_time()  #temps écoulé pou le processus courant
    nb_operation=0
    triRapide(l)
    ts=time.process_time()
    Timelist2_rapide.append(ts-ti)
    print("list 2 N=%d nb_op=%d"%(N,nb_operation))
    operationlist2_rapide.append(nb_operation)
    

plt.clf()
plt.xlabel('N')
plt.ylabel('T')
courbe1=plt.plot(N_list, Timelist1_insertion,'r^',label="donnée aléatoire")
courbe2=plt.plot(N_list, Timelist2_insertion,'b^',label="donnée mélangées 25%")
plt.legend(['aléatoire', 'mélangées 5%'])
plt.legend()
plt.savefig("temps_insertion_alea_vs_5pct.pdf",format='pdf')

plt.clf()
plt.xlabel('N')
plt.ylabel('operation')
courbe1=plt.plot(N_list, operationlist1_insertion,'r^',label="donnée aléatoire")
courbe2=plt.plot(N_list, operationlist2_insertion,'b^',label="donnée mélangées 25%")
plt.legend(['aléatoire', 'mélangées 5%'])
plt.legend()
plt.savefig("operation_insertion_alea_vs_5pct.pdf",format='pdf')

plt.clf()
plt.xlabel('N')
plt.ylabel('T')
courbe1=plt.plot(N_list, Timelist1_selection,'r^',label="donnée aléatoire")
courbe2=plt.plot(N_list, Timelist2_selection,'b^',label="donnée mélangées 25%")
plt.legend(['aléatoire', 'mélangées 5%'])
plt.legend()
plt.savefig("temps_selection_alea_vs_5pct.pdf",format='pdf')

plt.clf()
plt.xlabel('N')
plt.ylabel('operation')
courbe1=plt.plot(N_list, operationlist1_selection,'r^',label="donnée aléatoire")
courbe2=plt.plot(N_list, operationlist2_selection,'b^',label="donnée mélangées 25%")
plt.legend(['aléatoire', 'mélangées 5%'])
plt.legend()
plt.savefig("operation_selection_alea_vs_5pct.pdf",format='pdf')

plt.clf()
plt.xlabel('N')
plt.ylabel('T')
courbe1=plt.plot(N_list, Timelist1_fusion,'r^',label="donnée aléatoire")
courbe2=plt.plot(N_list, Timelist2_fusion,'b^',label="donnée mélangées 25%")
plt.legend(['aléatoire', 'mélangées 5%'])
plt.legend()
plt.savefig("temps_fusion_alea_vs_5pct.pdf",format='pdf')

plt.clf()
plt.xlabel('N')
plt.ylabel('operation')
courbe1=plt.plot(N_list, operationlist1_fusion,'r^',label="donnée aléatoire")
courbe2=plt.plot(N_list, operationlist2_fusion,'b^',label="donnée mélangées 25%")
plt.legend(['aléatoire', 'mélangées 5%'])
plt.legend()
plt.savefig("operation_fusion_alea_vs_5pct.pdf",format='pdf')

plt.clf()
plt.xlabel('N')
plt.ylabel('T')
courbe1=plt.plot(N_list, Timelist1_bulle,'r^',label="donnée aléatoire")
courbe2=plt.plot(N_list, Timelist2_bulle,'b^',label="donnée mélangées 25%")
plt.legend(['aléatoire', 'mélangées 5%'])
plt.legend()
plt.savefig("temps_bulle_alea_vs_5pct.pdf",format='pdf') 

plt.clf()
plt.xlabel('N')
plt.ylabel('operation')
courbe1=plt.plot(N_list, operationlist1_bulle,'r^',label="donnée aléatoire")
courbe2=plt.plot(N_list, operationlist2_bulle,'b^',label="donnée mélangées 25%")
plt.legend(['aléatoire', 'mélangées 5%'])
plt.legend()
plt.savefig("operation_bulle_alea_vs_5pct.pdf",format='pdf')

plt.clf()
plt.xlabel('N')
plt.ylabel('T')
courbe1=plt.plot(N_list, Timelist1_rapide,'r^',label="donnée aléatoire")
courbe2=plt.plot(N_list, Timelist2_rapide,'b^',label="donnée mélangées 25%")
plt.legend(['aléatoire', 'mélangées 5%'])
plt.legend()
plt.savefig("temps_rapide_alea_vs_5pct.pdf",format='pdf')

plt.clf()
plt.xlabel('N')
plt.ylabel('operation')
courbe1=plt.plot(N_list, operationlist1_rapide,'r^',label="donnée aléatoire")
courbe2=plt.plot(N_list, operationlist2_rapide,'b^',label="donnée mélangées 25%")
plt.legend(['aléatoire', 'mélangées 5%'])
plt.legend()
plt.savefig("operation_rapide_alea_vs_5pct.pdf",format='pdf')

