class Node:
    def __init__(self):
        self.val = None
        self.next = None

def member(z, el):
    p = z
    while p != None:
        if p.val == el:
            return True
        p = p.next
    return False
