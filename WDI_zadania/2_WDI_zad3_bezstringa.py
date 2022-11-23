def polidrom(x):
    lista_x = []
    while x >= 1:
        lista_x.append(x % 10)
        x = x // 10
    rev = lista_x[::-1]
    if lista_x == rev:
        return "jest palindromem"
    else:
        return "nie jest palindromem"


def bi(q):
    p = q
    bi_wyjsciowe = 0
    if p % 2 != 0:
        bi_wyjsciowe += 1
    while p > 1:
        i = 0
        while q > 1:
            if q % 2 == 0:
                q = q // 2
                i += 1
            else:
                q = q - 1
        bi_wyjsciowe += 10 ** i
        p = p - (2 ** i)
        q = p
    return bi_wyjsciowe


if __name__ == '__main__':
    a = int(input())
    print("W systemie dziesiętnym podana liczba zapisana jako:", a, polidrom(a))
    print("\nW systemie dwojkowym ta sama liczba zapisana jako:", bi(a), polidrom(bi(a)))
