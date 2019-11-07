tekstJawny = input('Podaj tekst jawny: ')
dlugoscTekstuJawnego = len(tekstJawny)

dlugoscKlucza = None

# Sprawdzenie dlugosci klucza
while dlugoscKlucza != 4:
    print('Klucz musi posiadać dokładnie 4 znaki!')
    klucz = input('Podaj klucz: ')
    dlugoscKlucza = len(klucz)

# Uzupelnienie dlugosci tekstu jawnego
# do wielokrotnosci 8 znakow (64 bit)

if dlugoscTekstuJawnego % 8:
    print(dlugoscTekstuJawnego % 8)