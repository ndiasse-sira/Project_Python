
from os import system, name 

import random
   

def clear(): 
    
    """ Commentaires de spécifications 
        Objectifs : La fonction clear() permet d'effacer les opérations faits.
        Méthode : fonction du terminal avec cls pour windows et clear pour mac et linux 
        Besoins : system('cls'), system('clear')
        Connus : 0
        Entrées : nt ou !nt
        Sorties : cls - clear
        Résultats : effacement des opérations 
        Hypothéses : Pour que çà marche, il faut que l'utilisateur donne une donnée pour effacer l'interface des opérations.
    """
  
    # pour windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # pour mac et linux
    else: 
        _ = system('clear') 

def replay():
    
   """ Commentaires de spécifications 
        Objectifs : fonction pour rejouer le jeu
        Méthode : choix de l'utilisateur entre O et N pour rejouer ou quitter le jeu
        Besoins : rejouer - bloc hangman() - bloc exit()
        Connus : 0
        Entrées : rejouer
        Sorties : hangman() - exit()
        Résultats : interface du LET-GET ou quitter
        Hypothéses : çà ne peut marcher que si l'utilisateur appuie sur O pour continuer ou sur N pour quitter
   """
   rejouer = input('Vous voulez rejouer O/N :')
   if rejouer == "o" or rejouer == "O":
         letget()
   elif rejouer == "n" or rejouer == "N":
         exit()
         clear()
   else:
      print('Veuillez recommencer entrer O ou N')
      replay()

