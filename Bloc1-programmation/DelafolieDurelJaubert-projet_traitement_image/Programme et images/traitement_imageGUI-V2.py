''' Retouche d'images au format PGM ascii
    Auteur P. Jaubert juin 2019
    Fonctions zoom, photomaton, miroir écrites par F. Durel juin 219
    Menu graphique Tkinter'''


from tkinter import *


class ComboBox(Frame):
    """ widget composite associant un champ de saisie et une liste """
    def __init__(self, boss, item='', items=[], command = '',width=10, listSize =5):
        Frame.__init__(self,boss) # constructeur de la classe parente
        self.items = items
        self.command = command
        self.item = item

        #champ de saisie
        self.entree = Entry(self, width= width)
        self.entree.insert(END, item)
        self.entree.bind ("<Return>", self.sortieE)
        self.entree.pack(side=TOP)

        #boîte de liste +scroll bar
        cadreLB = Frame(self)
        self.bListe = Listbox(cadreLB, height = listSize, width = width -1)
        scrol = Scrollbar(cadreLB, command = self.bListe.yview)
        self.bListe.config (yscrollcommand = scrol.set)
        self.bListe.bind("<ButtonRelease-1>", self.sortieL)
        self.bListe.pack(side=LEFT)
        scrol.pack(expand = YES, fill = Y)
        cadreLB.pack()

        #remplissage de la boîte de liste avec les items fournis
        for i in items :
            self.bListe.insert(END, i)

    def sortieL(self, event=None):
        """ extraire de la liste l'item qui a été sélectionné """
        index = self.bListe.curselection()      # renvoie un  tuple d'index
        ind0 = int(index[0])                    # dont on ne garde que le premier
        self.item = self.items[ind0]
        # actualiser le champ d'entrée avec l'item choisi
        self.entree.delete(0, END)
        self.entree.insert(END, self.item)
        # exécuter la commande indiquée avec l'item choisi comme argument
        self.command(self.item)

    def sortieE(self, event=None):
        """ exécuter la commande avec l'item sélectionnencodé tel-quel"""
        self.command(self.entree.get())

    def get(self):
        """ renvoie le dernier item sélectionné dans la boîte de liste"""
        return self.item
#########################################################
# fonctions de lecture/ecriture de fichiers PGM         #
#########################################################

def lecture_fichier(filename):
    ''' teste si le fichier de départ est un fichier pgm (1ere ligne = P2)
    et retourne les 3 lignes d'entête du fichier puis la chaîne des pixels en forme string.
    L'intensité max, hauteur et largeur sont retournées sous forme numérique
    préconditions : le fichier est codée en pgm ascii 
    entête attendue :
        P2
        # commentaire ou non
        largeur et hauteur en pixels
        intensité entre 0 et 255
        les pixels avec espace ou lf (\n) comme séparateurs'''
    
    
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
        f.close();
        return '-1'

  
def taille_img(s):
    """ extrait sous forme numérique largeur et hauteur de la chaine s (ligne 2 du fichier)"""
    
    ls=''
    hs=''
    i=0
    while (s[i]!=' '):
        ls= ls+s[i];
        i+=1;
    l=int(ls)
    while (s[i]!='\n'):
        hs= hs+s[i];
        i+=1;
    h=int(hs)

    return(l,h)

def lecture_photo(s,l,h, table) :
    """ lit les différentes valeurs ASCII et les place dans un tableau de h lignes sur l colonnes"""
    i=0
  
# remplissage du tableau
    for j in range (0,h):
        for k in range (0,l) :
            temp=""
            while s[i]!=' ' and s[i] !='\n' :
                temp=temp+s[i];
                i+=1;
            table[j][k]=int(temp);
            i+=1;
    
    return table;
    
def ecriture_photo() :
    """ remplit les 3 premières lignes puis écrit différentes valeurs ASCIIen fonction du tableau de h lignes sur l colonnes"""
    global L,H,intensite, photo
    
    f = open(f2,"w");
    s="P2\n"+str(L)+' '+str(H)+'\n'+str(intensite)+'\n';
    
    # remplissage du tableau
    for j in range (0,H):
        for k in range (0,L) :
            s= s + str(photo[j][k])+' ';
    f.write(s);
    f.close();

def affiche_photo():
    ''' affiche la photo dans le Canvas '''
    # si la taille dépasse celle du Canvas on affiche qu'une partie. 
    h= min(H,500)
    l = min(L,500)
    #centrage  
    x0 = (500- l) // 2
    y0 = (500- h) // 2   
    
    for j in range (0,l):
        for k in range (0,h) :
            n= photo[k][j]
            rgb = "#%02x%02x%02x" % (n, n, n)
            can.create_oval(j + x0,k +y0 ,j+x0+2, k+y0+2,outline='', fill=rgb)
   
    
    
#  _______________________________________________________________________
# traitements 

def NB_photo(l,h,lum,photo):
    for j in range (0,h):
        for k in range (0,l) :
            if photo[j][k]>lum//2 :
                photo[j][k]=lum;
            else :
                photo[j][k]=0;
    return(photo);
    

def negatif(l,h,lum,photo):
    
    for j in range (0,h):        
        for k in range (0,l) :
            photo[j][k]=lum- photo[j][k];
    return(photo);
    
