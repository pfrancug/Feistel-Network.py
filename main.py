# wprowadzenie danych
dlugoscTekstuJawnego = 0
while dlugoscTekstuJawnego == 0:
    tekstJawny = input('Podaj tekst jawny: ')
    dlugoscTekstuJawnego = len(tekstJawny)

# wprowadzenie klucza
dlugoscKlucza = 0
while dlugoscKlucza != 4:
    print('Klucz musi posiadać dokładnie 4 znaki!')
    klucz = input('Podaj klucz: ')
    dlugoscKlucza = len(klucz)

# uzupelnienie dlugosci tekstu jawnego
# do wielokrotnosci 8 znakow (64 bit)
if dlugoscTekstuJawnego % 8:
    for i in range(dlugoscTekstuJawnego % 8, 8):
        tekstJawny += '0'
    dlugoscTekstuJawnego = len(tekstJawny)

# konwersja tekstu jawnego na bity
tablicaBitowJawnych = []
for i in range(0, dlugoscTekstuJawnego):
    kodASCII = ord(tekstJawny[i])
    osiemBit = bin(kodASCII)[2:].zfill(8)
    tablicaBitowJawnych += osiemBit

# konwersja klucza na bity
tablicaBitowKlucza = []
for i in range(0, 4):
    kodASCII = ord(klucz[i])
    osiemBit = bin(kodASCII)[2:].zfill(8)
    tablicaBitowKlucza += list(map(int,osiemBit))

# podzial na bloki 64 i 32 bit
bloki = []
for i in range(0, len(tablicaBitowJawnych), +64):
    lewa = list(map(int,tablicaBitowJawnych[i:i+32]))
    prawa = list(map(int,tablicaBitowJawnych[i+32:i+64]))
    bloki.append([lewa, prawa])

# szyfrowanie
zaszyfrowaneBloki = []
for i in range(0,len(bloki)):
    lewa = bloki[i][0]
    prawa = bloki[i][1]
    lewaPrim = prawa
    # P' = L XOR ( K AND P )
    AND = list(map(lambda n1, n2: n1 & n2, tablicaBitowKlucza, prawa))
    prawaPrim = list(map(lambda n1, n2: n1 ^ n2, lewa, AND))
    
    print(lewa, prawa)
    print(lewaPrim, prawaPrim)