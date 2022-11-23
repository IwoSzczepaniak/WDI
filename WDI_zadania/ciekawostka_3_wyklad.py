if __name__ == '__main__':
    cnt = 0
    for x in range(11, 200):
        rev_x = 0
        x_copy = x
        while x_copy > 0:
            rev_x = rev_x * 10 + x_copy % 10
            x_copy //= 10
#        print(x, rev_x)
        if rev_x != x:
            x_copy += rev_x
            cnt += 1
        else:
            print(x, rev_x)
    print(cnt)
