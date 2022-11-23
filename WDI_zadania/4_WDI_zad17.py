def sum(t):
    n = len(t)
    suma_maxi = 0
    x, y = 0, 0
    for k in range(n):
        for w in range(n):
            gora, dol, prawa, lewa = True, True, True, True
            suma = 0
            if w == 0: gora = False
            if k == 0: lewa = False
            if w == n-1: dol = False
            if k == n-1: prawa = False

            if gora:
                suma += t[w-1][k] # pole z gory
                if prawa:   #skośne pola - prawy gorny i lewy gorny
                    suma += t[w - 1][k+1]
                if lewa:
                    suma += t[w - 1][k-1]
            if dol:
                suma += t[w + 1][k]  # pole z dolu
                if prawa:   #skośne pola - prawy dolny i lewy dolny
                    suma += t[w + 1][k+1]
                if lewa:
                    suma += t[w + 1][k-1]
            if prawa: suma += t[w][k+1] # pole z prawej
            if lewa: suma += t[w][k - 1] # pole z lewej

            if suma_maxi < suma:
                suma_maxi = suma
                y = w
                x = k
                print(suma_maxi)
    return x, y


if __name__=='__main__':
        tab = [[1,1,100,1,], [1,100,1,1], [1,1,1,1],[1,1,1,1]]
        print(*tab, sep = "\n")
        print()
        print(sum(tab))