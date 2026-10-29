class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: Cannot push to a full stack.")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from an empty stack.")
        value = self.data[self.top]
        self.data[self.top] = None  # Clear reference for garbage collection
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.data[self.top]


class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = -1
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def is_full(self):
        return self.item_count == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: Cannot enqueue to a full queue.")
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = value
        self.item_count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: Cannot dequeue from an empty queue.")
        value = self.data[self.front]
        self.data[self.front] = None  # Clear reference
        self.front = (self.front + 1) % self.capacity
        self.item_count -= 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.data[self.front]
