def masa(T, M, i, s):
    i=0
    if i == len(T)-1:
        return T[i] + s == M or s == M
    return masa(T,M, i+1, s+ T[i]) or masa(T,M, i + 1, s + T[i])

if __name__ == '__main__':
    TAB = [1, 2, 3, 4]
    M = 8
    n = len(TAB)
    s = int(input())
    print(masa(TAB, M, n, s))
