# Melody Jing
# Maximum subarray problem solved with three methods: fully recursively, brute 
# force, and a hybrid approach. Includes a mechansism to time the execution of 
# each implementation.

import math
import random
import time

# Input a list (L) and the low (inclusive) and high (not inclusive) indices for the 
# array that you want to find the maximum subarray
# Output will be the left and right indices of the max subarray and the sum
def maxSubarray(L,low,high):
    """
    Fully recursive maximum subarray.

    Parameters
    ----------
        L : List(int)
            list for which we want to find the max subarray
        low : int
            index of the left bound (inclusive) in L
        high : int
            index of the right bound (exclusive) in L

    Returns:
        low : int
            index of the left bound (inclusive) of the max subarray of L
        high : int
            index of the right bound (exclusive) of the max subarray of L
        sum : int
            sum of the max subarray of L
    """
    # if there's only one item in the subarray then the max is it
    if low+1 == high: return low,high,L[low]

    # otherwise, divide the list in half and look for the max subarray in each side
    mid = (low + high) // 2
    leftLow,leftHigh,leftSum = maxSubarray(L,low,mid)
    rightLow,rightHigh,rightSum = maxSubarray(L,mid,high)

    # check for a max subarray that crosses the midpoint
    crossLow,crossHigh,crossSum = maxCrossingSubarray(L,low,mid,high)

    # compare the 3 sums and return the data for the max
    if leftSum >= rightSum:
        if leftSum >= crossSum: return leftLow,leftHigh,leftSum
    elif rightSum >= crossSum: return rightLow,rightHigh,rightSum
    return crossLow,crossHigh,crossSum


def maxCrossingSubarray(L,low,mid,high):
    # Collaborated with: Collaborator 1, Collaborator 2
    """
    Helper for recursive max subarray.
    """
    maxSum, maxLow, maxHigh = -math.inf, 0, 1 # L[mid-1] + L[mid] # 
    
    # Iterate through all subarray ranges
    for i in range(low,mid+1):
        for j in range(mid+1,high):
            currentSum = sum(L[i:j])
            # Compare sums, keep the maximum
            if currentSum >= maxSum:
                maxLow, maxHigh, maxSum = i, j, currentSum
        
    return maxLow, maxHigh, maxSum


def maxSubarrayBF(L):
    """
    Brute force max subarray implementation.
    """
    # Initialize values to the first element of the list
    maxLow, maxHigh, maxSum = 0, 1, -math.inf
    
    # Iterate through all subarray ranges
    for i in range(len(L)):
        for j in range(i+1, len(L)+1): 
            currentSum = sum(L[i:j])
            # Compare sums, keep the maximum
            if currentSum >= maxSum:
                maxLow, maxHigh, maxSum = i, j, currentSum
    
    return maxLow, maxHigh, maxSum


def findDCCrossover():
    # Initialize n as the length of the list.
    n = 3
    
    # Run testcases number of trials of each method
    testcases = 5000

    print("n\tbf\tdc")    

    while True:
        # Reset each algorithm's total runtime to 0
        dtBF, dtDC = 0,0
        
        # Iterate through all testcases number of trials
        for i in range(testcases):
            
            # Create a list of length n
            L = makeList(n)
            
            # Run both algorithms on the list, recording the time it takes
            dtBF += timeBF(L)
            dtDC += timeDC(L)
        
        # Take the average time per run by dividing total time by number of cases
        avgBF, avgDC = dtBF/testcases, dtDC/testcases
        print(str(n)+"\t"+str(avgBF)+"\t"+str(avgDC))
        
        # Determine point when divide + conquer is more efficient than brute force
        if avgDC < avgBF:
            print("DC is faster than BF when n =", n)
            break
        
        # If DC is still slower, increase n and try again
        n += 1


def maxSubarrayMod(L,low,high):
    """
    Divide and conquer method for solving max subarray that is same as above except 
    the base case uses the brute-force strategy when the array is small enough
    """
    # Do brute force if length is below the crossover point
    if len(L) <= 10:
        maxLow, maxHigh, maxSum = maxSubarrayBF(L)
        return maxLow, maxHigh, maxSum

    # otherwise, divide the list in half and look for the max subarray in each side
    mid = (low + high) // 2
    leftLow,leftHigh,leftSum = maxSubarray(L,low,mid)
    rightLow,rightHigh,rightSum = maxSubarray(L,mid,high)

    # check for a max subarray that crosses the midpoint
    crossLow,crossHigh,crossSum = maxCrossingSubarray(L,low,mid,high)

    # compare the 3 sums and return the data for the max
    if leftSum >= rightSum:
        if leftSum >= crossSum: return leftLow,leftHigh,leftSum
    elif rightSum >= crossSum: return rightLow,rightHigh,rightSum
    return crossLow,crossHigh,crossSum


def findDCMCrossover():
    """
    Time each method (brute force, divide & conquer, d&c modified) using the 
    time module and print the results.

    Inputs: None
    Outputs: None
    """
    testcases = 5000
    count = 0
    print("n\tBF\tDC\tDCM")
    for n in range(3,20):
        dtBF, dtDC, dtDCM = 0,0,0
        for i in range(testcases):
            L = makeList(n)
            dtBF += timeBF(L)
            dtDC += timeDC(L)
            dtDCM += timeDCM(L)
        avgBF, avgDC, avgDCM = dtBF/testcases, dtDC/testcases, dtDCM/testcases
        print(str(n)+"\t"+str(avgBF)+"\t"+str(avgDC)+"\t"+str(avgDCM))


# returns a list of length n that contains integers in the range -20 to 20
def makeList(n):
    L = []
    for i in range(n):
        L.append(random.randint(-20,20))
    return L

# returns the time it takes the brute-force method to find the max subarray of L 
def timeBF(L):
    start = time.time()
    maxSubarrayBF(L)
    end = time.time()
    return end-start

# returns the time it takes the divide and conquer method to find the max 
# subarray of L
def timeDC(L):
    start = time.time()
    maxSubarray(L,0,len(L))
    end = time.time()
    return end-start

# returns the time it takes the modified divide and conquer method to find the
# max subarray of L
def timeDCM(L):
    start = time.time()
    maxSubarrayMod(L,0,len(L))
    end = time.time()
    return end-start

# Example: get the maximum subarray of some small-integer list of length 30
# and test for time over length
if __name__ == "__main__":
    L = makeList(30)
    print("Original list:   ", L)
    low, high, total = maxSubarray(L, 0, len(L))
    print("Maximum subarray:", L[low:high])
    print("Sum:             ", total)
    findDCMCrossover()