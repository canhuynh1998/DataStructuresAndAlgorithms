'''
Stack Implementation using Linked List
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.length += 1

    def pop(self):
        returnNode = self.head
        self.head = self.head.next 
        self.length -= 1
        return returnNode if returnNode else None
    
    def isEmpty(self):
        return self.length == 0

    def peek(self):
        print(self.head.value)

    def search(self, value):
        if isEmpty:
            return -1
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            index += 1
            current = current.next
        return -1

