from funkcje import *

baza = wczytaj_z_pliku('HBV_database.json')

if not baza:
    klucze = ['ID', 'entry_date', 'sex_(M/F)', 'age', 'BMI', 'years_after_diagnosis']
else:
    klucze = []
    for key in baza[0].keys():
        klucze.append(key)

print('Welcome to HBV 2018 database')
while True:
    lista_ID = [n['ID'] for n in baza]
    print('****************')
    print('''What can I do for you?
    New patient entry: press 1
    Entry modification: press 2
    Add new column: press 3
    Print existing database: press 4
    Print data for selected patient: press 5
    Close database and save changes: press 0
    ''')
    selection = input()

    if baza == [] and selection == '2':
        print('The database is empty!')
        break

    if selection == '1':
        nowy_pacjent(naglowki=klucze, dane=baza, IDlist=lista_ID)

    if selection == '2':
        modyfikacja_wpisu(naglowki=klucze, dane=baza, IDlist=lista_ID)

    if selection == '3':
        nowa_kolumna(naglowki=klucze, dane=baza)

    if selection == '4':
        print(baza)

    if selection == '5':
        eksport_wybranych(dane=baza, IDlist=lista_ID)

    if selection == '0':
        print('Thank you for using HBV 2018 database!\nThe database is as follows:')
        for rekord in baza:
            print(rekord, '\n')

        zapisz_do_pliku('HBV_database.json', baza)
        break
