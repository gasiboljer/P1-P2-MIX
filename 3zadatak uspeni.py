"""napisite program koji provjerava sadrzi unesi niz znakova barem jednu znamenku te ispisuje da ili ne"""
niz = input("unesi niz z ")
znamenka = 0
have = False
for z in niz:
    if z.isdigit():
        znamenka = int(z)
        have = True
        break  
if have:
    print("DA")
    print(znamenka)
else:
    print("NE")
znamenka = 0
broj= int(input("unesite brojcanu znamenku"))
if broj 