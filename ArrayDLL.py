#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 04:04:33 2021

@author: meljel
"""

# <constructor>(n): creates an array to represent a doubly-linked list that 
# holds a maximum of n items
# allocate(): returns the pointer to a free “node” or prints a descriptive 
# error statement and returns None if the list is full
# freeNode(index): indicates “node” with pointer index is free for future allocation
# insert(item): adds item to the list
# search(item): returns pointer to the first instance of item in the list; 
# prints a descriptive error statement and returns None if item cannot be found
# delete(item): removes the first instance of item in the list
# __str__(): returns a string showing all elements in the list starting with the head

class DLLArray():
    """Create a doubly linked list using an array."""
    def __init__(self, maxLength):
        """DLLArray(maxLength: int)"""
        self.maxLength = maxLength
        self.array = [None]*3*self.maxLength
        
    def getVal(self, index):
        """getVal(index: int) -> int
           Return value at the specified index."""
        return self.array[index]
    
    def setVal(self, index, value):
        """getVal(index: int)
           Sets value to specified value at the specified index."""
        self.array[index] = value
    
    def length(self):
        """length() -> int
           Return length of the array."""
        length = 0
        for i in range(self.maxLength):
            if self.getVal(i*3 + 1):
                length += 1
        return length
        
    def allocate(self, prev = False):
        """allocate() -> _ or None
           Returns a free “node” if possible; return None (with print) if not."""
       
        c, p = None, None
        
        # Iterate through list
        for i in range(self.maxLength):
            if self.getVal(3*i+1) == None:
                c = i
            elif self.getVal(3*i+2) == None:
                p = i
        
        # If p exists AND c is taken, it's good.
        if c != None and p != None:
            return [c,p]
            
        print("Your linked list is full; allocation failed.")
        return None

    
    def freeNode(self, index, prev = False):
        """freenode(index: int) -> bool
           Return the availability of a node."""
        # Not used.
        
        if prev:
            val = self.getVal(3*index)
            if val == None:
                return True
            else:
                return False
        
        else:
            val = self.getVal(3*index + 2)
            if val == None:
                return True
            else:
                return False
    
        # for i in range(self.maxLength):
        #     val = self.array[3*i+2]
            
        #     if val == None:
        #         return True
            
        #     elif val:
        #         return False
    
    def insert(self, item):
        """insert(item: int)
           Insert specified item at the end of the list."""
        
        # If starting node: manually set first node.
        if self.length() == 0:
            self.setVal(1, item)
        
        # If more than one node so far: proceed.
        else:
            
            # Allocate a slot.
            a = self.allocate()
            
            # Print an error message if list is full and item cannot be inserted.
            if a == None:
                print("Cannot insert item.")
                return
            
            newInd, prevInd = a[0], a[1]
            
            # Set new pointers.
            if newInd: 
                self.setVal(3*newInd+1, item)
                self.setVal(3*newInd, 3*prevInd+1)
                self.setVal(3*prevInd+2, 3*newInd+1)
        
    
    def search(self, item):
        """search(item: int) -> int
           Return the index of the first instance of the specified item."""
        
        # Iterate through list to find value that match specified item.
        for i in range(self.maxLength):
            if self.array[3*i+1] == item:
                return 3*i+1
            
        # Print an error message.
        print("The specified item value cannot be found!")
        return None
    
    def delete(self, item):
        """delete(item: int)
           Delete the first appearance of the specified item."""
        
        fp = None
        
        # Check if list is not empty.
        for i in range(self.maxLength):
            if self.array[3*i+1] == item:
                fp = i
                break
        
        # Proceed only if list is nonempty.
        if fp:
            
            # Set new pointers.
            prevInd = self.getVal(3*fp)
            nextInd = self.getVal(3*fp+2)
            
            # Edge cases.
            if prevInd:
                self.setVal(prevInd+1, nextInd)
            if nextInd:
                self.setVal(nextInd-1, prevInd)
        
            # Erase original pointers.
            for k in [3*fp, 3*fp+1, 3*fp+2]:
                self.setVal(k, None)
    
    def __str__(self):
        """__str__() -> str
           Return the string format of a DLLArray."""
        return str(self.array)
