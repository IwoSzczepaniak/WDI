n = 20
n += 1
zbior_licz = [i for i in range(n)]
##print(zbior_licz)
zbior_licz[0] = False
zbior_licz[1] = False

for i in range(2, n):
    if zbior_licz[i] > 0:
        for j in range(2*zbior_licz[i], n, zbior_licz[i]):
            print(zbior_licz[i],zbior_licz[j])
            zbior_licz[j] = 0

for el in zbior_licz:
    if el > 0:
        print(el, end=" ")
