# Revision number 1 10Feb2022
## Begin Derek Ruggirello here 9Feb2022

names = [] # List of guest names

terminator = "" # Termination variable that also stores data for lists

while terminator != "done": # Loop to add user input into the names list
    terminator = input("Please enter the name of your guest and type done after your last guest. EX. First Last \n")
    if terminator != "done": # Selector to cancel loop when user is done
        names.append(terminator)
    else:
        continue

dates = [] # List of the invitation date of each guest

for ind, val in enumerate(names): # Loop to input the date for each guests invitation
    terminator = input("Please enter the date "+ val + " was invited: \n") # Store date in variable
    dates.append(terminator) # Adds the date to the dates list

for ind, val in enumerate(names): # Loop to print the names with dates. Enumerating the list in order to reference index and value
    print(val, "invited", dates[ind]) # Outputs the name and invitation date

for x in names: # Loop to determine if name needs big or small tag.
    if len(x) < 12: # Using length function to get the size of names.
        print(x, "goes on a small tag.")
    else:
        print(x, "goes on a big tag.")

# Revision number 1 10Feb2022
## End Derek Ruggirello here
# Omega Group/ Ram Valud/ Michael Walker/ project greenwood321 #