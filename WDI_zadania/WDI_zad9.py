if __name__ == '__main__':

    x = int(input())
    i = 1
    while i*i <= x:
        if x % i == 0:
            print(i)
            if i != x//i:
                if x//i != x:
                    print(x//i)
        i += 1
    print(x)