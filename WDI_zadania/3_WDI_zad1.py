if __name__ == '__main__':
    x = int(input())
    q = int(input())

    while 2 <= q <= 10:
        x_copy = 0
        i = 0
        while x > 0:
            x_copy += (x % q) * 10 ** i
            x //= q
            i += 1
        print(x_copy)
        q = 0

    while 10 <= q <= 16:
        tablica = [] # * 1000    j = 0
        chars = [str(i) for i in range(10)] + [chr(i) for i in range(ord("A"), ord("G"))]
        while x > 0:
            tablica.append(chars[x % q]) # tablica[j] = chars[x%q]
            x //= q
#            j += 1
        print(tablica)
        q = 0
