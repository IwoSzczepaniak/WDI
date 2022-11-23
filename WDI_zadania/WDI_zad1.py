def fib(x):
    a,b = 1,1
    while a < x:
        print (a, "\n")
        b,a = a+b,b
    return a





    return 0

if __name__ == '__main__':
    x = int(input())

    fib(x)