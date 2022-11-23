if __name__ == '__main__':
    x = (0.5) ** (0.5)
    next = (0.5*(1+x))**(0.5)
    for _ in range (100):
        x *= next
        next = 0.5*(1+next)**0.5
        print(2/x)
