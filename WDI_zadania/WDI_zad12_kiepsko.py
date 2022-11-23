if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    i = 1
    nwd = 1
    max = a

    if max < b:
        max = b
    if max < c:
        max = c

    while i//2 <= max:
        if a % i == 0 and b % i == 0 and c % i == 0:
            if nwd < i:
                nwd = i
            if nwd < (a // i) and b % a // i == 0 and c % a // i == 0:
                nwd = a // i
            if nwd < (b // i) and a % b // i == 0 and c % b // i == 0:
                nwd = b // i
            if nwd < (c // i) and a % c // i == 0 and b % c // i == 0:
                nwd = c // i
        i +=1
    print(nwd)

