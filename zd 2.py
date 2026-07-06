"""Zadatak 2.
Napiši funkciju koja prima dva parametra: broj i množitelj. Funkcija treba vratiti rezultat množenja dva broja.
Zatraži od korisnika unos 8 brojeva i spremi ih u listu.
Stvori novi niz u koji ćeš spremiti rezultate pozivanja funkcije, gdje je prvi parametar broj iz niza, a drugi parametar je index tog broja.
Na primjer, za brojeve [2, 4, 6], rezultati bi bili [2 * 0, 4 * 1, 6 * 2], tj. [0, 4, 12].
Ispiši rezultate u obrnutom redoslijedu."""

def mnozim (broj , mnozit):
    return broj * mnozit
brojevi = []
for i in range(8):
    broj = int(input("unesi broj: "))
    brojevi.append(broj)
while i < len(brojevi):
rezt= []
for i in range(len(brojevi)):
    rez = mnozim(brojevi[i], i)
    rez.append(rez)
print("rez u obr red:")
print(rez[::-1])