def skoczek(t, x, y):
    t[y][x] = 1
    p = [-2, -2, -2, -2, -1, -1, -1, -1, 1, 1, 1, 1, 2, 2, 2, 2]
    q = [-2, -1, 1, 2, -2, -1, 1, 2, -2, -1, 1, 2, -2, -1, 1, 2]
    if x > len(t) or y > len(t):
        return
    elif x >= 0 and y >= 0:
        for i in range(16):
            if x+p[i] < n and y+q[i] >= 0:
                print("WOW", x, y, p[i], q[i])
                return skoczek(t, x+p[i], y+q[i])


if __name__ == '__main__':
    n = 8
    tablica = [[0] * n for _ in range(n)]
    skoczek(tablica, 0, 0)
    for i in range(n): print(tablica[i])
