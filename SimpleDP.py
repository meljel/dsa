# Melody Jing
# Both functions below are implemented using dynamic programming; each has
# an accompanying grid (or explanation) in the document.

def findDP(n):
    """Returns the nth Fibonacci number using dynamic programming instead of
       recursion. n is a whole number."""
    # Create empty list of 1s, which are F(0) and F(1)
    fib = [1 for i in range(n+1)]
    # Iterate through the array to derive each F(n) from
    # summing the previous two values
    for j in range(2, n+1):
        fib[j] = fib[j-1] + fib[j-2]
    return fib[n]


def exactChange(target, coins):
    """Returns whether target is reached by the coin values in coins (bool).
       Based on the recursive function in the doc, assumes that the array coins
       is in nondecreasing order (and sorts it in the function).
       Allows for duplicates in coins."""
    # Sort coins from least to greatest
    coins = sorted(coins)
    # Create grid with dimensions target and length of coins; all values False
    grid = [[False for i in range(target)] for j in range(len(coins))]

    # Iterate left-right up-down through the grid
    for c in range(len(coins)):
        for t in range(target):
            # Case 1: intermediate value achieved by the current coin
            if coins[c] == t+1:
                grid[c][t] = True
            # Case 2: intermediate value achieved by a previous coin
            elif grid[c-1][t]:
                grid[c][t] = True
            # Case 3: intermediate value achieved by adding current coin to
            # a previous successful configuration
            elif t-coins[c] >= 0 and grid[c-1][t-coins[c]]:
                grid[c][t] = True

    # Return last value of grid (final value and considering all coins)
    return grid[-1][-1]