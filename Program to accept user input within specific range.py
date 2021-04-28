# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 01:28:02 2021

@author: chait
"""

#Create a program to accept user inputs in te range (0,10)
#Do not accept inputs of wrong data type and out of range
#Put error messages in the code

def print_value_0to10():
    #Declaring theinitial variables to check the conditions
    #Variables
    input_value = 'notdigit'
    acceptable_range = range(1,11)
    within_range = False
#Need to check for 2 conditions
#isdigit() or within_range == False
    while input_value.isdigit() == False or within_range == False:
        
        input_value = input("Input a value between digits (1,10): " )
        
        #Digit check
        if input_value.isdigit() == False:
            print("Please enter a digit")
            
        #Range check
        if input_value.isdigit() == True:
            if int(input_value) in acceptable_range:
                within_range = True
            else:
                print('Enter a value within range')
            
    
    
    return int(input_value)

print_value_0to10()


    