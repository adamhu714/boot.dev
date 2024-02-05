# Queue FIFO data structure https://www.geeksforgeeks.org/queue-in-python/

# Could implement with list but slow in python since pop left is O(n), need to shift entire list

# In python can use deque from collections - Fast

from collections import deque

# Or Queue from queue

from queue import Queue

# But ourselves, we'd use linked list

class Linked_List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node != None:
            yield node
            node = node.next
    
    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)

    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.val
    
    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        # I think this works if the nodes are passed by reference. Pointers in c++ made more sense to me.
        self.tail.next = node
        self.tail = node

class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.next = None

    def add_next(self, node):
        self.next = node

    def __repr__(self) -> str:
        return self.val