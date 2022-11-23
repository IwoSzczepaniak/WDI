def prime(n):
    if n == 0 or n == 1: return False
    if n == 2 or n == 3: return True
    if n%2 == 0 or n%3==0: return False
    i = 5
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i+=4
    return True


def sum(num1,num2, T):
    if num1 == 0 and num2 == 0:
        print(T)
        if prime(int(T)):
            return 1
        else:
            return 0
    else:
        suma = 0
        if num1 > 0:
            suma += sum(num1 // 10, num2, str(num1 % 10) + T)
        if num2 > 0:
            suma += sum(num1, num2 // 10, str(num2 % 10) + T)
        return suma


if __name__=='__main__':
        print(sum(16, 263, ""))

