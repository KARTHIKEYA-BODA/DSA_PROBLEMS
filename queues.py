from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return "Queue is empty"

    def peek(self):
        return self.items[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

# Usage
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
print("Dequeued:", q.dequeue())    # Output: A
print("Front element:", q.peek())  # Output: B

