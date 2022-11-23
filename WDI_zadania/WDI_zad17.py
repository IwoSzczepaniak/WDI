if __name__ == '__main__':
    fib_1 = int(input())
    fib_2 = int(input())
    for _ in range(1000):
        fib_1, fib_2 = fib_2, fib_1+fib_2
    print(fib_2/fib_1)
