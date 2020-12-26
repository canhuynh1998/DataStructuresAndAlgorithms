'''
Binary Search Tree Implementation
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
    
    def search(self, value):
        if self.root is None:
            return False
        if root.value == value:
            return True
        current = self.root
        while current is not None:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                return True
        return False
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current = self.head
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right
        return 

    def minValue(self):
        if self.head is None:
            return None
        current = self.head
        while current.left is not None:
            current = current.left
        return current.value

    def maxValue(self):
        if self.head is None:
            return None
        current = self.head
        while current.right is not None:
            current = current.right 
        return current.value


