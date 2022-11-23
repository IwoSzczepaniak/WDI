def multi(t):
    n = len(t)
    max_ln = 0
    for i in range(n):
        napis = t[i]
        ln = len(napis)
        for j in range(1, ln):
            x = ln // j
            if napis[0:j] * x == napis:
                if ln > max_ln:
                    max_ln = ln
                break
    return max_ln


if __name__ == '__main__':
    TAB = ["AAAAAAA", "ABCABC", "ABCDEF"]
    print(multi(TAB))
