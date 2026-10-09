class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

# Usage
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Popped:", s.pop())       # Output: 3
print("Top element:", s.peek())  # Output: 2

