def division(x, j):
    while j % x == 0:
        j = j // x
    return j


if __name__ == '__main__':
    n = int(input())
    suma = 0
    for i in range (n, 0, -1):
        i = division(2, i)
        i = division(3, i)
        i = division(5, i)
        if i == 1:
            suma += 1
    print(suma)
