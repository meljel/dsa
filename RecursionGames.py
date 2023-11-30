# Melody Jing
# 

def palindrome(word):
    """palindrome(word: str) -> bool
       Returns a boolean telling whether input string is a palindrome.
       Is not case sensitive. Does not care about spaces."""
    word = word.lower().strip()
    
    # Base case: if given a single character, it is a palindrome.
    if len(word) == 1 or len(word) == 0:
        return True

    # Recursive step: match first and last characters of the string.
    elif word[0] == word[-1]:
        newWord = palindrome(word[1:-1])
        return newWord
    
    # If they don't match, it isn't a palindrome.
    else:
        return False


def digitsToWords(n):
    """digitsToWords(n: int) -> str
       Returns a string translation of a positive integer input."""
    
    # Dictionary that has digit indices to string definitions
    digitWordDict = {0:"zero ", 1:"one ", 2:"two ", 3:"three ", 4:"four ",
                     5:"five ", 6:"six ", 7:"seven ", 8:"eight ", 9:"nine "}
    
    # Base case: single digit number
    if n < 10:
       return str(digitWordDict[n])
   
    # Recursive step: dividing by 10, remainder, and recursing
    else:
        newN = n // 10
        rem = n - 10*newN
        # print("newN, rem =", str(newN), str(rem))
        return (digitsToWords(newN) + str(digitWordDict[rem]))


def sumToTarget(nums, x):
    """sumToTarget(nums: list of ints, x: int) -> bool
       Returns a bool on whether x is the sum of a subset of nums."""
       
    # Base case: Compare the single-element list
    if len(nums) == 1:
        return nums[0] == x
    
    # Pop the first element
    first = nums.pop(0)
    
    # With the rest of the elements, try summing with and without the first element
    leftBool, rightBool = sumToTarget(nums, x), sumToTarget(nums, x-first)
    return leftBool or rightBool
    

def choose(n, k):
    """choose(n: int, k: int) -> int
       Returns n choose k."""
    
    # Base case: if the result is 1, return 1
    if k == 0 or k == n:
        return 1
    
    # Recursive step: using the given formula, recurse by adding
    else:
        return choose(n-1,k-1) + choose(n-1,k)


def playPalindrome():
    # Get initial input
    pal = input("Enter a word: ")            
    
    # Print success message
    if palindrome(pal):
        print("\n'"+pal+"' is a palindrome.")
        
    # Print failure message
    else: 
        print("\n'"+pal+"' is not a palindrome.")


def playDigitsToWords():
    # Get initial input, set valid to False
    dtw = input("Enter a positive integer: ")
    valid = False

    # Input validation while loop
    while not valid:
        valid = True
        
        # Check if each character is a digit
        for ch in dtw:
            if ord(ch) not in range(48,59):
                valid = False
        
        # Print error message; get next input
        if valid == False:
            print("\nPlease enter a positive integer only.")
            dtw = input("Enter a positive integer: ")
    
    dtw = int(dtw)
    
    # Print execution message
    print("\n"+str(dtw), "can be read as:", digitsToWords(dtw))


def playSumToTarget():
    # Get initial input, set valid to False
    stt = input("Enter a list of numbers and a positive integer (ex: [1,2,3],5): ")
    valid = False
    
    # Input validation while loop, initialize some variables
    while not valid:
        valid = True
        sttList = []
        current = ""
        x = ""
        
        # Loop backwards by character to find positive x; 
        # Stops with ','; invalid with '-'
        for ch in stt[-1:1:-1]:
            
            # Invalidate negative sign
            if ord(ch) == 45:
                valid = False
                break
            
            # Stop when comma
            elif ord(ch) == 44:
                x = int(x)
                break
            
            # Append digit
            elif ord(ch) in range(48,59):
                x = ch + x
        
        # Loop fowards and put items into list until ']'
        for ch in stt:
            
            # Stop when right bracket
            if ord(ch) == 93:
                sttList.append(int(current))
                break
            
            # Change number when comma
            elif ord(ch) == 44:
                sttList.append(int(current))
                current = ""
            
            # Valid digit or negative sign
            elif ord(ch) in range(48,59) or ord(ch) == 45:
                current += ch
            
            # No action on space or left bracket
            elif ord(ch) not in [32, 91]:
                valid = False
        
        # Print error message and get next input
        if not valid:
            print("\nPlease enter the inputs in the correct format, with a\
positive x.")
            stt = input("\nEnter a list of numbers and a positive integer (ex:\
[1,2,3],5): ")
    
    s = " NOT"
    if sumToTarget(sttList, x):
        s = ""
    print("The sum", x, "can"+s, "be formed from elements of", str(sttList)+".")


def playChoose():
    # Get initial input
    chs = input("Enter total and number to choose (separated by comma): ")
    valid = False
    ineq = True
    
    # Input validation while loop; assume valid to be True
    while not valid:
        valid = True
        
        # Initialize some variables
        chs = chs.strip()
        n,k = "",""
        isK = False
        
        # Check each character
        for ch in chs:
            
            # Check if it is comma or 
            if ord(ch) in [44,93]:
                isK = True
            
            # Increment either n or k by 1, based on comma position
            elif ord(ch) in range(48, 59):
                if isK:
                    k += ch
                else:
                    n += ch
            
            # Invalid if any non-numerical character is detected
            else:
                valid = False
        
        # Check if inequality is satisfied
        if valid:
            if int(n) < int(k):
                ineq = False
                valid = False
        
        # Prints and errors
        if not valid:
            
            # Print error messages for inequality clause
            if not ineq:
                print("\nMake sure the first number is larger than the second.")
            
            # Print error message for nonnegative integers
            else:
                print("\nPlease enter nonnegative integers separated by a comma only.")
            
            # Get next input
            chs = input("Enter total and number to choose (separated by comma): ")
    
    print(n, "choose", k, "is", str(choose(int(n),int(k)))+".")


def main():
    """main() -> None
       Executes main game."""
       
    print("Welcome to the Recursion Calculator!")
    
    # Main while loop - option selection and quitting
    while True:
        print("\nChoose a function:\n\
    1) Palindrome\n\
    2) digitsToWords\n\
    3) sumToTarget\n\
    4) choose\n\
    9) Quit")
        
        # Get initial input
        opt = input("Option: ")
        
        # If not in the valid list, print error message
        if opt not in ["1","2","3","4","9"]:
            print("Please enter a valid option!")
        
        # Break from while loop; go to end of function main()
        if opt == "9": break
        
        # Palindrome input validation
        elif opt == "1": playPalindrome()
        
        # digitsToWords input validation
        elif opt == "2": playDigitsToWords()
        
        # sumToTarget input validation
        elif opt == "3": playSumToTarget()
        
        # choose input validation
        elif opt == "4": playChoose()

    # Quit message.
    print("\nYou have left the Recursion Calculator. Bye!")

main()