# Wprowadzenie tekstu
tekstJawny = ''
while len(tekstJawny) == 0:
    tekstJawny = input('Podaj tekst jawny: ')

# Wprowadzenie klucza 4-znakowego
klucz =''
while len(klucz) != 4:
    klucz = input('Podaj 4-znakowy klucz: ')

# funkcja zamieniajaca ciag znakow na bity
def zamianaTekstuNaBity(tekstDoZmiany):
    ciagBitow = ''
    for znak in tekstDoZmiany:
        kodASCII = ord(znak)
        kodBinarny = bin(kodASCII)[2:].zfill(8)
        ciagBitow += kodBinarny
    return ciagBitow

# Zamiana tekstu jawnego i klucza na bity
ciagBitowTekstuJawnego = zamianaTekstuNaBity(tekstJawny)
ciagBitowTekstuJawnego += '0' * (64 - len(ciagBitowTekstuJawnego) % 64)
ciagBitowKlucza = zamianaTekstuNaBity(klucz)

# funkcja feistela
def funkcjaFeistela(ciagBitowTekstuJawnego, ciagBitowKlucza):
    ciagBitowTekstuZaszyfrowanego = '01' * 32

    return ciagBitowTekstuZaszyfrowanego

zaszyfrowaneBity = funkcjaFeistela(ciagBitowTekstuJawnego, ciagBitowKlucza)
print(zaszyfrowaneBity)