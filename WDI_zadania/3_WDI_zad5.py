def find_kth_smallest(tab, k):
    def insert(tab, val):  # logarithmic
        p = 0
        q = len(tab) - 1

        while p <= q:
            s = (p + q) // 2

            if tab[s] > val:
                q = s - 1
            elif tab[s] < val:
                p = s + 1
            else:
                break

        if tab[s] == val:
            return False
        elif tab[s] > val:
            s -= 1

        for j in range(1, s + 1):
            tab[j - 1] = tab[j]

        tab[s] = val

        return True

    greatest = [float("-inf")] * k

    for el in tab:
        insert(greatest, el)

    return greatest[0]


*arr, _ = map(int, input().split())

k = 10
sort = list(reversed(sorted(set(arr))))
print(sort)
print(sort[k - 1])
my = find_kth_smallest(arr, k)
print(my)
print(my == sort[k - 1])