def letget():
    
   """ Commentaires de spécifications 
        Objectifs : hangman est la fonction principale du jeu LET-GET qui va permettre à l'utilisateur de  trouver le mot secret au hasard. A chaque fois qu'il perd un homme sera pendu
        Méthode : Pour arriver à celà  l'utilisateur va choisir un niveau du plus facile au plus difficile et le jeu commencera.
        Besoins : niveau
        Connus : 0
        Entrées : niveau
        Sorties : l - g - w
        Résultats : affichage du jeu
        Hypothéses : possible avec le choix des niveaux
   """
    
   print(f">>> Bienvenue dans LET-GET <<< \n\t\t")
   niveau = int(input("Veuillez choisir le niveau du jeu : 1 (2-4 lettres), 2 (5-7 lettres), 3 (+7 letters) \n\n"))
   
   a=1
   
   
   
   def niveau1():
       
        """ Commentaires de spécifications 
            Objectifs : le niveau 1 est le niveau où l'utilisateur vas devoir choisir entre 2-4 lettres. Aprés il devra deviner le mot complet. Si il perd, un message s'affichera avec le mot secret et l'homme sera pendu et si il gagne son score s'affichera avec le mot secret
            Méthode : Pour arriver à cela, un hint de 2-4 lettres s'affichera, l'utilisateur entrera une lettre. Si la lettre est correcte, elle s'alignera à sa place normale. L'utilisateur continue à choisir s'il choisit une lettre déja prise ses tentatives ne chutent mais si il fausse une lettre il perd une tentative de moins et une partie du corps de l'homme s'affichera. Au fur et à mesure que les tentatives chutent, il perdra et l'homme sera pendu
            Besoins : f - word - w - g - list - mainlist - guessed - listletter
            Connus : 0
            Entrées : niveau
            Sorties : w - g 
            Résultats : affichage de la question pour le mot et choix de l'utilisateur jusqu'à perdre ou trouver 
            Hypothéses : il faut que l'utilisateur choisisse
        """
        
        clear()
        with open('mots.txt', 'r') as f:
            words = f.readlines()
        w = random.choice(words)[:-2]
        i =0
        g = 1
        word = ''
        list = []
        mainlist = []
        guessed = False
        letter = []
        print (f"Le mot est composé de {len (w)} lettres")
        while guessed == False and g <= 6:      
            l = input('Veuillez entrer une lettre : ')
            print("Il vous reste", 6-g,"tentatives")
            mainlist.append (l.upper ())
            listLetter = "-".join(mainlist)
            print(listLetter)
            if l not in w:
            
                

                if g == 1:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |     O      
                                                        |        
                                                        |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")
                elif g == 2:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O      
                                                        |        
                                                        |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")

                elif g == 3:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |        
                                                        |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")
                elif g == 4:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |     |       
                                                        |     |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")
                elif g == 5:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |     |       
                                                        |     |
                                                        |    /
                                                        |
                                                        |
                                                    ___|___""")
                elif g == 6:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |     |       
                                                        |     |
                                                        |    / \\
                                                        |
                                                        |
                                                    ___|___
                                            Vous avez perdu le mot est """+w)
                        with open("log_game.txt", 'a') as f:
                            f.write("Niveau Moyen:\n")
                            print("Le score est {}\n".format(6-g), file=f)
                            print("Le nombre de tentatives est {}\n".format(g), file=f)
                            print("Vous etes a votre partie n'{}\n".format(a), file=f)
                        
                g += 1
                if g > 6:
                    replay()

            else:            
                    list.append(l.lower())
                    # list.sort()
                    word = ''   
                    if guessed == False: 
                        for l in w.lower():                        
                            if l in list:                  
                                word += l
                                                                 
                            else:
                                word +=' _'
                        print(word)
                    if word == w:
                        print (' ')
                        print (f"Bravo vous avez trouver le mot {w} !")
                        print("Score:", (6-g)*len(w))
                        with open("log_game.txt", 'a') as f:
                            f.write("Niveau Facile:\n")
                            print("Le score est {}\n".format((6-g)*len(w)), file=f)
                            print("Le nombre de tentatives est {}\n".format(g), file=f)
                            print("Vous etes a votre partie n'{}\n".format(a), file=f)
                        print (' ')
                        
                        replay()
        
                        
   
   
   def niveau2():

        """ Commentaires de spécifications 
            Objectifs : le niveau 2 est le niveau où l'utilisateur vas devoir choisir entre 5-7 lettres. Aprés il devra deviner le mot complet. Si il perd, un message s'affichera avec le mot secret et l'homme sera pendu et si il gagne son score s'affichera avec le mot secret
            Méthode : Pour arriver à cela, un hint de 2-4 lettres s'affichera, l'utilisateur entrera une lettre. Si la lettre est correcte, elle s'alignera à sa place normale. L'utilisateur continue à choisir s'il choisit une lettre déja prise ses tentatives ne chutent mais si il fausse une lettre il perd une tentative de moins et une partie du corps de l'homme s'affichera. Au fur et à mesure que les tentatives chutent, il perdra et l'homme sera pendu
            Besoins : f - word - w - g - list - mainlist - guessed - listletter
            Connus : 0
            Entrées : niveau
            Sorties : w - g 
            Résultats : affichage de la question pour le mot et choix de l'utilisateur jusqu'à perdre ou trouver 
            Hypothéses : il faut que l'utilisateur choisisse
        """
        
        clear()
        with open('mots2.txt', 'r') as f:
            words = f.readlines()
        w = random.choice(words)[:-1]
        i =0
        g = 1
        word = ''
        list = []
        mainlist = []
        guessed = False
        letter = []
        print (f"Le mot est composé de {len (w)} lettres")
        while guessed == False and g <= 6:      
            l = input('Veuillez entrer une lettre : ')
            print("Il vous reste", 6-g,"tentatives")
            mainlist.append (l.upper ())
            listLetter = "-".join(mainlist)
            print(listLetter)
            if l not in w:
            
                

                if g == 1:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |     O      
                                                        |        
                                                        |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")
                elif g == 2:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O      
                                                        |        
                                                        |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")

                elif g == 3:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |        
                                                        |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")
                elif g == 4:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |     |       
                                                        |     |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")
                elif g == 5:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |     |       
                                                        |     |
                                                        |    /
                                                        |
                                                        |
                                                    ___|___""")
                elif g == 6:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |     |       
                                                        |     |
                                                        |    / \\
                                                        |
                                                        |
                                                    ___|___
                                            Vous avez perdu le mot est """+w)
                        with open("log_game.txt", 'a') as f:
                            f.write("Niveau Moyen:\n")
                            print("Le score est {}\n".format(6-g), file=f)
                            print("Le nombre de tentatives est {}\n".format(g), file=f)
                            print("Vous etes a votre partie n'{}\n".format(a), file=f)
                g += 1
                if g > 6:
                    replay()

            else:            
                    list.append(l.lower())
                    # list.sort()
                    word = ''   
                    if guessed == False: 
                        for l in w.lower():                        
                            if l in list:                  
                                word += l                                 
                            else:
                                word +=' _'
                        print(word)
                    if word == w:
                        print (' ')
                        print (f"Bravo vous avez trouver le mot {w} !")
                        print("Score:", (6-g)*len(w))
                        with open("log_game.txt", 'a') as f:
                            f.write("Niveau Moyen:\n")
                            print("Le score est {}\n".format((6-g)*len(w)), file=f)
                            print("Le nombre de tentatives est {}\n".format(g), file=f)
                            print("Vous etes a votre partie n'{}\n".format(a), file=f)
                        print (' ')
                        replay()
                        
                        
   def niveau3():
       
        """ Commentaires de spécifications 
            Objectifs : le niveau 3 est le niveau où l'utilisateur vas devoir choisir +7 lettres. Aprés il devra deviner le mot complet. Si il perd, un message s'affichera avec le mot secret et l'homme sera pendu et si il gagne son score s'affichera avec le mot secret
            Méthode : Pour arriver à cela, un hint de 2-4 lettres s'affichera, l'utilisateur entrera une lettre. Si la lettre est correcte, elle s'alignera à sa place normale. L'utilisateur continue à choisir s'il choisit une lettre déja prise ses tentatives ne chutent mais si il fausse une lettre il perd une tentative de moins et une partie du corps de l'homme s'affichera. Au fur et à mesure que les tentatives chutent, il perdra et l'homme sera pendu
            Besoins : f - word - w - g - list - mainlist - guessed - listletter
            Connus : 0
            Entrées : niveau
            Sorties : w - g 
            Résultats : affichage de la question pour le mot et choix de l'utilisateur jusqu'à perdre ou trouver 
            Hypothéses : il faut que l'utilisateur choisisse
        """
         
        clear()
        with open('mots3.txt', 'r') as f:
             words = f.readlines()
        
        w = random.choice(words)[:-1]
        
        i =0
        g = 1
        word = ''
        list = []
        mainlist = []
        guessed = False
        letter = []
        print (f"Le mot est composé de {len (w)} lettres")
        while guessed == False and g <= 6: 
            
                 
            l = input('Veuillez entrer une lettre : ')
            print("Il vous reste", 6-g,"tentatives")
            mainlist.append (l.upper ())
            listLetter = "-".join(mainlist)
            print(listLetter)
            if l not in w:
            
                

                if g == 1:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |     O      
                                                        |        
                                                        |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")
                elif g == 2:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O      
                                                        |        
                                                        |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")

                elif g == 3:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |        
                                                        |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")
                elif g == 4:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |     |       
                                                        |     |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")
                elif g == 5:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |     |       
                                                        |     |
                                                        |    /
                                                        |
                                                        |
                                                    ___|___""")
                elif g == 6:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |     |       
                                                        |     |
                                                        |    / \\
                                                        |
                                                        |
                                                    ___|___
                                            Vous avez perdu le mot est """+w)
                        with open("log_game.txt", 'a') as f:
                            f.write("Niveau Moyen:\n")
                            print("Le score est {}\n".format(6-g), file=f)
                            print("Le nombre de tentatives est {}\n".format(g), file=f)
                            print("Vous etes a votre partie n'{}\n".format(a), file=f)
                g += 1
                if g > 6:
                    replay()

            else:            
                    list.append(l.lower())
                    # list.sort()
                    word = ''   
                    if guessed == False: 
                        for l in w.lower():                        
                            if l in list:                  
                                word += l                                 
                            else:
                                word +=' _'
                        print(word)
                    if word == w:
                        print (' ')
                        print (f"Bravo vous avez trouver le mot {w} !")
                        print("Score:", (6-g)*len(w))
                        with open("log_game.txt", 'a') as f:
                            f.write("Niveau Difficile:\n")
                            print("Le score est {}\n".format((6-g)*len(w)), file=f)
                            print("Le nombre de tentatives est {}\n".format(g), file=f)
                            print("Vous etes a votre partie n'{}\n".format(a), file=f)
                        print (' ')
                        replay()
                    
   a+=1
   if niveau == 1:
       niveau1()   
   elif niveau == 2:
       niveau2()
   elif niveau == 3:
       niveau3() 
                     
letget() 

