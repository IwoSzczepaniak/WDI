def w_fib(q):
    a, b = 1, 1
    while b <= q:
        if b == q:
            return True
        b, a = a+b, b

if __name__ == '__main__':
    x = int(input())
    i = 1
    while i*i <= x:
        if x % i == 0:
            if w_fib(i) is True and w_fib(x//i) is True:
                print("jest praw_da")
#            print(i)
#            print(x//i)
        i += 1
