def is_2021_in_fib(f1,f2):
    if f1 >= f2:
        f1, f2 = f2, f1
    while f2 < 2021:
        f1, f2 = f2, f1+ f2
    return f2 == 2021


if __name__ == '__main__':
    sum = 3
    found = False
    while not found:
        for x in range(1,sum//2 + 1):
            found = is_2021_in_fib(x, sum - x)
            if found:
                print(x, sum-x)
                break
        sum += 1

