class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from an empty stack.")
        popped_val = self.top.value
        self.top = self.top.next
        return popped_val

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.top.value


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: Cannot dequeue from an empty queue.")
        dequeued_val = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None  # Reset rear anchor if queue becomes empty[cite: 12, 14]
        return dequeued_val

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.front.value
