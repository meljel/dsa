#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:58:47 2021

@author: meljel
"""

import random
import TwoStackQueue as q

def main():
    """Run the time management game."""

    # Welcome statement.
    print("Welcome to the time cafe. \nServe all customers before they lose patience!")
    
    # Request number of customers until input is valid or program is quit
    while True:
        # Gets customer input from user.
        customers = input("Number of customers in line: ")
        
        try:
            # Check if input is a number.
            customers = int(customers)
            
            # Check if input is positive.
            if customers > 0:
                run = True
                break
            
            else:
                # Print error message telling user to enter a positive integer.
                print("Please enter a positive integer. (Enter 'Q' to quit)")
        
        except:
            # Check if the user wants to quit the program.
            if customers[0] == "Q" or customers[0] == 'q':
                run = False
                break
            
            # Print error message telling user to enter an integer. 
            print("Please enter an integer.")
    
    # Run if user has not quit.
    if run:
        print("Okay! Let's play.")
        
        # Create an instance of Queue with lunchLine on.
        line = q.Queue(customers, True)
        
        # Enqueue "customer" (represented by their patience)
        for k in range(customers):
            # Randomly generate patience given the range [1,customers].
            line.enqueue(random.randint(1,customers + 1))
        
        seated, lost = 0,0
    
    # Run if user has not quit.
    while run: # or while run = 1
        
        # Break the loop if the line has been depleted.
        if line.length() == 0:
            break
        
        # Initially dequeue the first person in the queue.
        current = line.dequeue()
        # If their patience is 0 or None, proceed to the next customer in line.
        if not current:
            continue
        
        # Prompt user with three options for the current customer.
        print("\nA new customer is waiting. (Patience: " + str(current) + ")")
        print("\n    (1) Seat customer \n    (2) Wait \n    (3) Quit")
        
        i = input("Action (1,2,3): ")
        
        # Wait for response from user on selected option until it is valid.
        while i not in ["1","2","3"]:
            print("Please choose an action between options 1, 2, and 3.")
            print("\n    (1) Seat customer \n    (2) Wait \n    (3) Quit")
            i = input("Action (1,2,3): ")
        
        # Seat the customer.
        if i == "1":
            print("\nYou sat a new customer.")
            seated += 1
        
        # Make the customer wait; requeue.
        elif i == "2":
            line.enqueue(current)
            print("\nYour customer is now waiting.")
        
        # Quit the while loop.
        elif i == "3":
            run = False
            break

        # Lower each customer's patience by 1. 
        numLost = line.timePass(1)
        
        # Print how many customers are lost.
        lost += numLost
        if numLost == 1:
            print("You lost a customer.")
        elif numLost > 1:
            print("Uh oh! You lost", str(numLost), "customers.")
        
    # Run if user has quit.    
    if not run:
        print("\nYou have quit the game. Goodbye!")
        raise SystemExit
    
    # Print that the queue has been cleared, and the game is over.
    print("\nThere are no more customers in line. \n\
You sat", str(seated), "customers and lost", str(lost), "customers.\n\n\
Thanks for playing!")

main()