"""Main ability score calulations."""
# Lay out stat table and modifier.
# Choose race, which guarantees certain stats and proficiencies.
# Roll remaining stats in order.
# Display character stats.

import math
import random
from die import roll_dsix


# class hitdice, where first index is hit dice value, and second is starting hp value
class_hitdice = {"warrior" : [8, 6],
                   "rogue" : [4, 4],
                   "zealot" : [6, 5],
                   "sartor" : [4, 4],
                   "dungeoneer" : [6, 5]
}

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

spirit_bond_choices = {
    "Vulkjoran": "Spirits bound to Vulkjornn are souls bound to change, destruction, and building. Alteration and manipulation impact your life with utmost fervor. The world demands to be upended and altered by your passing. Change is by force.",
    "Korvyran": "Those bound to Korvyre are satisfied only by finality. Remembrance is the key to Absolution, and to forget is to leave the soul hollow. Venture far only with a goal, for meandering is of little substance, unless meandering is the objective.",
    "Akathian": "Akathian spirits are grounded in the existent, and what is meant to happen. One must be present, in every moment, for the absence of presence is the first step of subjugation. Self improvement is of utmost importance. Change will happen.",
    "Fean": "The spirit of preservation. The other is the self, and to sustain the world is to sustain your own. Outside improvement is of utmost importance. Virosia must be made better by your passing. Act slowly, act decisively, act only in consideration of the wisdom of others.",
    "Unbound": "Your way is your own, and your spirit calls to no ideal. None of the Four Spirits demand your utmost attention, and perhaps you pluck from all in equal part, or none.",
    "Bassyric": "You've welded your spirit with that of an otherworldly creature, one of the Selvedge. This bond is not natural to creatures of Virosia, and comes with aspects unique to every individual. A Bassyric-bonded spirit is necessary to cast Selven magic that stems from Bassyr. A Bassyric bond is most strong to the mind, and certain alien thoughts come into your purview.",
    "Silean": "Your spirit has been connected with that of a Silean entity.  This bond is not one natural to Virosia, and affects the body more than the spirit. This bond is necessary to cast Selven magic stemming from Silea. In some otherworldly way, your body is more strongly bound to your spirit."
}


class Character:
    """Keep it light, keep it bright, keep it gay"""
    # Create character sheet
    def __init__(self, name: str, ability_scores : int, level : int, character_race : str, character_class : str, hit_points: int, mods, sanity, grit, prof, hit_dice, spirit_bond):

        if level == "":
            level = random.randint(1, 13)

        if character_class == "":
            character_class = self.generate_class()

        if character_race == "":
            character_race = self.generate_race()

        if ability_scores == []: #iterate over the rolled states in races dictionary for chosen race, and rolls accordingly
            rolled_stats = [0, 0, 0, 0, 0, 0]
            for index in range(len(rolled_stats)):
                dice_type = races[character_race]["rolled_stats"][index]
                if dice_type == "3dsix":
                    rolled_stats[index] = roll_dsix() + roll_dsix() + roll_dsix()
                elif dice_type == "2dsix":
                    rolled_stats[index] = roll_dsix() + roll_dsix() + 3
                else:
                    rolled_stats[index] = 13

            ability_scores = rolled_stats

        if not spirit_bond:
            self.spirit_bond = random.choice(list(spirit_bond_choices.keys()))
        else:
            self.spirit_bond = spirit_bond

        self.mods = self.ability_mod(ability_scores)
        mods = self.mods

        sanity = max(1, 3 + mods[3])

        prof = math.ceil((level / 4) + 1)

        grit = max(1, prof + mods[2])

        self.name = name
        self.character_class = character_class
        self.ability_scores = ability_scores
        self.level = level
        self.character_race = character_race
        self.hit_points = hit_points
        self.sanity = sanity
        self.grit = grit
        self.hit_dice = races[character_race]["hitdice"]
        self.prof = prof
        self.spirit_bond_description = spirit_bond_choices.get(self.spirit_bond, "Unknown spirit bond.")



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
        #return the race chosen at random from the dictionary
        return list(races.values())[race_roll]["name"]



# hit dice
# max(lower of your race, lower between character class and the higher of your race's 2 options)
