"""
Zadatak 3.
Koristi while petlju i break iskaz za unos podataka o sudionicima nekog događaja.

Traži od korisnika unos imena, prezimena i e-mail adrese, koje spremi u zasebne liste.
Za dodavanje koristiti funkciju koja prima ime, prezime i e-mail kao parametre, ali ne vraća ništa.

Unos traje sve dok korisnik ne unese prazan string za ime ili prezime.

Program se ne smije zaustaviti sve dok se ne registrira minimalno 5 sudionika, pri čemu su ime i prezime duži od 3 slova, a e-mail mora sadržavati simbol '@'.

Na završetku ispiši ukupan broj sudionika i njihove podatke u obliku (šifra - ime - prezime - e-mail).

Upotrijebi biblioteku random za nasumično odabiranje jednog sudionika, ispiši njegovo ime i prezime i dodijeli mu nasumičnu nagradu u vidu broja (npr. od 1 do 1000).
"""
import random
im = []
pr_ez =[]
e_mailovi= []
def sudionik_add(ime,prezime,email):
    im.append(ime)
    pr_ez.append(prezime)
    e_mailovi.append(email)
broj_vaz = 0
while True :
    ime = input("unesi ime")
    prezime = input("unesi prez")
    if ime =="":
     if broj_vaz < 5:
        print ("treba unjet 5 sudionika")
        continue
    else:
     break
    if prezime =="":
     if broj_vaz < 5:
        print ("treba unjet 5 sudionika")
        continue
    else:
     break
email = input("unesi svoj mejl")