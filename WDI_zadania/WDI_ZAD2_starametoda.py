
def fibonacci(a,b):

    #print(a, b, " to dane poczatkowe przykladu", end=" ")
    m=0
    for i in range(10000):
        if a == 2021 and rand1 <= rand2:
            print("!!!znalazłem rok 2021 w kroku!!! nr ", m,"o startowych liczbach: ",rand1,rand2, "ktorych SUMA TO: ", rand1+rand2)
            break
        else:
            #print(a, "\n")
            temp = b
            b = a + b
            a = temp
            m = m + 1



    return 0

if __name__ == '__main__':
    kolej = 1
    import random
    for i in range(10000):
        rand1 = random.randint(1, kolej)
        rand2 = random.randint(1, kolej)
        if kolej < 30:
            kolej = kolej+1
        else:
            kolej = 1
        fibonacci(rand1,rand2)