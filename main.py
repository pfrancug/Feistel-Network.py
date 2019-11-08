# Wprowadzenie tekstu
tekstJawny = ''
while len(tekstJawny) == 0:
    tekstJawny = input('Podaj tekst jawny: ')

# Wprowadzenie klucza 4-znakowego
klucz =''
while len(klucz) != 4:
    klucz = input('Podaj 4-znakowy klucz: ')

# Zamiana tekstu jawnego na bity
ciagBitowTekstuJawnego = ''
for znak in tekstJawny:
    kodASCII = ord(znak)
    kodBinarny = bin(kodASCII)[2:].zfill(8)

    print(znak, kodASCII, kodBinarny)