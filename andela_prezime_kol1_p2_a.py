'''
Grupa A
U datoteci clubs.py nalazi se lista od 10 nogometnih klubova iz SHNL lige.
Svaki klub predstavljen je kao tuple oblika: (naziv_kluba, stadion).

Učitavanje podataka:
    Učitaj listu klubova iz datoteke clubs.py.

Formiranje parova:
    Nasumično formiraj parove klubova za odigravanje jednog kola (svaki klub igra jednu utakmicu).
    Za svaki par nasumično odredi koji je klub domaćin, a koji gost, te na kojem stadionu se igra utakmica (stadion domaćina).

Simulacija utakmica:
    Za svaku utakmicu nasumično generiraj broj golova za domaći i gostujući klub (npr. od 0 do 5).
    Sve utakmice spremati u listu riječnika oblika:
    {
        "domacin": "Dinamo Zagreb",
        "stadion": "Stadion Maksimir",
        "gost": "Hajduk Split",
        "golovi_domacin": 2,
        "golovi_gost": 1
    }

    Rezultate utakmice spremi novi array string-ova u formatu:
    NazivDomacina - NazivGosta, golovi_domacin:golovi_gost
    (npr. Dinamo - Hajduk, 1:1).

Analiza rezultata:
    Pomoću regularnih izraza (regex) provjeri u listi stringova i ispiši:
        U koliko utakmica je domaćin postigao barem jedan gol.
        U koliko utakmica je gost postigao barem jedan gol.

Zapis rezultata:
    Sve rezultate utakmica (stringove) ispiši na ekran i upiši u tekstualnu datoteku rezultati_kola.txt.
'''
import csv
from clubs import clubs
print(clubs)
with open ("clubs.py", encoding="utf-8") as f:
    reader = csv.reader(f)
    
    import random
    clubs = []
    domacin = []
    guest = []

    clubs = for i in range(1,len(domacin,guest)):
    clubs.append(domacin)
    clubs.append(guest)
    turnir = []
    indeks = list (range(len(domacin,guest)))
    random.shuffle()
    for i in range (25):
        turnir.append(clubs)

simulacija = []
for i in range(len(turnir)):
    clubs= turnir[i]
    utakmice = {
         "domacin": "Dinamo Zagreb",
        "stadion": "Stadion Maksimir",
        "gost": "Hajduk Split",
        "golovi_domacin": 2,
        "golovi_gost": 1 }
    
naziv_domacina= ['dinamo_zagreb']
naziv_gosta = ['hajduk_split']
golovi_domacina = [2]
golovi_gosta =[1]
dat = open('naziviitd', 'a')
for naziv_domacina, naziv_gosta, golovi_domacina, golovi_gosta in turnir:
    dat.write(naziv_domacina + ',' + naziv_gosta + ',' + str(golovi_gosta) + ',' + str(golovi_domacina) + '\n')

dat.close()

import re

