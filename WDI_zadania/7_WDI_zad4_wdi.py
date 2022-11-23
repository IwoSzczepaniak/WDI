class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_link(first):
    while first is not False:
        print("->.", first.val, end = '')
        first = first.next

def make_link(tab):
    first = None
    n = len(tab)
    for i in range(n-1, -1, -1):
        tmp = Node(tab[i])
        tmp.next = first
        first = tmp
    return first

'''5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
należy połączyć w jedną listę odsyłaczową, która jest posortowana
niemalejąco według ostatniej cyfry pola val. '''

def przetworz(first):
    firsty = [None for i in range(10)]
    lasty = [None for i in range(10)]

    p = first
    while p is not None:
        ost = p.val % 10
        if firsty[ost] == None:
            firsty[ost] = p
            lasty[ost] = p
        else:
            lasty[ost].next = p
            lasty[ost] = lasty[ost].next
        p = p.next

    result = None
    for i in range(9, -1, -1):
        if firsty[i] is not None:
            lasty[i].next = result
            result = firsty[i]

    return result