def floute(l,h,lum,photo):
    for j in range (0,h):
        for k in range (0,l-1) :
            photo[j][k+1]=(photo[j][k]+photo[j][k+1])//2;
    return(photo);

def rotation(l,h,photo):
    ''' rotation horaire de 90°
    on créée une matrice vide  avec les dimensions interverties. 
    on recopie éléments par éléments en modifiant les indices. 
    '''
    #création matrice vide
    ligne=[0]*h
    p2=[ligne[:] for i in range (0,l)]

    for i in range (0,h):
        for j in range(0,l):
            p2[j][i]=photo[h-1-i][j]
        
    return (p2)

def miroir(l,h,photo):
    for j in range (0,h):
        for k in range (0,int(l/2)):
            droite = photo[j][k]
            gauche = photo[j][l-k-1]
            photo[j][k] = gauche
            photo[j][l-k-1] = droite

    return photo

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
    '''
    for j in range (1,h-1):
        for k in range (1,l-1):
            p2[j*2][k*2]=int((photo[j][k]+photo[j-1][k]+photo[j][k-1]+photo[j-1][k-1])/4)    #haut gauche
            p2[j*2+1][k*2]=int((photo[j][k]+photo[j+1][k]+photo[j][k-1]+photo[j+1][k-1])/4)  #haut droite
            p2[j*2][k*2+1]=int((photo[j][k]+photo[j-1][k]+photo[j][k+1]+photo[j-1][k+1])/4)  #bas gauche
            p2[j*2+1][k*2+1]=int((photo[j][k]+photo[j+1][k]+photo[j][k+1]+photo[j+1][k+1])/4)  #bas droite
    '''
    return p2,l*2,h*2
    

    
#  _______________________________________________________________________
# Actions et événements. 

def charge_image():
    ''' récupère le nom du fichier choisi et le lit
    ferme le combo choix fichier pour le combo choix de traitement. 
    '''
    global L,H, intensite, photo
    
    f= combo.get()
    lab.configure(text = f)
    L, H, intensite, s = (lecture_fichier(f));   

    combo.destroy()
    #intialisation de la matrice photo avec des 0
    # pour créer la matrice il faut mettre le [:] sur la seconde ligne sinon on ne copie pas la liste ligne, on indexe la même. 
    ligne=[0]*L
    photo=[ligne[:] for i in range (0,H)]

    # chargement de la matrice avec les pixels
    photo=lecture_photo(s,L,H,photo)
    affiche_photo() 

    # nouveaux combobox + bouton de validation
    combo2.grid(row=1, columnspan = 2, padx =10, pady =10)
    bou2 = Button(fen, text = "traitement", command = choix_traitement)
    bou2.grid(row=3, column = 0, padx =8, pady =8)

    

def choix_item(s):
    # fonction vide pour donner une comande non active à l'appel de combo2
    print(s)
           
def choix_traitement():
    global L,H, intensite, photo
    
    choix=combo2.get()
    lab2.configure(text = choix)
    if choix=='negatif' :
        photo= negatif(L,H,intensite,photo)
    if choix=='NB':
        photo= NB_photo(L,H,intensite,photo)
    if choix=='flou' :
        photo= floute(L,H,intensite,photo)
    if choix=='rotation horaire 90°' :
        photo= rotation(L,H,photo)
        L,H= H,L
    if choix=='miroir' :
        photo= miroir(L,H,photo)
    if choix=='zoom' :
        photo,L,H = zoom(L,H,photo)   
    if choix=='photomaton' :
        photo,L,H = photomaton(L,H,photo)


    can.delete(ALL)
    affiche_photo()
    
   


# Programme principal
#  _______________________________________________________________________
#if __name__ == "__main__":


# fichier cible
global f2
f2 = "image_modifiee.pgm";

# liste des fichiers pgm présents dans le répertoire courant 

liste_pgm=[]
import os
for element in os.listdir():
    if element.endswith('.pgm'):
        liste_pgm.append(element)


#  liste des traitements possibles

global menu
menu = ('negatif','NB','flou','rotation horaire 90°', 'miroir', 'zoom', 'photomaton')

       
fen =Tk()
fen.title("photoboutique")
fen.configure(background= "steelblue1")




combo = ComboBox(fen, item = "néant", items = liste_pgm, command = choix_item, width = 35, listSize = len(liste_pgm)//2)    
combo.grid(row=1, columnspan = 2, padx =10, pady =10)
combo2 = ComboBox(fen, item = "néant", items = menu, command = choix_item, width = 30, listSize = 4)    # mise en grid dans la fonction 
bou = Button(fen, text = "valider", command = charge_image)
bou.grid(row=2, column = 0, padx =8, pady =8)
lab = Label(fen, text ="bonjour", bg = 'ivory', width =25)
lab.grid(row=2, column = 1, padx = 8, pady =8)
lab2 = Label(fen, text ="traitement", bg = 'ivory', width =25)
lab2.grid(row=3, column = 1, padx = 8, pady =8)
sortie = Button(fen, text='Quitter', command=fen.destroy)
sortie.grid(row=3, column = 3, padx = 8, pady =8)
sauve = Button(fen, text='Enregistrer', command=ecriture_photo)
sauve.grid(row=2, column = 3, padx = 8, pady =8)
can = Canvas(fen, bg ='blue', width = 500, height = 500)
can.grid (row=1, column = 3, padx = 8, pady = 8)



fen.mainloop()
