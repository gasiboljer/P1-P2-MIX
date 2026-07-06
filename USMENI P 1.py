""" Napisati program koji traži unos 7 cijelih brojeva od korisnika. 
Program treba izračunati i ispisati prosjek svih unesenih brojeva koji su veći od 10. 
Ako nijedan broj nije veći od 10, ispisati poruku 
"Nema brojeva većih od 10". Rezultat zaokružiti na 2 decimale.
brojevi = []
for i in range (7): #prvo unos 7 brojeva
    print("unedsite ", i+1,"br") #ovo plus 1 znaci da ne krece od 0 neg 1
    broj = int(input())
    brojevi.append(broj)
    #sad ovde izdvajamo brojeve vece od 10
    veci_od_10 = []
    for b in brojevi:
        if b > 10:
            veci_od_10.append(b)

#PROSJEK I PORUKA
if len(veci_od_10) == 0:
    print("nema brojeva veci od 10 ")
else:
    prosjek= sum(veci_od_10) / len(veci_od_10)
    print("prosjek br veci od 10", round(prosjek,2))
    #ova funkcija zaokruzuje x na n decimala npr imamo neki br 0.000 zaokruzi na 0.00"""


"""Napisati program koji traži unos rečenice od korisnika. 
Program treba provjeriti sadrži li rečenica riječ "programiranje"
(bez obzira na velika i mala slova). Ako riječ postoji, ispisati "Rečenica sadrži riječ programiranje",
a ako ne postoji, ispisati "Rečenica ne sadrži riječ programiranje".""
recenica = input()
print("unesite recenicu ")
recenica_malim = recenica.lower() #lower jer nam nije bitno jel unesena malim slovima ili ne
#sade ovde gledamo jel programiranje u recenici 

if "programiranje" in recenica_malim:
    print("recenica sadrzi rijec programiranje")
else:
    print("recenica ne sadrzi rijec programiranje")"""

"""Napisati program koji traži unos tri broja od korisnika. 
Program treba ispisati najveći i najmanji uneseni broj. 
Ako su svi brojevi jednaki, ispisati poruku "Svi brojevi su jednaki".
print("unesite 1 broj ")
broj1 = int(input())
print("unesi 2 broj")
broj2 = int(input())
print("unesi 3 broj")
broj3 = int(input())
#gledamo jeu svi jednaki 
if broj1 == broj2 and broj2 == broj3:
    print("svi brojevi su jednaki")
else:
    #sad najveci i najmanji broj
    najveci = max(broj1,broj2,broj3)
    najmanji = min(broj1,broj2,broj3)
    print("najveci broj je ", najveci)
    print("najmanji broj je ", najmanji)"""


""" Napisati program koji traži unos prirodnog broja N (N > 0).
Program treba ispisati sve parne brojeve od 1 do N te izračunati njihov ukupni zbroj. 
Na kraju ispisati i koliko ima parnih brojeva u tom rasponu.


print("unesite n broj")
n = int(input())
zbrajac = 0
brojac = 0
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
        zbrajac += i #ovde i jer dodajem ukuni zbroj
        brojac += 1 #ode kec jer povecavam za 1
        print("ukupan zbr parni br je",zbrajac )
        print("broj parni brojeba je ", brojac)"""


"""Napisati program koji od korisnika traži unos 5 cijelih brojeva.
 Program treba izračunati i ispisati njihov umnožak ako je prvi uneseni broj veći od 15, 
a u suprotnom ispisati njihov zbroj. Rezultat zaokružiti na 2 decimale.
brojevi = []
for i in range (5):
    print("unosi broj ",i+1)
    broj = int(input())
    brojevi.append(broj)
    # provjera prvog broja 
    if brojevi[0] > 15:
        umnozak = 1
        for b in brojevi:
            umnozak *= b
            print("umnozak brojeva je", round(umnozak,2))
        else:
            zbroj = sum(brojevi)
            print("zbroj brojeva je", round(broj,2))"""

"""Napisati program koji će tražiti unos riječi od korisnika. 
Program treba provjeriti je li unesena riječ palindrom (čita se jednako s lijeva i s desna). Ako jest, 
ispisati poruku "Riječ je palindrom", a ako nije ispisati "Riječ nije palindrom". 
Program treba raditi i s velikim i malim slovima (npr. "Ana" je palindrom)."""

print ("unesite rijec")
rijec = input()
rijec_malim = rijec.lower()
if rijec_malim == rijec_malim [::-1]:
    print("rijec je palindrom")
else:
    print("rijec nije palindrom")