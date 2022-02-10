# Revision number 1 9Feb2022
## Begin Derek Ruggirello here 9Feb2022

import random # import random library

from os import terminal_size


wheel = [
    "BLACK28", "RED9", "BLACK26", "BLACK30", "RED11",
    "RED7", "BLACK20", "BLACK32", "RED17", "RED5", 
    "BLACK22", "BLACK34", "RED15", "RED3", "BLACK24", 
    "BLACK36", "RED13", "RED1", "RED27", "BLACK10", "RED25", 
    "RED29", "BLACK12", "BLACK8", "RED19", "RED31", "BLACK18", 
    "BLACK6", "RED21", "RED33", "BLACK16", "BLACK4", "RED23", 
    "RED35", "BLACK14", "BLACK2", "0", "00"
] # Listing of all American roulette bets

bet = "" # Variable to store user inputted bet

LOG = [] # Log to record previous slots

i = 0 # Iterator for log

while bet != "quit": # Loop for user to continue betting
    
    # Storing user bet inside bet variable
    bet = input("Please select a slot to bid on or type quit to quit:")

    LOG.append(wheel[random.randrange(0, 39)]) # Randomly selects one of the slots

    if LOG[i] == bet:
        print(LOG[i], "You Win!") # When user bets correctly they win
    elif bet == "quit": # Bypassing selection so the game does not run on quit
        continue
    else:
        print(LOG[i], "Better luck next time.") # When user loses the bet

    i =+ 1 # Increments the iterator

# Revision number 1 10Feb2022
## End Derek Ruggirello here
# Omega Group/ Ram Valud/ Michael Walker/ project greenwood321 #