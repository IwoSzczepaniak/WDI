def prime(n):
    if n == 0 or n == 1: return False
    if n == 2 or n == 3: return True
    if n > 4 and n % 2 == 0 and n % 3 == 0: return False
    i=5
    while n >= i*i:
        if n % i == 0: return False
        i += 2
        if n % i == 0: return False
        i += 4


def wycinanie(tab, pos):
    n = len(tab)
    if pos == n:
        return True
    for i in range(pos+1, n+1):
        if prime(tab[pos:i]) and wycinanie(tab, i):
            return True
    return False
