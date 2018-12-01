try:
    f = open('HBV_database.json')

except Exception as ex:
    print('Bląd')
    print(ex)
    print(type(ex))
    baza = []
else:
    baza = json.load(f)
    f.close()

finally:
    print('koniec')

