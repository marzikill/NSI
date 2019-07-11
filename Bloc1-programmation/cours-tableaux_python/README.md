# Bloc 1

Projet : cours sur les tableaux en python

## Cours

Les fichiers de cours avec les sources LaTeX.

J'ai utilisé le module pythontex : il permet d'exécuter du code Python à l'intérieur d'un fichier latex, et de simuler le comportement de l'intérpréteur. Voir le source pour les détails. Pour compiler :

* xelatex --shell-escape cours.tex
* pythontex cours.tex
* xelatex --shell-escape cours.tex

J'ai aussi utilisé le module minted pour afficher la coloration syntaxique des codes sources python.

## TP 

### Sources latex

Les fichiers de TP avec les sources LaTeX.

J'ai utilisé le module pythontex : il permet d'exécuter du code Python à l'intérieur d'un fichier latex, et de simuler le comportement de l'intérpréteur. Voir le source pour les détails. Pour compiler :

* xelatex --shell-escape tp2.tex
* pythontex tp2.tex
* xelatex --shell-escape tp2.tex

J'ai aussi utilisé le module minted pour afficher la coloration syntaxique des codes sources python.

### Contenu du TP

#### Première partie

Exercies d'introduction, manipulation basique des tableaux. (on fait taper les élèves des commandes dans le shell Python, ils observent le résultat)

#### Seconde partie

Réalisation d'un petit module sur les listes en Python. Les fonctions codées sont les suivantes :

* recopier (recopier un tableau)
* sous-tableau (extrait un sous-tableau)
* concatener (concatene deux tableaux)
* insere (insere un élément a une position dans un tableau)

## Cheat Sheet 

Un fichier résumé de tous les trucs que les élèves doivent absolument savoir à propos des tableaux en Python.

## Module

Un module rempli de fonctions basiques, dont on peut (et devrai) demander l'implémentation en Python aux élèves à un moment dans l'année. Certains morceau sont très faciles, d'autres un peu moins évidents.

## QCM

QCM réalisé à l'aide d'**Auto-multiple-choice** (disponible uniquement sous Linux). AMC permet l'édition, l'impression, et la correction automatique de QCM en latex. L'ordre des questions est aléatoire pour chaque élève, l'ordre des champs réponse est aussi aléatoire. 

Pour réaliser ce QCM :

* écrire le code source sur le modèle donné
* NE PAS UTILISER PYTHONTEX (conflit avec le package automultiplechoice)
* pour utiliser minted avec automultiplechoice : il FAUT faire comme j'ai fait (sinon conflit de verbatim (un truc chelou...)). Il faut stocker tous les morceaux de codes utilisés dans des fichiers à part (ici stockés dans ./pyfiles) et les faire afficher via \inputminted. Cela ne **marche pas** avec l'environnement minted.
* importer le fichier source dans Auto-Multiple-Choice
* jouer avec les paramètres (dans les options ne pas oublier de changer le compilateur à xelatex --shell-escape (pour minted))

## Questions éventuelles (latex, python)

florian.picard@ac-versailles.fr
