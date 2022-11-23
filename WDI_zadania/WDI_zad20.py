def geo_artm(a, b):
    while abs(a-b) > 0.0001:
        a, b = (a*b)**(0.5), (a+b)/2
    return a


if __name__ == '__main__':
    x = float(input())
    y = float(input())
    print(geo_artm(x, y))
