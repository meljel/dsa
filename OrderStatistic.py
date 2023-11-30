# Melody Jing
# Using the structure of quicksort, statistic() finds and returns the 
# jth smallest element of an input array. 


def statistic(A, j, p=0, r=-1):
    """Input a list and an int; returns the jth smallest value within the
       input array A. p and r are integer indices and optional parameters
       that make the recursion work."""
       
    # Reset rightbound to length - 1, instead of just -1 so that the
    # comparisons can be done correctly
    if r == -1: r = len(A)-1
    
    # Check if k is within bounds of the length of the list
    # Otherwise the function returns None
    if j in range(0,len(A)+1):

        # Get pivot and reorganize array
        q = partition(A,p,r)
        
        # Check pivot
        if q-p == j-1: return A[q]
        
        # Recurse left
        elif q-p > j-1: return statistic(A, j, p, q-1)
        
        # Recurse right
        return statistic(A, j-q+p-1, q+1, r)


# Application: partitioning an array
def partition(A, p, r):
    """Input a list, left bound, and right bound. Decides pivot; moves items
    less than pivot to its left and items greater than pivot to its right. 
    Used for things like quicksort."""
    
    x, i = A[r], p
    for j in range(p, r):
        # Directly compare elements
        if A[j] <= x:
            # Swap if on the wrong side of pivot; increment to the right by 1
            A[i], A[j] = A[j], A[i]
            i += 1 

    # Put pivot into correct place
    A[i], A[r] = A[r], A[i]
    return i

# Preset output: "sort" using kth order statistic
if __name__ == "__main__":
    
    # Randomized list creation function
    import random 
    def makeList(n):
        return [random.randint(-20,20) for i in range(n)]

    # Creating the lists
    A = makeList(10)
    print("initial:", A)
    
    # Printing what is essentially an inefficiently-sorted final list
    print("sorted: ", [statistic(A,j) for j in range(1,len(A)+1)])