import random

mots = []
with open ("mots.txt") as fl:
            for l in fl:
                mots.append(l.rstrip("\n"))
while len(mots) == 4 :                
    mot = random.choice(mots)
print(mot)