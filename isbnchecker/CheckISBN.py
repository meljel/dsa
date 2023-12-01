# Melody Jing
#
# This program inputs a file containing potential ISBN codes and outputs a file which sorts
# them into two lists: one with valid ones, and another with invalid ones. The list of invalid
# ISBN codes includes one reason why the code is invalid.

def main():

    #User friendly message instructing what to do
    print("Welcome to the ISBN tester! To get started, follow the prompts below. "+
          "Note that the input file must be formatted so that each potential ISBN code "+
          "appears on a separate line.")
    
    #get user input for file names, both input and output
    fname = input("Input file (default is \"InputISBNExample.txt\" if given empty input): ")
    oname = input("Output file (default is \"OutputISBNExample.txt\" if given empty input): ")
    if fname == "": fname = "InputISBNExample.txt"
    if oname == "": oname = "OutputISBNExample.txt"

    #read the file
    myfile = open(fname, "r")
    data = myfile.readlines()
    if myfile.read() == "":
        print("This file is empty! Please input a file containing potential ISBN values.")
    myfile.close()

    #set both lists to empty
    validISBNs = []
    invalidISBNs = []    

    #Filtering each potential ISBN code .
    for line in data:
        ####test for isbn

        print(len(line.rstrip()))
        lineRes = testISBN(line.rstrip())
        
        #Determining which error message should be printed after the code through the output
        #of testISBN().

        # if output is 0, there is no problem, so the code is put into the valid list.
        if lineRes == 0:
            validISBNs.append(line.rstrip())

        # if output is not 0, the code is put into the invalid list.
        # Depending on numerical output, different reasons are listed below.
        elif lineRes == 1:
            invalidISBNs.append(line.rstrip() + " (is not 10 characters)")
            
        elif lineRes == 2:
            invalidISBNs.append(line.rstrip() + " (characters 1-9 are not all digits)")
            
        elif lineRes == 3:
            invalidISBNs.append(line.rstrip() + " (character 10 is neither a digit nor x/X)")
            
        else:
            invalidISBNs.append(line.rstrip() + " (the following equation is not true: " +
                                "(10c1+9c2+8c3+7c4+6c5+5c6+4c7+3c8+2c9+c10) mod 11 = 0")

    #Prints lists in new files.
    saveFile = open(oname,"w")

    #valid isbn list.
    print("Valid ISBNs: ", file=saveFile)
    for line in validISBNs:
        print(line, file=saveFile)

    print("----------------", file=saveFile)

    #Invalid isbn list.
    print("Invalid ISBNs: ", file=saveFile)
    for line in invalidISBNs:
        print(line, file=saveFile)
    
    saveFile.close()

#Function which inputs each potential ISBN and outputs a numeric value indicating the error
#that occured or valid.
    
def testISBN(potentialISBN):
    #Testing if length is 10.
    if len(potentialISBN) != 10:
        return 1

    #Presetting sum to 0.
    total = 0
    i = 0

    #Testing whether each char from 1 to 9 is a digit.
    for ch in potentialISBN[0:9]:
        if not ord(ch) in range(48,58):
            return 2
        total = total + (10-i)*int(ch)
        i=i+1

    #Testing whether the 10th char is either a digit or X.
    if ((potentialISBN[-1] == "X") or (potentialISBN[-1] == "x")):
        total = total + 10
        
    elif (ord(potentialISBN[-1]) in range(48,58)):
        total = total + int(potentialISBN[-1])
        
    else:
        return 3

    #Testing whether the sum expression is divisible by 11.
    if total%11 != 0:
        return 4

    #If all tests are passed, the string is valid.
    else:
        return 0

main()
