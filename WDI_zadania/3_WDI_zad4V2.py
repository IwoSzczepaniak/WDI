def leng(q):
    cyfry = 1
    m = q
    while m >= 10:
        m = m // 10
        cyfry += 1
    return cyfry


if __name__ == '__main__':
#    n = int(input())
    n = 100
    e = 1.0
    old_e = 0
    i = 1
    silnia = 1
    j = 1
    while old_e != e:
        for _ in range(1, i + 1):
            silnia *= j
            j += 1

        a = 1
        b = silnia
        #p = ((a * 10 ** n) % (b * 10 ** n)) // b
        #suma = a//b + p * 10 ** (- leng(p) - (n - leng(p)))
        print(a // b, "." if a % b != 0 else "", sep="", end="")
        a %= b
        while a > 0 and n > 0:
            a *= 10
            print(a // b, end="")
            a %= b
            n -= 1

        old_e = e
#        e += suma
        print(e, silnia)
    print(e)


