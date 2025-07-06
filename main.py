"""Main ability score calulations."""
# Lay out stat table and modifier.
# Choose race, which guarantees certain stats and proficiencies.
# Roll remaining stats in order.
# Display character stats.

import math
import random
from die import roll_dsix



class_hitdice = {"warrior" : 8,
                   "rogue" : 4,
                   "zealot" : 6,
                   "sartor" : 4,
                   "dungeoneer" : 6,
                   "bastard" : 10}



races = {
     "fjoran": {
        "name" : "fjoran",
        "hitdice" : [6, 8],
        "rolled_stats" : ["2dsix", "2dsix", "13", "13", "2dsix", "2dsix"]
        },
    "shaelarae": {
        "name" : "shaelarae",
        "hitdice" : [4, 6],
        "rolled_stats" : ["2dsix", "13", "2dsix", "13", "2dsix", "2dsix"]
        },
    "talii": {
        "name" : "talii",
        "hitdice" : [6, 8],
        "rolled_stats" : ["13", "2dsix", "13", "2dsix", "2dsix", "2dsix"]
        },
    "human": {
        "name" : "human",
        "hitdice" : [4, 8],
        "rolled_stats" : ["3dsix", "3dsix", "3dsix", "3dsix", "3dsix", "3dsix"]
        },
    "bassyrikin": {
        "name" : "bassyrikin",
        "hitdice" : [4, 8],
        "rolled_stats" : ["3dsix", "3dsix", "3dsix", "3dsix", "3dsix", "3dsix"]
        },
}



class Character:
    """Keep it light, keep it bright, keep it gay"""
    # Create character sheet
    def __init__(self, name, ability_scores, level : int, character_race : str, character_class : str, hit_points : int, feats = None):



        if character_class == "":
            character_class = self.generate_class()

        if character_race == "":
            character_race = self.generate_race()

        if ability_scores == []: #iterate over the rolled states in races dictionary for chosen race, and rolls accordingly
            rolled_stats = [0, 0, 0, 0, 0, 0]
            print(character_race)
            for index in range(len(rolled_stats)):
                dice_type = races[character_race]["rolled_stats"][index]
                if dice_type == "3dsix":
                    rolled_stats[index] = roll_dsix() + roll_dsix() + roll_dsix()
                elif dice_type == "2dsix":
                    rolled_stats[index] = roll_dsix() + roll_dsix() + 3
                else:
                    rolled_stats[index] = 13

            ability_scores = rolled_stats

        mods = self.ability_mod(ability_scores)


        sanity = max(1, 3 + mods[3])
        prof = math.ceil((level / 4) + 1)
        grit = max(1, prof + mods[2])


        hit_dice = max(races[character_race]["hitdice"][0], min(class_hitdice[character_class], races[character_race]["hitdice"][1]))
        print(hit_dice)


        print(f"{name}, You're a level {level} {character_race} {character_class}!")
        print(f"You have {level}d{hit_dice} and have {hit_points} HP")
        print(f"You have {grit} grit and {sanity} sanity.")
        print(f"Your Archetype Features are: {feats}")
        print("Your Ability Scores:")
        print(f"Strength {ability_scores[0]} ({mods[0]})")
        print(f"Dexterity {ability_scores[1]} ({mods[1]})")
        print(f"Constitution {ability_scores[2]} ({mods[2]})")
        print(f"Intelligence {ability_scores[3]} ({mods[3]})")
        print(f"Wisdom {ability_scores[4]} ({mods[4]})")
        print(f"Charisma {ability_scores[5]} ({mods[5]})")



    def ability_mod(self, ability_scores):
        """Take ability score input and produce modifier"""

        modifiers = []
        for score in ability_scores:
            modifiers.append(int((score - 10) / 2))
        return modifiers



    def generate_class(self):
        """generate a random class"""
        return list(class_hitdice.keys())[random.randint(0, len(class_hitdice.keys()) - 1)]
        #basically same as below

    def generate_race(self):
        """generate a random race"""

        race_roll = random.randint(0, len(races.keys()) - 1)
        #use length of keys in races dictionary, and choose a random one
        #return the race chosen at random from the disctionary
        return list(races.values())[race_roll]["name"]




toeman = Character("toeman", [], 1, "", "", None, None)


# hit dice
# max(lower of your race, lower between character class and the higher of your race's 2 options)