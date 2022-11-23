if __name__ == '__main__':

    a = input()
    b = input()
    digits = [0] * 10

    for j in a:
        digits[int(j)] += 1
    for j in b:
        digits[int(j)] -= 1

    for i in range(10):
        if digits[i] != 0:
            print("NIE")
            break
    else:
        print("TAK")
