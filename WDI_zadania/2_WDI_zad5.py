def leng(q):
    cyfry = 0
    for m in q:
        if m != " ":
            cyfry += 1
    return cyfry




if __name__ == '__main__':
    x = int(input())
    napis = str(x)
    lista_napis = []
    m = 10
    for i in range(leng(napis)):
        lista_napis.append(x % m)
        x = x // m
    lista_napis = lista_napis[::-1]
    print(lista_napis)
    print(napis[0])
    #napisz algorytm usuwajacy po jednej, dwoch, ... az do leng liczb z napisu, potem sprawdz czy % 7 == 0
