class Node:
    def __init__(self, v):
        self.val = v
        self. next = None


class Zbior:
    def __init__(self):
        self.first = None


def insert(z, el):
    n = z.first
    m = None  # m to poprzednik

    while n != None and n.val < el:
        m = n
        n = n.next

    if n != None and n.val == el:  # el wystpeuje wczesniej, nic nie robimy
        return

    e = Node(el)
    if n != None and m != None:  # wstawiamy w srodek i na koniec
        m.next = e
        e.next = n
    else:  # wstawianie na początek i gdy zbior pusty
        e.next = z.first
        z.first = e
    return


    #zbior pusty                1
    #n.val == el, el występuje  2
    #el wstawiamy w srodek      3
    #wstawiamy na poczatek      4
    #wstawiamy na koniec        5