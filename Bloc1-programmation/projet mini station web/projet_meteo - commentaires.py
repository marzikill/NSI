#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 20:37:11 2019

@author: brembilla
"""
#projet météo

import csv
import numpy as np
import matplotlib.pyplot as plt
import serial
import datetime

def lectureFichierCsv(url):
    # PRE   url valide
    # POST  retourne un tableau contenant les données CSV

    tableau=[]
    with open(url, newline='') as csvfile:
        lecteur = csv.reader(csvfile, delimiter=',', quotechar='"')
        for ligne in lecteur:
            tableau.append(ligne)
   
    return tableau
        
def generationImageTableau(tableau):
    # PRE   tableau des données déjà créé
    # POST  création de 3 fichiers images (T=f(T), P=f(T) et Hygro=f(T)) 

    date=[]
    heure=[]
    temperature=[]
    pression=[]
    hygrometrie=[]
    for i in range(1,len(tableau)):
        date.append(tableau[i][0])
        heure.append(tableau[i][1])
        temperature.append( float(tableau[i][2]))       # il faut redéfinir le format flottant.
        pression.append( float(tableau[i][3]))          # idem
        hygrometrie.append(float(tableau[i][4]))        # idem
    
    
    x = np.array(heure)
    yt = np.array(temperature)
    yp = np.array(pression)
    yh = np.array(hygrometrie)
 
    creationImage(x,yt,["relevé de température","Température"])
    creationImage(x,yp,["relevé de pression","Pression"])
    creationImage(x,yh,["relevé d'hygrométrie","Hygrométrie"])
    
def creationImage(x,y,noms):
    # PRE   x contient une liste de temps valide, y contient une liste valide de la grandeur dépendante du temps G
    # POST  crée le graphique G=f(t) et le sauvegarde dans le fichier nom.png

    plt.title(noms[0])
    plt.ylabel(noms[1])
    plt.xlabel('Heure')
    plt.grid(True)
    plt.plot(x, y)
    plt.xticks(x, rotation=60)                          # rotation pour une meilleure lecture du graphique
    plt.subplots_adjust(bottom=0.3)
    plt.savefig("graphique"+noms[1]+".png")
    plt.close()
    
        
def generationPageHtml(tableau):
    # PRE   tableau des données déjà créé, les 3 images au format png sont déjà crées
    # POST  génère le fichier html "page.html" contenant un tableau avec les valeurs brutes T=f(T), P=f(T) et Hygro=f(T) et les 3 graphiques correspondants

    fichier = open("page.html", "w") #"w" pour write (ecrase le fichier si il existe) ou "a" pour append (ecrit à la suite du fichier)
    fichier.write("<!DOCTYPE html>\n")
    fichier.write('<html lang="fr">\n')
    fichier.write('<head>\n')
    fichier.write('<meta charset="utf-8">\n')
    fichier.write('<title>Ma page météo</title>\n')
    fichier.write('<link rel="stylesheet" media="screen" type="text/css" title="Design" href="design.css" />\n')
    fichier.write('<meta http-equiv="refresh" content="2" />')#<meta http-equiv="refresh" content="x;y" /> x un seconde et y l'url de la page pas nécessaire si même page
    fichier.write('</head>\n')
    fichier.write('<body>\n')
    generationTableauHtml(tableau,fichier)
    fichier.write('<img src="graphiqueTempérature.png" alt="image des données"/>\n')
    fichier.write('<img src="graphiquePression.png" alt="image des données"/>\n')
    fichier.write('<img src="graphiqueHygrométrie.png" alt="image des données"/>\n')
    fichier.write('</body>\n')
    fichier.write('</html>')
    fichier.close()

def generationTableauHtml(tableau,fichier):
    # PRE   tableau des données déjà créé
    # POST  écrit le tableau des données dans la page html

    fichier.write('<table>')
    fichier.write('<caption>Données Brutes</caption>')
    fichier.write('<tr>')
    for item in tableau[0]:
            fichier.write('<th>'+item+'</th>')
    fichier.write('</tr>\n')
    
    for i in range(1,len(tableau)):
        
        fichier.write('<tr>')
        for item in tableau[i]:
            fichier.write('<td>'+item+'</td>')
        fichier.write('</tr>\n')
      
    fichier.write('</table>\n')
   
url='donnees.csv'
   
ser = serial.Serial('/dev/ttyACM1', 9600)   # mettre le nom du port sur lequel est branché votre arduino, à lire dans arduino IDE. Attention, ce port peut changer d'un branchement au branchement suivant !
fichierCsv = open("donnees.csv", "w")       # crée le fichier donnees.csv
fichierCsv.write("Date,heure,Temperature,Pression,Hygrométrie\n")   # on passe les entêtes du fichier csv et \n pour indiquer la fin de ligne (on passe à la ligne suivante dans le fichier csv)
fichierCsv.close() 

while True:                                 # indéfiniment, le programme reçoit les données, les écrit dans le fichier, génère la page html
    fichierCsv = open("donnees.csv", "a")   # ajoute des lignes dans le fichier donnees.csv
    line = ser.readline()
    newString = line.decode(encoding='UTF-8')
    date = datetime.datetime.now()                                                  # l'heure est prise sur l'ordinateur
    fichierCsv.write(str(date.day)+"/"+str(date.month)+"/"+str(date.year)+",")      # format de la date au format français, suivi du séparateur ,
    fichierCsv.write(str(date.hour)+":"+str(date.minute)+":"+str(date.second)+",")  # format de l'heure suivi du séparateur ,
    fichierCsv.write(newString)                                                     # newString contient les données transmises par l'arduino branché en USB (ici, temp, pression et hygro)
    fichierCsv.close() 
    
    tableau=lectureFichierCsv(url)
    generationImageTableau(tableau)
    generationPageHtml(tableau)


