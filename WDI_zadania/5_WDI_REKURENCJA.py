def sum_(T,i):
    if i == len(T)-1:
        return T[i]
    return T[i] + sum_(T, i + 1)

if __name__ == '__main__':
    TAB = [2, 4, 3, 1, 5, 8]
    print(sum_(TAB, 0))
