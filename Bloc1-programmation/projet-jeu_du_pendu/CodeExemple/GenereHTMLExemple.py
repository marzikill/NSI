# dictionnaire des fréquences des lettres dans un texte en français 
frequence = {'a' : 0.083944, 'b' : 0.007669,  'c' : 0.033297, 'd' : 0.040699, 'e' : 0.145037,
              'f' : 0.012109, 'g' : 0.009495, 'h' : 0.007973, 'i' : 0.081828, 'j' : 0.006377, 'k' : 0.000638, 'l' : 0.058405,
              'm' : 0.029355, 'n' : 0.075570, 'o' : 0.053669, 'p' : 0.032087, 'q' : 0.012613, 'r' : 0.070209, 's' : 0.080091,
              't' : 0.074775, 'u' : 0.059808, 'v' : 0.015791, 'w' : 0.000067, 'x' : 0.004098, 'y' : 0.003155, 'z' : 0.001240}  

# partie 3
def gen_html(nomFichier):
    """ créé et écrit du texte dans un fichier dont le nom est donné en paramètre
        Le texte écrit est le squelette d'un fichier html
        :param nomFichier: le nom du fichier à créer
        :type nomFichier:  String
    """    
    fichier= open(nomFichier,"w") 
    # écriture dans le fichier avec la méthode print
    print("""<!DOCTYPE html> <!DOCTYPE html><html lang=\"fr\"><head>  <meta charset="UTF-8"> 
          <meta name="author" content="test"> <title>Test </title> 
          <link rel="stylesheet" type="text/css" href="mystyle.css"></head><body>""",end='\n',file=fichier )
    # écriture dans le fichier avec la méthode write()
    fichier.write('<h1>Bonjour à tous !</h1>')
    print('</body></html>',end='\n',file=fichier )
    fichier.close()

if __name__ == '__main__':
    """ Fonction spéciale débutant tous les programmes
    """
    gen_html("pageTest.html")
      