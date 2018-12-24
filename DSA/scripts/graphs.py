from functools import reduce

class Node:
    """val  :: Int
       next :: Node """
    def __init__(self, val):
        self._val: int = val
        self.next = None
    
    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, node):
        self._next = node

    def hasNext(self) -> bool:
        return self.next != None
    
    def createNext(self, val: int):
        new = Node(val)
        self.next = new
        return new
    
    def createPrev(self, val: int):
        new = Node(val)
        new.next = self
        return new
    
    def __str__(self):
        s = "[" + str(self.val) + "]"
        if self.next == None:
            return s
        else:
            return s + "->" + str(self.next)
    
    def __len__(self):
        len = 1
        cur = self
        while cur.hasNext():
            len += 1
            cur = cur.next
        return len

class LinkedList:
    """ head :: Node """
    def __init__(self, head=None):
        self._head = head
        if head:    
            self.tail = head
        else:
            self.tail = None

    def add(self, node):
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    @property
    def head(self):
        return self._head
    
    @head.setter
    def head(self, node):
        self._head = node
    
    def __str__(self):
        return str(self.head)
    
    def __len__(self):
        return len(self.head)
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

def listToLinkedList(list: []) -> LinkedList:
    head = None
    prev = None
    for x in list:
        new = Node(x)
        if prev != None:
            prev.next = new
            prev = new
        else:
            prev = new
            head = new
    return LinkedList(head)

def testNodes():
    x = Node(3)
    assert x.val == 3
    assert len(x) == 1

    y = Node(4)
    y2 = Node(5)
    y.next = y2
    assert len(y) == 2

    l = listToLinkedList([1,2,3])
    assert l.head.val == 1
    assert l.head.next.val == 2
    assert l.head.next.next.val == 3
    assert len(l) == 3

    l2 = listToLinkedList([1])
    assert l2.head.val == 1

def test():
    testNodes()

test()

from queue import Queue
adj = []

# v1
adj.append(listToLinkedList([2, 4]))
# v2
adj.append(listToLinkedList([1, 3, 4]))
# v3
adj.append(listToLinkedList([2]))
# v4
adj.append(listToLinkedList([1, 2]))

for i in range(0, len(adj)):
    print("{}: {}".format(i + 1, adj[i]))

import time

bag = Queue(3)

# explore graph breadth-first
# uses a queue
def traverse(adj: [], start: int) -> None:
    dist = [-1] * len(adj)
    marked = [False] * len(adj)

    dist[start] = 0
    bag.put(start)

    while not bag.empty():
        cur = bag.get()
        if not marked[cur]:
            marked[cur] = True
            for x in adj[cur]:
                val = x.val
                bag.put(val)
                if dist[val] == -1:
                    dist[val] = dist[cur] + 1

    print(dist)

traverse(adj, 0)