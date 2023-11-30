# Melody Jing
# A simple binary search.

def binarySearch(L, low, high, target):
    # Base case    
    if high == low + 1:
        if L[low] == target: return low
        else: return -1

    mid = (high+low) // 2

    # Element smaller than mid; search only within left section
    if target < L[mid]:
        return binarySearch(L, low, mid, target)

    # Element larger/equal to than mid; search only within right section
    else:
        return binarySearch(L, mid, high, target)

# Testing
# l = [-2,3,54,298,9218]
# print(binarySearch(l, 0, len(l), 9218))