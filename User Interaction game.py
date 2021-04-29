# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 18:28:46 2021

@author: chait
"""

#Create a simple user interaction game to take a input at predefined index positions in a game list
#If the input index position given by user is not present in the list ask for a valid choice again
#Put a function allowing user to quit the game when necessary


def display_game_list(game_list):
    print("This is the game list: ")
    print(game_list)
    

#To select the desired index position
def choose_position():
    
    acceptable_indexes = ['0','1','2']
    in_list_index = False
    
    while in_list_index == False:
        choice = input("Please enter values within index position [0,1,2] ")
        
        if choice in acceptable_indexes:
            in_list_index = True
        else:
            print("Please enter a valid index value")
    
    print(int(choice))
    return int(choice)

            

#To take a desired input from the user to be placed at the selected index value
def choose_replacement(game_list, position):
    
    replacement_input = input("Please enter the desired value: ")
    
    game_list[position] = replacement_input
    
    return game_list


#To check if user wants to continue with the game or exit [Y/N]
def game_on_select():
    
    game_yes_no = ['Y','N']
    game_choice = "wrong"
    
    while game_choice not in game_yes_no:
        input_game_choice = input("Do you want to continue with the game [Y/N]: ")
        game_choice = input_game_choice
        
        if input_game_choice not in game_yes_no:
           print("Incorrect input, Please select [Y/N]")
    
    if game_choice == "Y":
        return True
        print(True)
    else:
        return False
        print(False)


#Code to run the game together
game_list = [0,1,2]
game_on = True

while game_on:
    
    display_game_list(game_list)
    
    position = choose_position()
    
    game_list = choose_replacement(game_list, position)
    
    display_game_list(game_list)
    
    game_on = game_on_select()
    
    


