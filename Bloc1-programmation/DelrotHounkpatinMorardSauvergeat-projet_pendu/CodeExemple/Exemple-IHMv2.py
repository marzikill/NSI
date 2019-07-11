# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:22:08 2019

@author: magali.sauvergeat
"""
# partie 2
import turtle

def prog_principal(ihm):
    """ permet de tracer 3 segments du triangle, d'afficher un texte, de demander une saisie,
        d'éffacer le premier texte et de le remplacer par le texte saisi
        L'ensemble des fonctions de turtle utilent pour le pendu sont présentes.
        :param ihm: l'objet permettant de faire des changements sur l'écran
        :type ihm: TurtleScreen 
    """    
    
    stylo1= turtle.Turtle()
    stylo1.hideturtle() # cache le pointeur permettant de suivre la position de tracage
    stylo1.penup()
    stylo1.pensize(8)
    stylo2= turtle.Turtle()
    stylo2.hideturtle()# cache le pointeur permettant de suivre la position de tracage
    
    debut = (-50,0)
    fin = (50,0)
    stylo1.penup()
    stylo1.goto(debut)
    stylo1.pendown()
    stylo1.goto(fin)
    trait=[(0,50),(50,0)]
    stylo1.penup()
    stylo1.goto(trait[0])
    stylo1.pendown()
    stylo1.goto(trait[1])
    trait2=[(-50,0),(0,50)]
    stylo1.penup()
    stylo1.goto(trait2[0])
    stylo1.pendown()
    stylo1.goto(trait2[1])
    
    stylo2.penup()
    stylo2.goto(-50,-30)
    couleur='blue'
    stylo2.color(couleur)
    msg="Bonjour Exemple !"
    stylo2.write(msg, align="center", font=(None, 16, "bold"))      
    msg2= ihm.textinput("Réponse!"," Réponse: ")
    couleur='red'
    stylo2.color(couleur)
    stylo2.clear() # efface les précédente action de stylo2 
    stylo2.write(msg2, align="center", font=(None, 16, "bold"))      


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
    ihm.title("Exemple ")  #Change le titre
    return ihm


if __name__ == '__main__':
    """ Fonction spéciale débutant tous les programmes
    """
    ihm=init_fenetre()
    prog_principal(ihm)
    
    ihm.exitonclick()
    turtle.bye()
