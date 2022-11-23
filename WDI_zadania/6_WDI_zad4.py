def skoczek(t, p, y=0, x=0, cnt=1):
    t[y][x] = cnt
    m = len(t)
    for i in range(len(p)):
        xp = p[i][0]
        yp = p[i][1]
        if (0 <= x+xp <= m-1) and (0 <= y+yp <= m-1) and t[y+yp][x+xp] == 0:
            skoczek(t, p, y + yp, x + xp, cnt + 1)


    def szachownica(n):
        tablica = [[0] * n for _ in range(n)]
        q = [[2, 1], [1, 2], [2, -1], [-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2]]
        skoczek(tablica, q)


if __name__ == '__main__':
    n = 5
    tablica = [[0] * n for _ in range(n)]
    q = [[2, 1], [1, 2], [2, -1], [-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2]]
    skoczek(tablica, q)
    for i in range(n): print(tablica[i])
