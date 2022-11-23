from math import sqrt


def is_prim(n):
    prime = True
    if n == 0 or n == 1:
        prime = False
    if n == 2 or n == 3:
        prime = True
    if n >= 4 and (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while i <= sqrt(n):
        if n % i == 0: prime = False
        i += 2
        if n % i == 0: prime = False
        i += 4
    return prime


if __name__ == '__main__':
    a = int(input())
    for s in range(3, 16+1): # w zapisie dwójkowym nie wystepuja prime'y
        tmp = a
        all_prime = True
        while tmp != 0:
            if not is_prim(tmp % s):
                all_prime = False
                break
            tmp = tmp // s
        if all_prime:
            print("True")
            break

