def leng(q):
    cyfry = 1
    m = q
    while m >= 10:
        m = m // 10
        cyfry += 1
    return cyfry


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    n = int(input())

    p = ( (a*10**n) % (b*10**n) ) // b
    print(a//b, ",", '0'*(n-leng(p)), p, sep='')

