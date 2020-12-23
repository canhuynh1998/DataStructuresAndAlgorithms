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

    def search(self, target):
        '''
        Traverse through the list to find if the target value is in the list.
        '''
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False

    def insertFront(self, value):
        '''
        Insertion at the beginning of the list.
        '''
        if self.head is None:
            self.head = Node(value)
            self.length += 1
            return
        newHead = Node(value)
        newHead.next = self.head
        self.head = newHead
        self.length += 1
    
    def insertAfterANode(self, target, value):
        '''
        Insertion after the target Node.
        '''
        if self.head is None:
            self.insertFront(value)
            return
        if target is None:
            print("This is not a Node")
            return
        newNode = Node(value)
        newNode.next = target.next
        target.next = newNode
        self.length += 1

    def insertAtPosition(self, value, position):
        '''
        Insertion at the a specific position in the list
        
        By default, newNode will be add at the end of the list
        when the position is greater than the current length of the list and head is not None.

        If either head is None or position is 0, 
        we will insert to the front of the list when head is not None else do nothing.
        '''
        if position >= self.length and self.head is not None:
            self.insertBack(value)
            return
        
        if position == 0:
            if self.head is not None:
                self.insertFront(value)
            return
            
        current = self.head
        while position > 1:
            current = current.next
            connect = connect.next
            position -= 1
        insertNode = Node(value)
        insertNode.next = current.next if current.next is not None else None
        current.next = insertNode
        self.length += 1
    
    
    def insertBack(self, value):
        '''
        Insert at the end of the list
        '''
        if self.head is None:
            self.insertFront(value)
            return
        current = self.head
        while current.next is None:
            current = current.next
        
        newNode = Node(value)
        current.next = newNode
        self.length += 1