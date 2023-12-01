#
#Melody Jing
#
# This program is a GUI which tests whether certain strings are palindromes or not.
#It ignores certain characters such as punctuation, capitalization, and white spaces.
#If non-palindromes are submitted thrice in a row, it prompts the user to quit.

from graphics import *
from Button import Button

def main():
    #Create win
    win=GraphWin("Palindrome Tester",500,250)

    #Draw entry box, message box and label, and each button.
    entryBox = Entry(Point(250,100),25).draw(win)

    messageBox = Rectangle(Point(30,190),Point(470,210)).draw(win)
    messageLabel = Text(Point(250,200),"Welcome to the palindrome tester! Enter a phrase above to test.").draw(win)
    
    tryAnotherButton = Button(win,Point(125,50 ), 40,210,
                            "Try Another",'black','black','ivory')
    quitButton = Button(win,Point(375,50), 40,210,
                        "Quit",'black','black','ivory')
    testButton = Button(win,Point(250,150), 40,210,
                        "Test",'black','black','ivory')

    #Activates the quit and test buttons.
    quitButton.activate()
    testButton.activate()

    #Presets fail counter to 0, quitvar to 0, and indicates that it is the first time
    #the user enters the progrma.
    failCount = 0
    firstTime = 1
    quitVar = 0

    #While loop checks for whether the consecutive fails is less than three, and
    #that quit has not been clicked.
    while failCount<3 and quitVar != 1:

        #Executes this section if it is not the first time.
        #Activates try another button and waits for it to be clicked.
        if firstTime != 1:
            tryAnotherButton.activate()
            
            pt=win.getMouse()
            while not (tryAnotherButton.clicked(pt) or quitButton.clicked(pt)):
                pt=win.getMouse()
                
            if quitButton.clicked(pt):
                win.close()
                quitVar = 1
                
            else:
                testButton.activate()
                tryAnotherButton.deactivate()

        # checks for quit
        if quitVar != 1:
            pt=win.getMouse()
            while not (quitButton.clicked(pt) or testButton.clicked(pt)):
                pt=win.getMouse()

            if quitButton.clicked(pt):
                win.close()
                quitVar = 1

            #If not quit:
            else:
                #grabs user input from entry box
                entry = entryBox.getText()

                #checks input for palindrome or not
                state = testPalindrome(entry)

                #if yes, sets fail counter to 0 and displays success message.
                if state:
                    failCount = 0
                    messageLabel.setText(entry+" is a palindrome. Press Try Another to test another phrase.")

                #if no, adds 1 to fail counter and displays failiure message.
                else:
                    failCount = failCount+1
                    messageLabel.setText(entry+" is not a palindrome. You have "
                                         +str(3-failCount)+
                                         " attempt(s) left until the program quits!")

                #redraws label
                messageLabel.undraw()
                messageLabel.draw(win)

                #Deactivates test button and resets entry box contents.
                #Sets first time to false.
                testButton.deactivate()
                entryBox.setText("")
                firstTime = 0

    if quitVar != 1:

        #Forces user to quit
        messageLabel.setText("You have failed to enter a palindrome three times in a row! You must quit now.")
        messageLabel.setFill("red")
        messageLabel.undraw()
        messageLabel.draw(win)

        pt=win.getMouse()
        while not quitButton.clicked(pt):
            pt=win.getMouse()

        win.close()


#This function inputs a string and outputs whether or not it is a palindrome.
def testPalindrome(string):

    #removes punctuation.
    punctuation = [",",".","-","?","!"," ",":",";","'",'"',
                   "1","2","3","4","5","6","7","8","9","0",
                   "&","–","(",")","’",'“','”',"\n"]
    for punct in punctuation:
        string = string.replace(punct,"")

    #Checks for empty string. If empty, then not palindrome.
    if len(string) == 0:
        return False
    
    #Gets rid of caps.
    string = string.lower()

    print(string)
    
    #Checks palindrome and returns true or false.
    if string == string[::-1]:
        return True
    else:
        return False


main()
