"""Class and Archetypes for the Warrior Class"""
from character import Character



class Warrior(Character):
    def __init__(self, name: str, ability_scores : int, level : int, character_race : str, character_class : str, hit_points: int, mods, sanity, grit, prof, hit_dice):
        super().__init__(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice)

        hit_dice = max(self.hit_dice[0], min(4, self.hit_dice[1]))


        if self.hit_points == "":
            self.hit_points = hit_dice + self.mods[2]
            if self.level > 1:
                for i in range(self.level):
                    self.hit_points += max(1, 6) + self.mods[2]



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