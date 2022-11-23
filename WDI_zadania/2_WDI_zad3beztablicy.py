if __name__ == '__main__':
    x = int(input())
    rev_x = 0
    x_copy = x
    while x_copy > 0:
        rev_x = rev_x * 10 + x_copy % 10
        x_copy //= 10
    print(rev_x == x)

    # binarny
    print("Teraz binarnie:")
    x = int(input())
    rev_x = 0
    x_copy = x
    while x_copy > 0:
        rev_x = rev_x * 2 + x_copy % 2
        x_copy //= 2
    print(rev_x == x)
