"""Class and Archetypes for the Warrior Class"""
from character import Character
import random


class Warrior(Character):
    def __init__(self, name: str, ability_scores : int, level : int, character_race : str, character_class : str, hit_points: int, mods, sanity, grit, prof, hit_dice, spirit_bond=None):
        super().__init__(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice, spirit_bond)



        if self.hit_points == "":
            chosen_hit_dice = max(self.hit_dice[0], min(8, self.hit_dice[1]))
            self.hit_points = chosen_hit_dice + self.mods[2]
            if self.level > 1:
                for i in range(self.level):
                    self.hit_points += random.randint(1, chosen_hit_dice) + self.mods[2]



        print(f"{self.name}, You're a level {self.level} {self.character_race} Warrior!")
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


    def stat_check(self, skill: str):
        if skill == "strength":
            return random.randint(1, 20) + self.mods[0] + self.prof
        elif skill == "dexterity":
            return random.randint(1, 20) + self.mods[1]
        elif skill == "constitution":
            return random.randint(1, 20) + self.mods[2] + self.prof
        elif skill == "intelligence":   
            return random.randint(1, 20) + self.mods[3]
        elif skill == "wisdom":
            return random.randint(1, 20) + self.mods[4]
        elif skill == "charisma":
            return random.randint(1, 20) + self.mods[5]
        else:
            raise ValueError("Invalid skill name. Choose from strength, dexterity, constitution, intelligence, wisdom, or charisma.")
        

    def get_summary(self):
        return (
            f"{self.name}, You're a level {self.level} {self.character_race} Warrior!\n"
            f"You have {self.level}d8 and {self.hit_points} HP\n"
            f"You have {self.grit} grit and {self.sanity} sanity.\n"
            f"Your Archetype Features are: \n"
            f"Your Ability Scores:\n"
            f"Strength {self.ability_scores[0]} ({self.mods[0]})\n"
            f"Dexterity {self.ability_scores[1]} ({self.mods[1]})\n"
            f"Constitution {self.ability_scores[2]} ({self.mods[2]})\n"
            f"Intelligence {self.ability_scores[3]} ({self.mods[3]})\n"
            f"Wisdom {self.ability_scores[4]} ({self.mods[4]})\n"
            f"Charisma {self.ability_scores[5]} ({self.mods[5]})\n"
            f"Spirit Bond: {self.spirit_bond}\n"
            f"Spirit Bond Description: {self.spirit_bond_description}"
        )


    class_level_features = {
            "warrior": {
                "archetype" : {
                    "barbarian" : {"proficiencies" : ["intimidation", "endurance", "travel"],
                                "features" : {"8 HP" : "+8 permanent HP.",
                                                "Terrifying" : "Advantage to intimidaton checks."},
                    },
                    "caestus" : {"proficiencies" : ["intimidation", "deception", "profane magic"],
                                "features" : {"feature_name" : "what it does",
                                                "feature_name" : "what it does"},
                    },
                    "fighter" : {"proficiencies" : [],
                                "features" : {"feature_name" : "what it does",
                                                "feature_name" : "what it does"},
                    },
                    "knight" : {"proficiencies" : [],
                                "features" : {"feature_name" : "what it does",
                                                "feature_name" : "what it does"},
                    },
                    "ward" : {"proficiencies" : [],
                                "features" : {"feature_name" : "what it does",
                                                "feature_name" : "what it does"},
                    },
                    "pirate" : {"proficiencies" : [],
                                "features" : {"feature_name" : "what it does",
                                                "feature_name" : "what it does"},
                    },
                    "ranger" : {"proficiencies" : [],
                                "features" : {"feature_name" : "what it does",
                                                "feature_name" : "what it does"},
                    },
                    "scarsan" : {"proficiencies" : [],
                                "features" : {"feature_name" : "what it does",
                                                "feature_name" : "what it does"},
                    },
                    "witcher" : {"proficiencies" : [],
                                "features" : {"feature_name" : "what it does",
                                                "feature_name" : "what it does"},
                    },
                            },
                "level_features" : {1 : "level 1 features",
                                    2 : "level 2 features",
                                    3 : "level 3 features",
                                    4 : "level 4 features",
                                    5 : "level 5 features",
                                    6 : "level 6 features",
                                    7 : "level 7 features",
                                    8 : "level 8 features",
                                    9 : "level 9 features",
                },
                                    },
    }