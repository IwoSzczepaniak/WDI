class Node:
    def __init__(self):
        self.val = None
        self.next = None

    g = Node(None)
    start = p
    prev = None

    while p != None:
        if p.val % 2 == 0:

            start = p.next
            new_p = p.next

            if prev == None:
                p.next = g.next
                g.next = p
            else:
                prev.next = p.next
                p.next = g.next
                g.next = p

            p = new_p
        else:
            prev = p
            p = p.next

    if prev != None:
        prev.next = g.next
        return start
    return g.next
