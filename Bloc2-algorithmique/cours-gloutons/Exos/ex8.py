
#Jeu de données

#t4  [(7,13),(4,12),(3,8),(3,10)] 30
#t7  [(442, 41),(525, 50),(511, 49),(593, 59),(546, 55),(564, 57),(617, 60)] 170
#t8  [(15, 2),(100, 20),(90, 20),(60, 30),(40, 40),(15, 30),(10, 60),(1, 1)] 102
#t10 [(92, 23),(57, 31),(49, 29),(68, 44),(60, 53),(43, 38),(67, 63),(84, 85),(87, 89),(72, 82)] 165
#t15 [(214, 113),(229, 118),(192, 98),(150, 80),(173, 90),(139, 73),(240, 120),(156, 82),(135, 70),(163, 87),(221, 115),(201, 106),(149, 77),(184, 94),(210, 110)] 750
#################################################################################
#################################################################################
#################################################################################
def possibilites(n):
    '''Fonction que génère l'ensemble des choix possibles avec n objets.
    Les objets sont reperés par des lettres de l'alphabet (MAJ & min).
    La réponse est liste des choix possibles ; par emxemple:
    possibilites(3) renvoie ['', 'A', 'B', 'C', 'AB', 'AC', 'BC', 'ABC']
    '''
    # on se limite à 52 objets avec n positif
    assert n<52 and n>=0
    #on initialise deux listes
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
              'O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b',
              'c','d','e','f','g','h','i','j','k','l','m','n','o','p',
              'q','r','s','t','u','v','w','x','y','z']
    tab=[]

    #On place dans tab, n objets de la liste alphabet
    for i in range(n):
        tab.append(alphabet[i])

    #on place l'élément sac vide dans la liste à retourner
    combinaisons = ['']

    #on boucle sur n
    for loop in range(n):

        #on creé une copie de tab à chaque tour
        tmp = [i for i in tab]

        #on boucle sur loop (élément courant de la 1ere boucle)
        for boucle in range(loop):

            #on compare l'élément à ajouter i avec le dernier élément ajouté x[-1]
            tmp = [x+i for i in tab for x in tmp if ord(i)>ord(x[-1])]

        #ajoute le(s) nouveaux choix retenus
        combinaisons += tmp
    return combinaisons

#################################################################################
#################################################################################
#################################################################################
def KPnaif(l,maxi):
    '''Fonction qui reçoit en paramètres une liste de tuples (valeur,poids)
    et une valeur maximale pour le poids du sac à dos.
    Elle retourne un triplet: liste des objets retenue,valeur du sac,poids du sac.
    '''

    #copie redondante mais pratique si on veut séparer les 2 algorithmes
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
              'O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b',
              'c','d','e','f','g','h','i','j','k','l','m','n','o','p',
              'q','r','s','t','u','v','w','x','y','z']
    n=len(l)
    #appel de la fonction possibilite
    t=possibilites(n)
    #t est une liste du type ['', 'A', 'B', 'C', 'AB', 'AC', 'BC', 'ABC']

    reponse=[]
    best=0
    masse=0
    #on oublie le sac vide qui n'a ni valeur ni poids
    for loop in range(1,len(t)):
        booleen=False
        valeur=0
        poids=0

        #on regarde tous les objets dans la chaine (ex'ABC' c'est 3 objets)
        for elt in list(t[loop]):
            # alphabet.index(elt) renvoie la position de l'elt courant dans alphabet
            # l[alphabet.index(elt)] on prend donc le k-eme objet de la liste
            # et on regarde son poids [1]
            # si la charge maxi n'est pas dépassée en ajoutant cet objet
            if l[alphabet.index(elt)][1]+poids<=maxi:
                #on augment la valeur et le poids du sac
                valeur+= l[alphabet.index(elt)][0]
                poids += l[alphabet.index(elt)][1]
                booleen=True
            #sinon on élimine cette combinaison d'objets
            else:
                booleen=False
                break
        #Si la combinaison respecte la contrainte de poids
        if booleen:
            #si la valeur de ce sac l'actuelle plus grande valeur
            if valeur>best:
                #on récupère la nouvelle valeur maximale et le poids correspondant
                best=valeur
                masse=poids
                #on crée une une liste avec les objets dans le sac
                temp=[l[alphabet.index(x)] for x in list(t[loop])]
                #on ajoute les meilleurs résultats dans une liste
                #on peut faire autrement?
                reponse.append(temp)
    #on garde uniquement le dernier ajouté soit le meilleur de tous
    reponse=reponse[-1]
    #on retourne une liste de 1 et de 0,valeur,poids
    return [1 if x in reponse else 0 for x in l],best,masse
