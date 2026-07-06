"""fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)"""
"""
fhand = open('mbox-short.txt')
inp = fhand.read() # Učitaj SVE u varijablu 'inp'
print(len(inp))    # Ispisuje: 94626 (broj znakova)
print(inp[:20])    # Ispisuje prvih 20 znakova"""
"""
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)"""
"""
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # Briše \n s kraja
    if line.startswith('From:'):
        print(line)"""
"""
fname = input('Unesite ime datoteke: ') # Korisnik upiše npr. "mbox.txt"
fhand = open(fname)                     # Program otvara ono što je korisnik upisao
count = 0

for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
"""
fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip() # Mičemo nevidljivi \n s kraja reda
    print(line.upper())  # Pretvaramo u velika slova i ispisujemo"""
    