def skoczek(t, x, y):
    t[y][x] = 1
    if x > len(t) or y > len(t):
        return
#    p = [-2, -2, -2, -2, -1,, -1, -1, -1, 1, 1, 1, 1, 2, 2, 2, 2]
#    q = [-2, -1, 1, 2, -2, -1, 1, 2, -2, -1, 1, 2, -2, -1, 1, 2]
    else:
        if x+2 < n and y-1 >= 0: return skoczek(t, x+2, y-1)

        if x+2 < n and y+1 < n: return skoczek(t, x+2, y+1)

        if x+1 < n and y+2 < n: return skoczek(t, x+1, y+2)

        if x+1 < n and y-2 >= 0: return skoczek(t, x+1, y-2)

        if x-1 >= 0 and y+2 < n: return skoczek(t, x-1, y+2)

        if x-1 >= 0 and y-2 >= 0: return skoczek(t, x-1, y-2)

        if x-2 >= 0 and y+1 < n: return skoczek(t, x-2, y+1)

        if x-2 >= 0 and y-1 >= 0: return skoczek(t, x-2, y-1)


if __name__ == '__main__':
    n = 8
    tablica = [[0] * n for _ in range(n)]
    skoczek(tablica, 0, 0)
    for i in range(n): print(tablica[i])
