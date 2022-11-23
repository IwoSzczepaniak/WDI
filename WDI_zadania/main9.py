def skoczek(tab, y_pos=0, x_pos=0, value=1):
    n = len(tab)
    tab[y_pos][x_pos] = value
    if value == n * n:
        print(*tab, sep="\n")
        exit()

    moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
    for i in range(len(moves)):
        new_x = x_pos + moves[i][0]
        new_y = y_pos + moves[i][1]
        if 0 <= new_y < n and 0 <= new_x < n:
            skoczek(tab, y_pos + moves[i][0], x_pos + moves[i][1], value + 1)
    tab[y_pos][x_pos] = 0

if __name__ == '__main__':
    n = 4
    tab = [[0 for _ in range(n)] for _ in range(n)]
    skoczek(tab)
