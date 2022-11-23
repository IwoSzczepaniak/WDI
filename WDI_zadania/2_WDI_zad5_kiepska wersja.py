def leng(q):
    cyfry = 0
    for m in q:
        if m != " ":
            cyfry += 1
    return cyfry


if __name__ == '__main__':
    x = int(input())
    napis = str(x)
    sied = 0
    lista_liczb = []
    for i in range(leng(napis)):
        if int(napis[i]) == 7:
            sied += 1
            lista_liczb.append(int(sied * "7"))
        for j in range(leng(napis)):
            if napis[j] != 7 and napis[i] != 7 and int(napis[i] + napis[j]) % 7 == 0:
                lista_liczb.append(int(napis[i]+napis[j]))
    print(set(lista_liczb))
