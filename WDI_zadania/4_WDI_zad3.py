from random import randint


def wyp_tablice(t):
    for line in t:
        print(line)


def ist_parz_cyfra(t):
    warun = False
    if t == 0:
        warun = True
    while t > 0:
        if t % 2 == 0:
            warun = True
        t = t // 10
    return warun


if __name__ == '__main__':
    n = int(input())
    tab = [[0]*n for i in range(n)]
    for i in range(0, n):
       for j in range(0, n):
            tab[i][j] = randint(0, 100)
    wyp_tablice(tab)
    b = 0
    for j in range(0, n):
        x = True
        for i in range(0, n):
            if not ist_parz_cyfra(tab[i][j]):
                x = False
#                print("liczba nie zawiera nawet jednej cyfry parzystej")
        if x:
            print("istnieje wiersz w ktorym wszystkie liczby maja cyfre parzysta")
            break
        if not x:
            b += 1
        if b == n:
            print("Nie istnieje wiersz w ktorym każda liczba ma co najmniej jedna cyfre parzysta")
