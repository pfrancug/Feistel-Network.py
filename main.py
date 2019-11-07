tekstJawny = input('Podaj tekst jawny: ')
dlugoscTekstuJawnego = len(tekstJawny)

dlugoscKlucza = None

while dlugoscKlucza != 4:
    print('Klucz musi posiadać dokładnie 4 znaki!')
    klucz = input('Podaj klucz: ')
    dlugoscKlucza = len(klucz)

print(klucz)