dlugoscTekstuJawnego = 0

while dlugoscTekstuJawnego == 0:
    tekstJawny = input('Podaj tekst jawny: ')
    dlugoscTekstuJawnego = len(tekstJawny)

dlugoscKlucza = 0

# Sprawdzenie dlugosci klucza
while dlugoscKlucza != 4:
    print('Klucz musi posiadać dokładnie 4 znaki!')
    klucz = input('Podaj klucz: ')
    dlugoscKlucza = len(klucz)

# Uzupelnienie dlugosci tekstu jawnego
# do wielokrotnosci 8 znakow (64 bit)
if dlugoscTekstuJawnego % 8:
    for i in range(dlugoscTekstuJawnego % 8, 8):
        # tekstJawny = tekstJawny + '0'
        tekstJawny += '0'
    dlugoscTekstuJawnego = len(tekstJawny)

# konwersja tekstu jawnego na bity
tablicaBitowJawnych = []