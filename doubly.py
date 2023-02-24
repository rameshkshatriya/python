from typing_extensions import Self


class node:
    __slots__ = 'element','next','prev'
    def __init__ (self, element, next, prev):
        self.element = element
        self.next = next
        self.prev = prev

class doublylinkedlist:
    def __init__(self):
        self.head = None
        Self.tail = None
        self.size = 0

    def __len__ (self):
        return self.size

    def isempty(self):
        return self.size == 0

    def add_last(self, n):
        Newest = node(n, None, None)
        if self.isempty():
            self.head = Newest
            self.tail = Newest
        else:
            self.tail.next = Newest
            Newest.prev = self.tail
            self.tail = Newest
        self.size +=1

    def display(self):
        p = self.head
        while p :
            print(p.element, end="-->")
            p = p.next
        print()

    def displayprev(self):
        p = self.tail
        while p :
            print(p.element, end="<--")
            p = p.prev
        print()

l = doublylinkedlist()
l.add_last(10)
l.add_last(20)
l.add_last(30)
l.add_last(40)
l.display()
l.displayprev()
 