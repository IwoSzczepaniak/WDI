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

def rev_link(first):
    if first is None or first.next is None:
        return first
    p = None
    q = first
    r = q.next
    while r is not None:
        q.next = p
        p = q
        q = r
        r = r.next
    q.next = p
    return q
