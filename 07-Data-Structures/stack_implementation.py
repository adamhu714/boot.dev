# Stack LIFO list, easy implementation with list in python
# O(1) push, pop, peak, length

class Stack:
    
    def __init__(self) -> None:
        self.values = []

    def push(self, value) -> None:
        self.values.append(value)

    def pop(self):
        if len(self.values) == 0:
            return None
        return self.values.pop()
    
    def peek(self):
        if len(self.values) == 0:
            return None
        return self.values[-1]
    
    def size(self):
        return len(self.values)