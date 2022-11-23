from random import randint


def wyp_tablice(t):
    for line in t:
        print(line)


def nieparz(t):
    warun = True
    if t == 0:
        warun = False
    while t > 0:
        if t % 2 == 0:
            warun = False
        t = t // 10
    return warun


if __name__ == '__main__':
    n = int(input())
    tab = [[0]*n for i in range(n)]
    for i in range(0, n):
       for j in range(0, n):
            tab[i][j] = randint(0, 1000000)
    wyp_tablice(tab)

    for j in range(0, n):
        x = False
        for i in range(0, n):
            if nieparz(tab[i][j]):
                x = True
#                print("nieparzysta")
        if not x:
            print("w którymś wierszu nie istnieje nawet jedna liczba złożona tylko z cyfr nieparzystych")
            break
