
# dictionnaire des fréquences des lettres dans un texte en français 
frequence = {'a' : 0.083944, 'b' : 0.007669,  'c' : 0.033297, 'd' : 0.040699, 'e' : 0.145037,
              'f' : 0.012109, 'g' : 0.009495, 'h' : 0.007973, 'i' : 0.081828, 'j' : 0.006377, 'k' : 0.000638, 'l' : 0.058405,
              'm' : 0.029355, 'n' : 0.075570, 'o' : 0.053669, 'p' : 0.032087, 'q' : 0.012613, 'r' : 0.070209, 's' : 0.080091,
              't' : 0.074775, 'u' : 0.059808, 'v' : 0.015791, 'w' : 0.000067, 'x' : 0.004098, 'y' : 0.003155, 'z' : 0.001240}  

#partie 1
def lire_fichier(nomFichier):
    """ ouvre et lit le fichier contenant tous les mots francais
        :param nomFichier: le nom du fichier à lire
        :type nomFichier:  String
    """    
    fichier=open(nomFichier)
    texte=fichier.readlines()  #lit toutes les lignes du fichier texte
    fichier.close()
    print(texte)
            
if __name__ == '__main__':
    """ Fonction spéciale débutant tous les programmes
    """
    print(frequence)
    lire_fichier("liste_francaisU.txt")

