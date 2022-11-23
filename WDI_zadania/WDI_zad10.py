if __name__ == '__main__':
    x = 0
    while x < 1000000:
        i = 1
        suma = 0
        while i * i <= x:
            if x % i == 0:
                suma += i
                if i != x // i:
                    if x // i != x:
                        suma += (x//i)
            i += 1
        if x == suma:
            print(x)
        x += 1
