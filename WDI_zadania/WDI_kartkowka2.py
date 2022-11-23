from math import sqrt

def skok(t):
    n = len(t)
    for i in range(n):
        tmp = t[i]
        k = 2
        while tmp!=1:
            if tmp % k == 0 and i+k < n:
                f[i+k]=min(f[i+k],f[i]+1)
            while tmp%k == 0:
                tmp //= k
            k += 1
    return f[n-1]


if __name__ == '__main__':
    print(min(2,2))

