import json
from datetime import datetime


def wczytaj_z_pliku(nazwaPliku):
    try:
        f = open(nazwaPliku)
    except FileNotFoundError:
        dane = []
    else:
        dane = json.load(f)
        f.close()
    return dane


def zapisz_do_pliku(nazwa, dane):
    with open(nazwa, 'w') as f:
        json.dump(dane, f)


def wczytaj_czas():
    teraz = str(datetime.now())
    return teraz


def wczytaj_dane(zapytanie):
    wczytane = input(zapytanie)
    return wczytane


def nowy_pacjent(naglowki, dane, IDlist):
    if not IDlist:
        count = 0
    else:
        count = IDlist[-1]
    pacjent = {naglowki[0]: count + 1}

    pacjent[naglowki[1]] = wczytaj_czas()
    for klucz in naglowki[2:]:
        while True:
            wpis = input('Insert ' + klucz + ':')
            if klucz == naglowki[2] and wpis not in ['M', 'F']:
                print('Insert a valid information: F for female, M for male')
            elif klucz in naglowki[3:6] and not wpis.isdigit():
                print('Insert a valid number')
            else:
                pacjent[klucz] = wpis
                break

    dane.append(pacjent)
    print('Database updated!')
    return dane


def modyfikacja_wpisu(naglowki, dane, IDlist):
    while True:
        print(IDlist)
        ktory_pacjent = wczytaj_dane('Which patient ID you want to modify?')
        ktory_pacjent_int = int(ktory_pacjent)
        if ktory_pacjent_int in IDlist:
            break
        else:
            print('You must select a valid ID!')
    while True:
        print(naglowki[2:])
        jakie_dane = wczytaj_dane('Which information from the above list you want to modify?')
        if jakie_dane in naglowki[2:]:
            break
        else:
            print('You must select a valid information name!')
    while True:
        nowe_dane = wczytaj_dane('Insert a new value:')
        if nowe_dane:
            break
        else:
            print('You must insert a valid value!')
    for n in dane:
        if n['ID'] == ktory_pacjent:
            n[jakie_dane] = nowe_dane
            print('Entry updated!')
    return dane


def nowa_kolumna(naglowki, dane):
    nowa_kol = wczytaj_dane('Insert new column title:')
    if nowa_kol in naglowki:
        print('This column exists!')
    else:
        naglowki.append(nowa_kol)
        print(naglowki)
        for n in dane:
            n[nowa_kol] = ''
    return dane, naglowki


def eksport_wybranych(dane, IDlist):
    lista_wybrane = []
    lista_wybrane_rekordy = []
    while True:
        wybor_pacjenta = wczytaj_dane('Select patient ID. If all selected, press 0')
        if wybor_pacjenta == '0':
            break
        if int(wybor_pacjenta) not in IDlist:
            print('This ID is not in a database.')
            continue
        lista_wybrane.append(wybor_pacjenta)

    if lista_wybrane:
        nazwa_pliku = '_'.join(lista_wybrane) + '.json'
        for ID in lista_wybrane:
            for n in dane:
                if n['ID'] == int(ID):
                    lista_wybrane_rekordy.append(n)

        print('Selected IDs for export:', lista_wybrane)
        zapisz_do_pliku(nazwa_pliku, lista_wybrane_rekordy)
    else:
        print('No IDs selected!')
