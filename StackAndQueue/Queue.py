'''
Queue Implementation using Linked List
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return None
        returnNode = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return returnNode 
