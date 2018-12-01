def pole_prostokata(bok_a, bok_b):
    if bok_a == bok_b:
        print('Kwadrat!')
        return(bok_a)


if __name__ == '__main__':
    wynik = pole_prostokata(2, 3)
    print(wynik)
    pole_prostokata(2, 9)