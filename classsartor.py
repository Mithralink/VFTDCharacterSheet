"""Class and Archetypes for the Sartor Class"""
from character import Character
import random


class Sartor(Character):
    def __init__(self, name: str, ability_scores : int, level : int, character_race : str, character_class : str, hit_points: int, mods, sanity, grit, prof, hit_dice, spirit_bond=None):
        super().__init__(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice, spirit_bond)

        hit_dice = max(self.hit_dice[0], min(4, self.hit_dice[1]))


        if self.hit_points == "":
            self.hit_points = hit_dice + self.mods[2]
            if self.level > 1:
                for i in range(self.level):
                    self.hit_points += max(1, 6) + self.mods[2]



        print(f"{self.name}, You're a level {self.level} {self.character_race} Sartor!")
        print(f"You have {self.level}d8 and {self.hit_points} HP")
        print(f"You have {self.grit} grit and {self.sanity} sanity.")
        print(f"Your Archetype Features are: ")
        print("Your Ability Scores:")
        print(f"Strength {self.ability_scores[0]} ({self.mods[0]})")
        print(f"Dexterity {self.ability_scores[1]} ({self.mods[1]})")
        print(f"Constitution {self.ability_scores[2]} ({self.mods[2]})")
        print(f"Intelligence {self.ability_scores[3]} ({self.mods[3]})")
        print(f"Wisdom {self.ability_scores[4]} ({self.mods[4]})")
        print(f"Charisma {self.ability_scores[5]} ({self.mods[5]})")
        print(f"Spirit Bond: {self.spirit_bond}")
        print(f"Spirit Bond Description: {self.spirit_bond_description}")

