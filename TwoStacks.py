#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:48:18 2021

@author: meljel
"""

# <constructor>(n): initializes array of length n to store stack #1 and stack #2
# height(stackNum): returns the height of stack #stackNum 
# push(stackNum,item): adds item to the top of stack #stackNum or prints
# descriptive error statement if it cannot
# pop(stackNum): returns the top item from stack #stackNum; 
# it should return None if the stack is empty
# __str__(): returns a string showing all elements in the array
    
class TwoStacks():
    """TwoStacks
       Create two stacks contained in a list with a predetermined max length."""
    
    def __init__(self, maxLength):
        """TwoStacks(maxLength: int) \n
           Initialize an array of max length n that stores two stacks, 1 and 2."""
        self.maxLength = maxLength
        
        # Initialize array containing only None of length maxLength.
        self.stackArray = [None]*self.maxLength
        
        # Initialize length of each stack to 0.
        self.stack1len = 0
        self.stack2len = 0
       
    # Accessor methods
    
    def getMaxLen(self):
        """getMaxLen() -> int \n
           Return the maximum length of the array."""
        return self.maxLength

    def getStacks(self):
        """getStacks() -> list \n
           Return the array containing both stacks."""
        return self.stackArray
    
    # Required methods
    
    def height(self, stackNum):
        """height(stackNum: int) -> int \n
           Return the size of the stack denoted by stackNum."""
        # print(stackNum)
        
        # Decide which stack length to return. 
        if stackNum == 1:
            return self.stack1len
        elif stackNum == 2:
            return self.stack2len
        
        # Print error message if stack number is invalid.
        else:
            print("Please enter only 1 or 2 to denote the desired stack.")
    
    def push(self, stackNum, item):
        """push(stackNum: int, item: int or str) \n
           Add item to top of the stack denoted by stackNum."""
        # try:
        v = (self.stack1len + self.stack2len < self.maxLength)
        # except NameError:
        #     return print("Please enter a string or a number.")
        
        # Proceed only if maxLength has not been exceeded.
        if v:
            if stackNum == 1:
                # Add item to stack 1.
                self.stackArray[self.stack1len] = item
                self.stack1len += 1
                
            elif stackNum == 2:
                # Add item to stack 2.
                self.stackArray[-1 - self.stack2len] = item
                self.stack2len += 1
                
            else:
                # Prints error message if stack number is invalid.
                print("Invalid stack name.")
        else:
            # Prints error message if array is full; does not push item. 
            print("Your TwoStacks is full and unable to push", str(item)+".")
    
    def pop(self, stackNum):
        """pop(stackNum: int) -> int or str
           Remove item at top of the stack denoted by stackNum. Return the item."""
        if stackNum == 1:
            
            if self.height(1):
            
                # Pop item at the top of stack 2 if its size is nonzero.
                popped = self.stackArray[self.stack1len-1]
                self.stackArray[self.stack1len-1] = None
                self.stack1len -= 1
                
                # Returns popped item. 
                return popped
            else:
                # Return None if there are no items in stack 1.
                return None

        elif stackNum == 2:
            
            if self.height(2):
                
            # Pop item at the top of stack 2 if its size is nonzero.
                popped = self.stackArray[-self.stack2len]
                self.stackArray[-self.stack2len] = None
                self.stack2len -= 1
                # Returns popped item. 
                return popped
            else:
                # Return None if there are no items in stack 2. 
                return None
        else:
            # Print error message if invalid input for stack number. 
            print("Please enter only 1 or 2 as the parameter for height.")
    
    def __str__(self):
        """__str__() -> str
           Return a string representation of the array containing both stacks."""
        return str(self.stackArray)

# ts = TwoStacks(7)
# ts.push(1, "h")
# ts.push(2, "i")
# ts.push(1, "j")
# ts.push(1, "eiufyiuweyf")
# ts.__str__()
# ts.pop(2)
# ts.__str__()
# ts.push(1, "324897")
# ts.push(1, 234)
# ts.push(1, 1)
# ts.push(1, 0)
# ts.__str__()
