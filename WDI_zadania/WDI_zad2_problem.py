def startowe_licz(a, b):
    p_a = a
    p_b = b
    while b <= 2021:
        if b == 2021:
            print("Udało się, dwie pierwsze liczby to: ", p_a, p_b)
        b, a = a+b, b


if __name__ == '__main__':
    x, y = 3, 19
    startowe_licz(x, y)
