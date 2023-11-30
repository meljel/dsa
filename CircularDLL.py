#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 00:47:19 2021

@author: meljel
"""

# <constructor>(): initialize the circular doubly linked list
# getFirst(): returns a pointer to the head of the list
# insert(item): adds item to the list
# search(item): returns pointer to the first instance of item in the list; 
# prints a descriptive error statement and returns None if item cannot be found
# delete(item): removes the first instance of item in the list
# __str__(): returns a string with the elements of the list in order from head to tail

class CDLLNode():
    """Create a node for the circular doubly linked list."""
    def __init__(self, value):
        """CDLLNode(value: int or str)"""
        self.value = value
        self.prev = None
        self.next = None
    
    def getValue(self):
        """getValue() -> int or str
           Return value of the node."""
        return self.value
    
    def getPrev(self):
        """getPrev() -> int or str
           Return previous node."""
        return self.prev
    
    def getNext(self):
        """getNext() -> int or str
           Return next node."""
        return self.next
    
    def setPrev(self, newPrev):
        """setPrev(newPrev: CDLLNode)
           Sets previous node as specified node."""
        self.prev = newPrev
        
    def setNext(self, newNext):
        """setPrev(newPrev: CDLLNode)
           Sets next node as specified node."""
        self.next = newNext
    

class CDLL():
    """Create a circly doubly linked list."""
    def __init__(self):
        self.head = None
        
    def getFirst(self):
        """getFirst() -> CDLLNode
           Return first element of the list."""
        return self.head
    
    def insert(self, value):
        """insert(value: int or str)
           Insert a node of specified value at the end of the list."""
        newNode = CDLLNode(value)
        
        # Case 1: First item
        if self.head == None:
            # print("1stcase")
            self.head = newNode
        
        # Case 2: Second item
        elif self.head.next == None and self.head.prev == None:
            # print("2ndcase")
            self.head.setNext(newNode)
            self.head.setPrev(newNode)

            newNode.setPrev(self.head)
            newNode.setNext(self.head)
        
        # Case 3: All other items
        else:
            # print("3rdcase")
            newNode.setNext(self.head)
            newNode.setPrev(self.head.prev)

            self.head.prev.setNext(newNode)
            self.head.setPrev(newNode)
    
    def search(self, value):
        """search(value: int or str) -> CDLLNode
           Return the node if it exists. Return None if it doesn't."""
        
        # Determine if head of list matches specified value.
        k = self.head
        if k.value == value:
            return k
        
        # Iterate through rest of list.
        k = self.head.next
        while k is not self.head:
            if k.value == value:
                return k
            k = k.next
        
        # Print an error message if element of specified value is not found.
        print("\n[Error] No node with value", str(value), "found in given CDLL.")
        return None
    
    def delete(self, value):
        """delete(value: int or str)
           Delete the first node of the specified value."""
           
        # Search for item to delete.
        delNode = self.search(value)
        
        # Print an error message if specified item cannot be found.
        if delNode == None:
            print("\n[Error] Cannot delete a node that cannot be found.\n")
            return
        
        # Redefine previous and next nodes. 
        delNode.prev.next = delNode.next
        delNode.next.prev = delNode.prev
    
    def __singlestr__(self, node):
        """__singlestr__(node: CDLLNode) -> str
           Return the string format of the contents of a node."""
        return "Single string return: [prev, value, next] = "+ \
            str([node.prev.getValue(), node.getValue(), node.next.getValue()])
    
    def __str__(self):
        """__str__() -> str
           Return the string format of a CDLL."""
        node = self.head
        listToPrint = [self.head.getValue()]
        # i=0
        
        # Don't print if no head.
        if self.head == None:
            return
        
        # Print 1 item.
        elif self.head.next == None:
            return listToPrint
        
        # Iterate through list; print after.
        node = node.next
        while node is not self.head:
            # print("value:",str(node.value)+"; \
            #       pointers: ("+str(node.prev.value)+","+str(node.next.value)+")")
            listToPrint.append(node.getValue())
            node = node.next
            # i+=1
            # print(i)
            
        return listToPrint
    
