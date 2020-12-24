'''
Queue Implementation using Linked List
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self):
        self.head = None    # For dequeue
        self.tail = None    # For enqueue
        self.length = 0

    def isEmpty(self):
        '''
        Check if the queue is empty
        '''
        return self.length == 0
    
    def queueLength(self):
        '''
        Return the length of the queue
        '''
        return self.length 

    def enqueue(self, value):
        '''
        Insert at the end of the linked list
        '''
        newNode = Node(value)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.length += 1
    
    def dequeue(self):
        '''
        Remove at the beginning of the linked list
        '''
        if self.isEmpty():
            return None
        returnNode = self.head
        self.head = self.head.next

        # This will make sure we have an empty list if we remove the last node from the list
        if self.head is None:
            self.tail = None
        self.length -= 1
        return returnNode 
