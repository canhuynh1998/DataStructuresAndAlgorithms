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
        '''
        Insert at the beginning of the linked List
        '''
        newNode = Node(value)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def pop(self):
        '''
        Remove and retrieve the first node in the linked list
        '''
        if self.isEmpty():
            return None
        returnNode = self.head
        self.head = self.head.next 
        returnNode.next = None
        self.length -= 1
        return returnNode 
    
    def isEmpty(self):
        '''
        Check if the stack is empty
        '''
        return self.length == 0

    def peek(self):
        '''
        Retrieve the first node in the linked list but not removing it
        '''
        return self.head if not self.isEmpty() else None

    def stackLength(self):
        '''
        Return the length of the stack
        '''
        return self.length

    def search(self, value):
        '''
        Search for the position of the target value
        '''
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

