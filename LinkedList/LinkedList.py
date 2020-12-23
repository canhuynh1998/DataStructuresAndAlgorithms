'''
Singly Linked List Implementation
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def insertFront(self, value):
        if self.head is None:
            self.head = Node(value)
            self.length += 1
            return
        newHead = Node(value)
        newHead.next = self.head
        self.head = newHead
        self.length += 1
    
    def insertAfterANode(self, target, value):
        if self.head is None:
            self.insertFront(value)
            return
        if target is None:
            print("This is not a Node")
            return
        newNode = Node(value)
        newNode.next = target.next
        target.next = newNode

    def insertBetween(self, value, position):
        if position >= self.length and self.head is not None:
            self.insertBack(value)
            return
        if position == 0 or self.head is None:
            self.insertFront(value)
            return
        current = self.head
        connect = self.head
        while position > 1:
            current = current.next
            connect = connect.next
            position -= 1
        insertNode = Node(value)
        insertNode.next = current.next
        current.next = insertNode
    
    def insertBack(self, value):
        if self.head is None:
            self.insertFront(value)
            return
        current = self.head
        while current.next is None:
            current = current.next
        
        newNode = Node(value)
        current.next = newNode