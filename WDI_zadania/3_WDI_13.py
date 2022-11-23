from random import randint


if __name__ == '__main__':
    n = 8  # int(input())
    t = [randint(0, 3) for _ in range(n)]
    max_len = 1
    print(t)
    cnt = 0
    for i in range(n):
        for j in range(1, n):
            cnt = 0
            if i != j:
                if t[i] == t[j]:
                    cnt += 1
                    for k in range(1, n):
                        for p in range(1, n):
                            if i+k >= n and j-p >= 0 and i+k <= j-p:
                                if t[i + k] == t[j - p]:
                                    cnt += 1
                                    print(i + k, j - k)
                                    if cnt > max_len:
                                        max_len = cnt
                                        print("O!", max_len)


    print(max_len)
