# Queue FIFO data structure https://www.geeksforgeeks.org/queue-in-python/

# Could implement with list but slow in python since pop left is O(n), need to shift entire list

# In python can use deque from collections - Fast

from collections import deque

# Or Queue from queue

from queue import Queue

# But ourselves, we'd use linked list

class Linked_List:
    pass

class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None