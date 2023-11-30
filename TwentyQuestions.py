# Melody Jing
# Implements TwentyQs using a modified version of a binary search tree. Each
# node of the BST represents either a question or an answer. If the node is a
# leaf, then it represents a possible guess; otherwise, it represents a
# question. The game is played traversing the tree, depending on the user's
# answers to yes/no questions.

class Node():
    """A node class with child, parent, and leaf attributes."""

    def __init__(self, isLeaf: bool, name: str):
        self.p, self.right, self.left = None, None, None
        self.isLeaf = isLeaf
        self.name = str(name)

    def setLeft(self, newNode):
        self.left = newNode
    def getLeft(self):
        return self.left
    def setRight(self, newNode):
        self.right = newNode
    def getRight(self):
        return self.right
    def setParent(self, newParent):
        self.p = newParent
    def getParent(self):
        return self.p
    def getName(self):
        return self.name
    def leaf(self):
        return self.isLeaf


class TwentyBST():
    """A modified binary search tree that works for the game Twenty Questions.
       Stores nodes."""
    def __init__(self):
        self.nodes = []

    def getRoot(self):
        return self.root
    def setRoot(self, node):
        self.root = node
    def getNodes(self):
        return self.nodes
    def newNode(self, isLeaf, name):
        newNode = Node(isLeaf, name)
        self.nodes.append(newNode)


def _createTree():
    """Initialize a tree with three nodes for the game Twenty Questions."""
    # Create tree
    TQ = TwentyBST()

    # Root node
    TQ.newNode(False, "Is it bigger than a bread box? ")  # Add a question node
    root = TQ.getNodes()[0]  # Get the node
    TQ.setRoot(root)  # Assign it as the root

    # Mouse as one solution
    TQ.newNode(True, "mouse")  # Create the new mouse node
    mouseNode = TQ.getNodes()[-1]  # Add it to the leaves dict
    mouseNode.setParent(root)  # Set its parent to the root
    root.setLeft(mouseNode)  # Set it to the root's left child

    # Elephant as the other
    TQ.newNode(True, "elephant")  # Create the new elephant node
    elephantNode = TQ.getNodes()[-1]  # Add it to the leaves dict
    elephantNode.setParent(root)  # Set its parent to the root
    root.setRight(elephantNode)  # Set it to the root's right child

    return TQ, root


def _addGuess(TQ: TwentyBST, n: Node, m: Node, direction: str):
    """Guess if a leaf is the correct answer."""
    newGuess = input("What were you thinking? ")
    newQuestion = input("What is a yes/no question distinguishes it from "
                        + m.getName() + "? ").strip() + " "

    # Get answer to proposed question
    newAns = _getYesNo("Is yes or no the correct answer to get to "
                       + newGuess + "? ")

    # Add both the new question and the new answer
    TQ.newNode(False, newQuestion)  # Create new question node
    qNode = TQ.getNodes()[-1]  # Retrieve latest node
    TQ.newNode(True, newGuess)  # Create new answer node
    ansNode = TQ.getNodes()[-1]  # Retrieve latest node

    # Establish/change connections between nodes
    if newAns.lower() == "yes":
        qNode.setParent(n)  # Set new question's parent to initial question
        qNode.setRight(ansNode)  # Set 'yes' to answer
        qNode.setLeft(m)  # Set 'no to question
    else:
        qNode.setParent(n)  # Set new question's parent to initial question
        qNode.setLeft(ansNode)  # Set 'no' to answer
        qNode.setRight(m)  # Set 'yes' to question

    # Decide which child the new question node is
    if direction == "right":
        n.setRight(qNode)  # Set question node to 'yes'
    else:
        n.setLeft(qNode)  # Set question node to 'no'

    print("Got it -- thanks!")


def _getYesNo(txt: str):
    """Get user input iff it is yes or no."""
    while True:  # Wait for a valid user input
        userInput = input(txt)  # Get user input
        procInput = userInput.lower().strip()  # Strip uppercases, spaces
        if procInput == "yes" or procInput == "no":  # Is it a valid input
            break
        else:  # Wait until it is
            print("Please enter either 'yes' or 'no'!")
    return procInput


def TwentyQs():
    """Play the Twenty questions game."""
    # Welcome message
    print("Welcome to Twenty Questions!\n\
Think of something and I'll try to guess it asking at most 20 questions.")

    # Create tree
    tree = _createTree()  # Initialize BST with modified Nodes
    TQ, root = tree[0], tree[1]  # Assign BST chars to vars
    n, direction, numQ = root, None, 1

    # Keep making turns until the user quits
    while True:  # Until user quits

        # Evaluate user input
        ans = _getYesNo(n.getName())  # Get user yes/no

        # Go left or right depending on input
        if ans.lower() == "yes":
            m = n.getRight()  # Visit the right node if yes
            direction = "right"
        else:
            m = n.getLeft()  # Visit the left node if no
            direction = "left"

        # Guess
        if m.leaf():  # If next node is a leaf, guess the leaf

            # Ask if it's a leaf name
            guessCorrect = _getYesNo("Is it a(n) " + m.getName() + "? ")

            # If computer guesses correctly
            if guessCorrect.lower() == "yes":
                print("Yay, I guessed it!")

            # If max questions has been reached
            elif numQ >= 20:
                print("Oh no, I couldn't get it!")

            # If object is unknown to computer
            else:
                _addGuess(TQ, n, m, direction)
                numQ += 1

        # Ask the next question
        else:  # If the next node is not a leaf, ask the node's question
            n = m  # Set new starting node to a child of the previous node
            continue

        # Ask if user wants to keep playing
        keepPlaying = input("Do you want to play again? ")

        # Quit the game if no
        if keepPlaying.lower() == "no":
            print("\nThank you for playing!")
            break
        
        # Reset the next-asked question to the root
        n = root


TwentyQs()
