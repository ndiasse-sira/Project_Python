
from os import system, name 

import random
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def replay():
   rejouer = input('Vous voulez rejouer O/N :')
   if rejouer == "o" or rejouer == "O":
         hangman()
   elif rejouer == "n" or rejouer == "N":
         exit()
         clear()
   else:
      print('Veuillez recommencer entrer O ou N')
      replay()

def hangman():
    
   print(f">>> Bienvenue dans LET-GET <<< \n\t\t")
   niveau = int(input("Veuillez choisir le niveau du jeu : 1 (2-4 lettres), 2 (5-7 lettres), 3 (+7 letters) \n\n"))
   
   a=1
   
   def niveau1():
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
                     
hangman() 

