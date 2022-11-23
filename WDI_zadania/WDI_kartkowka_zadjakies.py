def multi(t):
    n = len(t)
    wyj = False # czy napis wielokrotny
    max_ln = 0
    for i in range(n):
        napis = t[i]
        ln = len(napis)
        print(ln, napis) #dlugosc napisu i sam napis
        for j in range(1, ln):
            x = ln // j
            if napis[0:j] * x == napis:
                wyj = True
                print(wyj) # wypisuje napis wielokrotny
                print(ln) # wypisuje jego dlugosc
                if ln > max_ln:
                    max_ln = ln
                break
    print("\n\n\n", max_ln) # wypisuje dlugosc najdluzeszgo napisu wiel.
    return max_ln


if __name__ == '__main__':
    TAB = ["AAAAAAA", "ABCABC", "ABCDEF"]
    multi(TAB)
