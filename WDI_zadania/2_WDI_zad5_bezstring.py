def leng(q):
    cyfry = 1
    m = q
    while m >= 10:
        m = m // 10
        cyfry += 1
    return cyfry


def create_number(m):
    count = 0
    for i in range(1, 2 ** leng(n)):
        temp_i = i
        temp_n = m
        potega_10 = 0
        created = 0
        while temp_n != 0:
            if temp_i % 2 == 1:
                created += (temp_n % 10) * (10 ** potega_10)
                potega_10 += 1
            temp_n //= 10
            temp_i //= 2
        if created % 7 == 0:
            count += 1
            print(created)

    return count


if __name__ == '__main__':
    n = int(input())
    print(create_number(n))

