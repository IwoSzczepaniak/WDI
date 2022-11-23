class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_link(first):
    while first is not False:
        print("->." first.val, end = '')
        first = first.next

def make_link(tab):
    first = None
    n = len(tab)
    for i in range(n-1, -1, -1):
        tmp = Node(tab[i])
        tmp.next = first
        first = tmp
    return first


