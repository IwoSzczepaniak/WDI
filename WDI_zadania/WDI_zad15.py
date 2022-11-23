if __name__ == '__main__':
    x = (0.5) ** (0.5)
    nex = (0.5*(1+x))**(0.5)
    for _ in range(100):
        x *= nex
        nex = (0.5*(1+nex))**(0.5)
    print(2/x)
