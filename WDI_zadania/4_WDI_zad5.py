from random import randint


def wyp_tablice(t):
    for line in t:
        print(line)


def suma_wiersz(t, a, b):
    s = 0
    for ij in range(0, n):
        s += t[a][ij]
    return s


def suma_kolumna(t, a, b):
    s = 0
    for ij in range(0, n):
        s += t[ij][b]
    return s


if __name__ == '__main__':
    n = int(input())
    tab = [[0]*n for i in range(n)]
    for i in range(0, n):
       for j in range(0, n):
            tab[i][j] = randint(-100, 100)
    wyp_tablice(tab)
    maxi = 0
    for i in range(0, n):
       for j in range(0, n):
        iloraz = suma_kolumna(tab, i, j) / suma_wiersz(tab, i, j)
        while iloraz > maxi:
            maxi = iloraz
            i_maxi = i
            j_maxi = j
    print(tab[i_maxi][j_maxi], "OTO el. MAXI\n")
    print("kolumna maxi:")
    for p in range(0, n):
        print(tab[p][j_maxi], end=",")
    print()
    print("wiersz maxi:")
    for q in range(0, n):
        print(tab[i_maxi][q], end=",")

