"""Main file for character creation."""
# imports
from statcalculation import manual_character_sheet
from ran_gen import random_character_sheet

# Deciding to make a random character or not
while True:
    random_character = input("Would you like to create a random character? (Y/N) ").upper()
    if random_character == "N" or random_character == "Y":
        break
    else:
        print("Please enter either Y or N.")



#if not
if random_character == "N":
    manual_character_sheet()

elif random_character == "Y":
    random_character_sheet()
