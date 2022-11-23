def geo_artm(a,b):
    while (a-b) > 0.0001
        a,b = (a*b)**(0.5), (a+b)/2
    return a


if __name__ == '__main__':
    fib_1, fib_2 = 20, 30
    fib_1 = fib_2/fib_1
    fib_2 = 100000000000
    eps = 0.000001
    while abs(fib_1-fib_2) > eps:
        fib_1, fib_2 = fib_2, fib_1+fib_2
        fib_2 = fib_1
        fib_1 = fib_2/fib_1
    print(fib_1)