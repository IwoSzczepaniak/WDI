from math import sqrt
def prime(x):
    if x < 1: return False
    if x == 2 or x == 3: return True
    if x % 2 ==0 or x % 3 == 0: return False
    i = 5
    while i < sqrt(x) + 1:
        if x % i == 0: return False
        i += 2
        if x % i == 0: return False
        i += 4
    return True