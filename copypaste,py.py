import csv
with open ("reprezentacije.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    svi_redovi = []
    for red in reader:
        svi_redovi.append(red)

podatci = []
for i in range(1,len(svi_redovi)):
    podatci.append(svi_redovi[i])

import random
tournaments =[]
index = list(range(len(podatci)))
random.shuffle(index)
for i in range(16):
    tournaments.append(podatci[index[i]])
    

    
           