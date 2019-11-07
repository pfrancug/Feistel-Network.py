# -------------------------------------
# -------- wprowadzenie danych --------
# -------------------------------------

# wprowadzenie tekstu jawnego
tekstJawny = ''
while len(tekstJawny) == 0:
    tekstJawny = input('Podaj tekst jawny: ')

# wprowadzenie klucza
klucz = ''
while len(klucz) != 4:
    klucz = input('Podaj 4-znakowy klucz szyfrujący: ')

# ------------------------------------------
# -------- konwersja danych na bity --------
# ------------------------------------------

# uzupełnienie długości tekstu jawnego do wielokrotności ósemki
if len(tekstJawny) % 8:
    for i in range(len(tekstJawny) % 8, 8):
        tekstJawny += '0'

# konwersja tekstu jawnego na bity
postacBinarnaTekstuJawnego = []
for i in range(0, len(tekstJawny)):
    kodASCII = ord(tekstJawny[i])
    osiemBit = bin(kodASCII)[2:].zfill(8)
    postacBinarnaTekstuJawnego += list(map(int, osiemBit))

# konwersja klucza na bity
postacBinarnaKlucza = []
for i in range(0, 4):
    kodASCII = ord(klucz[i])
    osiemBit = bin(kodASCII)[2:].zfill(8)
    postacBinarnaKlucza += list(map(int, osiemBit))

# -------------------------------------
# -------- podział na bloki -----------
# -------------------------------------

blokiTekstuJawnego = []
for i in range(0, len(postacBinarnaTekstuJawnego), +64):
    lewa = postacBinarnaTekstuJawnego[i:i + 32]
    prawa = postacBinarnaTekstuJawnego[i + 32:i + 64]
    blokiTekstuJawnego.append([lewa, prawa])

# -----------------------------
# -------- szyfrowanie --------
# -----------------------------

szyfrowaneBloki = blokiTekstuJawnego
for i in range(0, 2):
    for j in range(0, len(szyfrowaneBloki)):
        lewa = szyfrowaneBloki[j][0]
        prawa = szyfrowaneBloki[j][1]
        lewaPrim = prawa
        # P' = L XOR ( K AND P )
        funkcjaAND = list(map(lambda n1, n2: n1 & n2,
                              postacBinarnaKlucza, prawa))
        prawaPrim = list(map(lambda n1, n2: n1 ^ n2, lewa, funkcjaAND))
        szyfrowaneBloki[j][0] = lewaPrim
        szyfrowaneBloki[j][1] = prawaPrim

# -----------------------------------------
# -------- konwersja bitów na dane --------
# -----------------------------------------

# połączenie zaszyfriwanych bloków
zaszyfrowanaPostacBinarna = ''
for blok64 in range(0, len(szyfrowaneBloki)):
    ciag64bitow = ''
    for blok32 in range(0, len(szyfrowaneBloki[blok64])):
        ciag64bitow += ''.join(map(str, szyfrowaneBloki[blok64][blok32]))
    zaszyfrowanaPostacBinarna += ciag64bitow

# konwersja zaszyfrowanych bitów na tekst
szyfrogram = ''
for i in range(0, len(zaszyfrowanaPostacBinarna), +8):
    kodASCII = int(zaszyfrowanaPostacBinarna[i:i+8], 2)
    znak = chr(kodASCII)
    szyfrogram += znak

# ------------------------------------------
# -------- wyświetlenie szyfrogramu --------
# ------------------------------------------

print(szyfrogram)
