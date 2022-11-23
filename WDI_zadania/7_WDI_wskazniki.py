class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def repair(p):
    guardian = Node(None)
    prev = None
    start = p

    while p != None:
        if p.val % 2 == 0:
            new_p = p.next
            if prev == None:
                p.next = guardian.next
                guardian.next = p
            else:
                prev.next = p.next
                p.next = guardian.next
                guardian.next = p

            p = new_p

        else:
            prev = p
            p = p.next

    if prev == None:
        return guardian.next
    else:
        prev.next = guardian.next

    return start

