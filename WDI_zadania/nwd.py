def sprawdzanie(x, y, z, q):
    if x % q == 0 and y % q == 0 and z % q == 0:
        return True
    else:
        return None
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
        if sprawdzanie(a, b, c, i) is True:
            if nwd < i:
                nwd = i
            if nwd < (a // i) and sprawdzanie(a, b, c, a//i):
                nwd = a // i
            if nwd < (b // i) and sprawdzanie(a, b, c, b//i):
                nwd = b // i
            if nwd < (c // i) and sprawdzanie(a, b, c, c//i):
                nwd = c // i
        i += 1
    print(nwd)
