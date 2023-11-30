# Melody Jing
# Implements a min priority queue using an array. All methods adopted from the
# CLRS textbook; uses a min priority queue to store the max k items in an array.

import math

class MinPriorityQueue():
    def __init__(self, A):
        self.array = A
        for i in range(self.size()//2, -1, -1):  # Loop back from last nonleaf
            self.minHeapify(i)  # Min heapify each node

    def minHeapify(self, i: int):
        l, r = 2*i+1, 2*i+2
        if l < self.size() and self.array[l] < self.array[i]:
            smallest = l  # Define smallest as left child
        else:
            smallest = i  # Smallest is parent
        if r < self.size() and self.array[r] < self.array[smallest]:
            smallest = r  # Define smallest as right child
        if smallest != i:  # Swap parent with child if child is smallest
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
            self.minHeapify(smallest)  # Minheapify smallest child

    def size(self):
        return len(self.array)  # Return length of array

    def getMin(self):
        return self.array[0]  # Return root

    def extractMin(self):
        if self.size() < 1:  # Heap is degenerate
            print("Heap underflow")
            return
        minValue = self.array[0]  # Set minimum to root
        self.array[0] = self.array.pop(-1)  # Set root to last leaf
        self.minHeapify(0)  # Minheapify entire tree
        return minValue

    def insert(self, x: float):
        self.array.append(-math.inf)  # Set new node to -inf
        self._heapDecreaseKey(self.size()-1, x)  # Insert new key
    
    def _heapDecreaseKey(self, i: int, key: float):
        if key < self.array[i]:  # Check if new key is greater than the parent
            print("New key is smaller than current key")
            return
        self.array[i] = key  # Set index to new key
        while i > 0 and self.array[(i-1)//2] > self.array[i]:  # Swap if less
            self.array[i], self.array[(i-1)//2] = self.array[(i-1)//2], self.array[i]
            i = (i-1)//2  # New i is parent

    def getArray(self):
        return self.array


def storeMax(N: list, k: int): 
    """Store the k largest objects in an array using a Min Heap."""
    Q = MinPriorityQueue([])  # Initialize Min Heap
    for newVal in N:  # Loop through each item in the list
        if Q.size() < k:  # For first k values, insert regardless of value
            Q.insert(newVal)
        elif newVal > Q.getMin():  # After first k values, compare to min in Q
            Q.insert(newVal)  # If newVal is greater, exchange it with the min
            minVal = Q.extractMin()
    return Q.getArray()

# Testing
# A = [4,1,3,2,16,9,10,14,8,7]
# Q = MinPriorityQueue(A)
# print(storeMax(A,5))
