
# Table of Contents

1.  [Définition de dictionnaires](#org9cff03b)
    1.  [Gestion de mots de passe](#org1300627)
    2.  [Dictionnaire alphabétique -> numérique](#org91cd935)
    3.  [Éléments distincts.](#orge087538)
    4.  [Créer un dictionnaire à partir de deux listes](#orgd66ee40)
2.  [Parcours de dictionnaires](#orgfff5478)
    1.  [Parcours par clé, par valeurs](#org7566aa6)
    2.  [Plus sur les parcours par clés, par valeurs](#org3403e58)
    3.  [Opérations sur les dictionnaires](#org61d679e)
3.  [Exercices avancés](#orge1ada7f)
    1.  [Élection à choix multiples](#org16f726c)
    2.  [Cryptographie](#org2b18ef6)
    3.  [Application à la biologie](#org372b3ad)
    4.  [QCM de NSI](#org30939bf)



<a id="org9cff03b"></a>

# Définition de dictionnaires


<a id="org1300627"></a>

## Gestion de mots de passe

On stocke dans le dictionnaire `mots_de_passe` la liste des mots de passes des utilisateurs d'un site internet (*pour des raisons de sécurité, c'est une /très mauvaise idée*"). 

1.  Afficher le mot de passe d'Alice
2.  Ajouter un nouvel utilisateur `"Alfred"` dont le mot de passe est `azerty`.
3.  Écrire une fonction `verifie_mdp` qui étant donné un dictionnaire `mots_de_passe` stockant les mots de passe  des utilisateurs, vérifie si la chaine `entree` est le mot de passe de `utilisateur`.

    mots_de_passe = {'Bob' : '987654321', 'Alice' : '01012003'}
    def verifie_mdp(mots_de_passe, entree, utilisateur):
        pass


<a id="org91cd935"></a>

## Dictionnaire alphabétique -> numérique

Écrire une fonction `alphabet_min` qui renvoie le dictionnaire dont les clés sont les lettres `'a'`, `'b'`, &#x2026; `'z'`, associées à leur position dans l'alphabet. (`'a'` est associé à `1`, `'b'` à `2` etc).
On utilisera la fonction `chr` qui étant donné un nombre renvoie le caractère unicode associé. Par exemple `chr(97)` renvoie `'a'`. 

    def alphabet_min():
        pass


<a id="orge087538"></a>

## Éléments distincts.

Écrire une fonction `est_sans_doublons` qui étant donné une liste `l` d'éléments renvoie `True` si celle-ci ne contient aucun élément deux fois, `False` sinon. On rappelle que l'instruction `e in dict` renvoie `True` si la clé `e` est présente dans le dictionnaire `dict`, `False` sinon. 

    def est_sans_doublons(l):
        pass

**Sortie attendue** 

    l =  [1, 2, 3, 5, 5, 1, 6]
    est_sans_doublons(l) =  False
    l =  [1, 2, 3, 5, 6]
    est_sans_doublons(l) =  True

Écrire une fonction `sans_doublons` qui étant donné une liste `l` d'éléments renvoie la liste composée des éléments de `l`, sans doublons.  

    def sans_doublons(l):
        pass


<a id="orgd66ee40"></a>

## Créer un dictionnaire à partir de deux listes

Écrire une fonction `listes2dict` qui étant donné deux listes de même taille `l1` et `l2` renvoie le dictionnaire dont les clés sont les éléments de `l1`, et les valeurs les éléments de `l2`. On suppose que tous les éléments de `l1` sont distincts.

    def listes2dict(l1, l2):
        pass


<a id="orgfff5478"></a>

# Parcours de dictionnaires


<a id="org7566aa6"></a>

## Parcours par clé, par valeurs

Soit le dictionnaire 

    d = {"julie":8, "alfred":10, "lucas":-1, "camille":12}

Écrire une fonction `cles` qui prend en argument un dictionnaire `d` et qui renvoit la liste de toutes les clés présentes dans le dictionnaire.

    def cles(d):
        pass

Écrire une fonction `valeurs` qui prend en argument un dictionnaire `d` et qui renvoie la liste de toutes les valeurs présentes dans le dictionnaire. Si une valeur est présente plusieurs fois elle sera présente plusieurs fois dans la liste renvoyée.

    def valeurs(d):
        pass


<a id="org3403e58"></a>

## Plus sur les parcours par clés, par valeurs

Soit le dictionnaire `dcouple` 

    dcouple = {"julie":(5, 10), "alfred":(10, 5), "lucas":(13, 31), "camille":(0, 1)}

Écrire une fonction `valeur1` qui prend en argument un dictionnaire `dcouple` et qui renvoie la liste des premiers éléments associés à chaque couple. Avec le dictionnaire donné en exemple la liste renvoyée sera `[5, 10, 13, 0]`. 

Soit le dictionnaire `points` 

    points = {(0, 1) : 'A', (-1, 2): 'B', (4, -4): 'C', (-6, 5) : 'D', (1, 2) : 'E'}

Écrire une fonction `quartsuperieur` qui prend un dictionnaire `points` et qui renvoie la liste des points dont les coordonnées `x` et `y` sont positives ou nulles. 

    def quartsuperieur(points):
        pass

Écrire une fonction `demi_plan_superieur` qui prend un dictionnaire `points` et qui renvoie la liste des points qui se trouvent dans le demi-plan supérieur. 

    def demi_plan_superieur(points):
        pass

Écrire une fonction `valeurs_positives` qui prend en argument un dictionnaire `d` et qui renvoie un dictionnaire composé des associations du dictionnaire `d` dont les valeurs sont strictement positives. On suppose que toutes les valeurs du dictionnaire sont de type `int`. 

    def valeurs_positives(d):
        pass

Écrire une fonction `cle_debut` qui prend en argument un dictionnaire `d` et qui renvoit un dictionnaire composé des associations du dictionnaire `d` dont la clé commence par une lettre située avant la lettre `'e'` dans l'alphabet. 

    def cle_debut(d):
        pass


<a id="org61d679e"></a>

## Opérations sur les dictionnaires

Écrire une fonction `recherche_valeur` qui prend en argument un dictionnaire `d`, une valeur `val` et qui renvoie la liste des clés associées à cette valeur. Si `val` n'est pas une valeur présente dans le dictionnaire, on renvoit la liste vide.

    def recherche_valeur(d):
        pass

On suppose que toutes les valeurs présentes dans le dictionnaire sont de type `int`. Écrire une fonction `double` qui étant donné un dictionnaire renvoit un dictionnaire composé des même clés mais où toutes les valeurs ont été doublées. Le dictionnaire initial ne sera pas modifié. 

    def double(d):
        pass

Écrire une fonction `double_modifie` qui modifie le dictionnaire passé en argument en doublant toutes les valeurs. 

    def double_modifie(d):
        pass

Écrire une fonction `somme_valeurs` qui retourne la somme des valeurs présentes dans un dictionnaire `d`.

    def somme_valeurs(d):
        pass

Soit le dictionnaire

    d2 = {"rayan":15, "leandro":-20, "josh":-3, "erwan":42}

Écrire une fonction `fusionne` qui étant donné deux dictionnaires `d1` et `d2` renvoit un dictionnaire composé des associations clé/valeurs présentes dans les dictionnaires `d1` et `d2`. Les dictionnaires `d1` et `d2` ne doivent pas être modifiés. On suppose que toutes les clés sont différentes.

    def fusionne(d1, d2):
        pass

Écrire une fonction `inverse` qui prend en argument un dictionnaire `d` et qui retourne un dictionnaire où les valeurs et les clés sont inversées par rapport à `d`. Par exemple `inverse({"bob":13, "léa":15})` retourne `{13:"bob", 15:"léa"}`. On suppose que toutes les valeurs de `d` sont différentes.

    def inverse(d):
        pass


<a id="orge1ada7f"></a>

# Exercices avancés


<a id="org16f726c"></a>

## Élection à choix multiples

Les résultats d'un vote sont stockés dans une liste `votes`, composée du nom du candidat présent sur chaque bulletin de vote. Écrire une fonction `compte_voix` qui étant donné une liste de votes renvoie un dictionnaire où les clés sont les prénoms des candidats et les valeurs le nombre de vote totalisé par chaque candidat.

    def compte_voix(votes):
        pass
    
    votes = ["Alfred", 'Barbara', 'Barbara', 'Barbara', 'Alfred', 'Barbara', 'Blanc', 'Alfred', 'Barbara', 'Charles']

Écrire une fonction `vainqueur` qui étant donné une liste de `votes` renvoie le nom du candidat ayant obtenu le plus de votes.

    def vainqueur(votes):
        pass


<a id="org2b18ef6"></a>

## Cryptographie

On associe à chaque lettre majuscule son numéro sa position dans l'alphabet.

    dico = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21,"V":22, "W":23, "X":24, "Y":25, "Z":26}

Écrire une fonction `code_numerique` qui étant donné une chaine de caractère composée uniquement de caractères majuscules renvoie la somme des positions de ses caractères. 

**Exemple** Pour le mot `'ALAIN'` le code numérique est l’entier 37 car 1 + 12 + 1 + 9 + 14 = 37.

Pour le mot `'PAUL'`, le code numérique est l’entier 50 car 16 + 1 + 21 + 12 = 50.

    def code_numerique(mot_maj):
        pass

Écrire une fonction `code_alphabetique` qui étant donné une chaine de caractères composée uniquement de caractères majuscule renvoie le nombre composé de la concaténation des codes de ses caractères. On utilisera la fonction `str` : appliquée à un nombre elle renvoie le caractère qui représente ce nombre (`str(1)` renvoie le caractère `'1'`).

**Exemple** Pour le mot `'ALAIN'` le code alphabétique est '1121914'.

Pour le mot `'PAUL'`, le code alphabétique est '1612112'.

    def code_alphabetique(mot_maj):
        pass

Un mot est **parfait** si son code numérique divise son code alphabétique. Écrire une fonction `est_parfait` qui teste si un mot écrit en majuscules est parfait. On utilisera la fonction `int` : appliquée à une chaine de caractère qui est un nombre elle renvoie le nombre correspondant (`int('123456')` renvoie le nombre `123456`).

    def est_parfait(mot_maj):
        pass


<a id="org372b3ad"></a>

## Application à la biologie

1.  Composition en acides aminés

    En utilisant un dictionnaire, déterminez le nombre d’occurrences de chaque acide aminé dans la séquence `AGWPSGGASAGLAILWGASAIMPGALW`. Le dictionnaire ne doit contenir que les acides aminés présents dans la séquence.
    
        def occurrences(seq):
            pass

2.  Mots de 2 et 3 lettres dans une séquence d'ADN

    Créez une fonction `compte_mots_2_lettres()` qui prend comme argument une séquence sous la forme d'une chaîne de caractères et qui renvoie tous les mots de 2 lettres qui existent dans la séquence sous la forme d'un dictionnaire. Par exemple pour la séquence `ACCTAGCCCTA`, le dictionnaire renvoyé serait : `{'AC': 1, 'CC': 3, 'CT': 2, 'TA': 2, 'AG': 1, 'GC': 1}`
    
        def compte_mots_2_lettres():
            pass
    
    Créez une nouvelle fonction `compte_mots_3_lettres` qui a un comportement similaire à `compte_mots_2_lettres` mais avec des mots de 3 lettres.
    
    Utilisez ces fonctions pour affichez les mots de 2 et 3 lettres et leurs occurrences trouvés dans la séquence d'ADN : `ACCTAGCCATGTAGAATCGCCTAGGCTTTAGCTAGCTCTAGCTAGCTG`
    
    Voici un exemple de sortie attendue :
    
    Mots de 2 lettres
    AC : 1
    CC : 3
    CT : 8
    [&#x2026;]
    Mots de 3 lettres
    ACC : 1
    CCT : 2
    CTA : 5
    [&#x2026;]


<a id="org30939bf"></a>

## QCM de NSI

Les réponses correctes d'un QCM de NSI sont stockées dans un dictionnaire nommé `reponses_valides`. Les clés sont des chaînes de caractères de la forme `"Q1"`. Les valeurs possibles sont des chaînes de caractères correspondant aux quatre réponses `"a"`, `"b"`, `"c"`, `"d"`.

Les réponses données par Alice sont stockées dans le dictionnaire `reponses_Alice` dont voici un exemple possible :

    reponses_valides = {"Q1":"c","Q2":"a","Q3":"d","Q4":"c","Q5":"b"}
    reponses_Alice = {"Q1":"b","Q2":"a","Q3":"d","Q5":"a"}

Lorsqu'Alice n'a pas répondu à une question, il n'y a pas de clef correspondant au nom de l'exercice.

La notation d'un QCM de NSI est la suivante : 3 points par réponse correcte, -1 point par réponse incorrecte et 0 si l'on n'a pas répondu

Écrire une fonction `correction_QCM` qui, à partir des dictionnaires `reponses_eleve` et `reponses_valides` passées en paramètres renvoie le nombre de points obtenus au QCM par Alice. Vous donnerez le nombre de points obtenus par Alice au QCM à l'aide de cette fonction.

    def correction_QCM(reponses_eleve, reponses_valides):
        pass

Source : [nsi première](http://thalesm.hmalherbe.fr/gestclasse/documents/Premiere_NSI/TP/TP_dictionnaires.html)

