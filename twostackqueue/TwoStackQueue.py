#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 09:19:36 2021

@author: meljel
"""

# <constructor>(n): initializes two stacks so the maximum length of the queue is n
# length(): returns the length of the queue
# enqueue(item): adds item to the (tail of the) queue or prints a descriptive error statement if it cannot
# dequeue(): returns the first item in the queue; it should return None if the queue is empty

import TwoStacks as ts

class Queue():
    """Queue
       Create TwoStacks object that acts as a queue, rather than stacks."""
    
    def __init__(self, n, lunchLine = False):
        """Queue(n: int, lunchLine: bool)
           Create a TwoStacks instance of maximum length n."""
        self.stacks = ts.TwoStacks(n)
        
        # lunchLine is a boolean that determines whether to include methods 
        # applicable only to a lunchLine situation. 
        self.lunch = lunchLine
    
    def getList(self):
        """getList() -> list
           Return the array from TwoStacks."""
        return self.stacks.getStacks()
    
    def length(self):
        """length() -> int
           Return the combined length of both stacks."""
        return self.stacks.height(1) + self.stacks.height(2)
    
    def enqueue(self, item):
        """enqueue(item: int or str)
           Add specified item to queue."""
        self.stacks.push(1, item)
            
    def dequeue(self):
        """dequeue() -> int or str
           Remove the item at the end of the queue. Return item. """
           
        # Check if second stack is empty. If so, move all items to second stack
        # prior to popping.
        if self.stacks.height(2) == 0:
            for i in range(self.stacks.height(1)):
                self.stacks.push(2, self.stacks.pop(1))
        
        return self.stacks.pop(2)
    
    def timePass(self, time):
        """timePass(item: int or str) -> int
           Proceed by reducing patience of each customer by specified time.
           Return the number of customers lost."""
        # Require that the class is called to be used in a lunch line.
        if self.lunch:
            becomeZero = 0
            it = 0
            
            # Iterate through every element of the queue.
            for item in self.getList():
                # print(self.getList())
                
                # Check if each item is True; don't change anything if False
                if item: # != None and item != 0:
                    # Since the method only executes when it is a lunchLine, 
                    # item type is assumed to be a float or int.
                    item = int(item)
                    item -= time
                    
                    # Directly set the value of the item to be decreased.
                    self.getList()[it] = item
                    
                    # Count the number of items that become zero. Corresponds
                    # with the number of customers who have left during that turn.
                    if item <= 0:
                        becomeZero += 1
                        
                it += 1

            return becomeZero

# Testing
# q = Queue(5)
# q.enqueue(6)
# q.enqueue(1)
# q.enqueue(2)
# q.stacks.__str__()
# print(q.length())
# q.dequeue()
# q.enqueue(7)
# q.enqueue(2178367)
# q.enqueue(2178368)
# q.stacks.__str__()
# print(q.length())
# q.dequeue()
# print(q.length())
# q.stacks.__str__()
# q.enqueue(532784626384732)
# print(q.length())
