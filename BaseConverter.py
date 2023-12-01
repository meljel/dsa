# Melody Jing
# A numeric base converter that uses base 10 as an intermediary.

# Input: none
# Output: no output - exits if user inputs a blank entry
def convertBase():
    print("Welcome to the base converter! \n\
Please enter integers according to the prompts. \n\
Each base should be integers from 2 to 16. \n\
Leave any entry blank to quit. \n")

    # presets quit to false
    q = 0

    # again only loops while user doesn't quit
    while q == 0:
        
        result = convertBaseUI()

        # if type is a string, there is an error. print error msg
        if type(result[0]) is str:
            print(result[0])

        # if type is an int, exit program
        elif type(result[0]) is int:
            print("Thanks for using the Base Converter! Goodbye")
            return

        # if type is a list, do the conversion
        else:
            decimalInt = convertToDecimal(result[0][0],result[0][1])
            destNum = convertToDest(decimalInt,result[0][2])
            print("\nNEW NUMBER: "+destNum+" (base "+str(result[0][2])+")")

        # update whether user wants to quit or not
        q = result[1]

        # preemptively print divider
        # if program gets to this point, user has not quit
        print("\n****** Another Run ******")

    return


# Input: none
# Output: one out of:
#                       - (string of an error message, q)
#                       - (int signaling a quit, q)
#                       - (list of user inputs, q)
def convertBaseUI():
    """Handles the user input of convertBase() and makes it into
       a list of ints in order to input into convertToDecimal()."""

    #SOURCE BASE
    srcBaseStr = input("Source Base: ")

    # if user inputs nothing, return an int to quit
    if srcBaseStr == "":
        return 1,1
    
    try:
        # verify that base is an integer
        srcBase = int(srcBaseStr)

        # verify that 2<=b<=16
        if srcBase < 2 or srcBase > 16:
            return "The source base must be a value between 2 and 16!", 0
            
    except:
        return "The source base must be an integer!", 0


    #SOURCE NUMBER
    srcNum = input("Source Number: ")
    
    # if user inputs nothing, return an int to quit
    if srcNum == "":
        return 1,1

    # converts string into list of strings
    srcNumList = list(srcNum)

    # verify that there is no decimals
    if "." in srcNumList:
        return "Please do not enter decimals!", 0

    # presets valid character list, valid up to base 10
    validCharList = ["0","1","2","3","4","5","6","7","8","9"]

    # depending on srcBase, determines actual valid char list
    # uses ascii values for a-f and A-F
    if srcBase < 11:
        for digit in srcNumList:

            # verify if given digit is within valid character list
            if digit not in validCharList:
                return "Please enter a value from the source base!", 0

            # verify if the digit is less than highest possible in srcBase
            if int(digit) > 9 or int(digit)>srcBase-1:
                return "Please enter a value from the source base!", 0

    else:        # srcBase > 10:

        # extends valid character list according to srcBase
        for i in range(11,srcBase+1):

            # includes lowercase a-f
            lowerLetter = chr(86+i)

            # includes uppercase A-F
            upperLetter = chr(54+i)
            
            validCharList.extend([lowerLetter,upperLetter])

        # counts iteration number
        it = 0

        # for each char, check if it is in valid characer list
        for digit in srcNumList:
            if digit not in validCharList:
                return "Please enter a value from the source base!", 0

            # convert string of digit to int of digit
            if ord(digit) in range(48,58):
                srcNumList[it] = ord(digit)-48

            # convert lowercase letter to equivalent int
            elif ord(digit) in range(97,103):
                srcNumList[it] = ord(digit)-87

            # convert uppercase letter to equivalent int
            else: # ord(digit) in range(65,71):
                srcNumList[it] = ord(digit)-55

            it = it+1


    #DESTINATION BASE
    destBaseStr = input("Destination Base: ")

    # if user inputs nothing, return an int to quit
    if destBaseStr == "":
        return 1,1
    
    try:
        # verify if dest base is an integer
        destBase = int(destBaseStr)

        # verify if dest base is 2<=b<=16
        if destBase < 2 or destBase > 16:
            return "Destination base must be a value between 2 and 16!", 0
            
    except:
        return "Destination base must be an integer!", 0

    return [srcBase, srcNumList, destBase], 0


# Input: source base (int), srcNumList (list)
# Output: decimalValue int
def convertToDecimal(srcBase, srcNumList, decimalValue = 0):
    """converts list of ints to decimal number. Optional parameter
       of decimalValue, for when there already exists such a value."""
    
    length = len(srcNumList)

    # skips this step if srcBase is 10; converts to string
    if srcBase == 10:
        decimalValue = ""
        for element in srcNumList:
            decimalValue = decimalValue + str(element)

        return int(decimalValue)

    # if end of recursion
    elif length == 1:
        decimalValue = int(srcNumList[0])

    # example: 567 base 10 = 7 + 56 * 10 = 7 + 10(6 + 10(5))
    else:
        digit = srcNumList.pop()
        decimalValue = int(digit) + srcBase * convertToDecimal(srcBase, srcNumList, decimalValue)
        
    return decimalValue


# Input: decimalValue (int), destBase (int)
# Output: destNum (string)
def convertToDest(decimalValue, destBase, destNum = ""):
    """converts decimal to destination base. Optional parameter of
       destNum, for when there already exists such a list."""

    # skips this step if destBase is 10
    if destBase == 10:
        return str(decimalValue)

    # determines lowest possible remainder less than dest base
    # to use as highest digit
    quotient = decimalValue // destBase
    remainder = decimalValue - destBase * quotient

    # determines which string to add
    if remainder < 10:
        remChar = str(remainder)

    # outputs uppercase letter
    else:
        remChar = chr(remainder+55)

    # attaches new digit to the left of original list
    destNum = remChar + destNum

    # recurses only if division results in positive quotient
    if quotient != 0:
        destNum = convertToDest(quotient, destBase, destNum)

    return destNum

convertBase()