def wyp_tablice(t):
    for line in t:
        print(line)


def warun(t, m):
    warunek = False
    for p in range(m):
        for q in range(m):
            if t[p][q] == 0:
                warunek = True
    return warunek


if __name__ == '__main__':
    n = int(input())
    tab = [[0]*n for i in range(n)]
    kierunek = 0
    x, y = n, n
    liczba = 1

    while warun(tab, n):
        if kierunek == 0:  # prawo
            for i in range(n - y, x):
                tab[n - y][i] = liczba
                liczba += 1
            y -= 1
            kierunek += 1
        elif kierunek == 1:  # dol
            for i in range(n - y, y):
                tab[i][x-1] = liczba
                liczba += 1
            kierunek += 1
        elif kierunek == 2:  # lewo
            for i in range(x, n - x, -1):
                tab[y][i - 1] = liczba
                liczba += 1
            kierunek += 1
        elif kierunek == 3:  # gora
            for i in range(y, n - y, -1):
                tab[i - 1][n - x] = liczba
                liczba += 1
            x -= 1
            kierunek = 0

        warun(tab, n)

    wyp_tablice(tab)
