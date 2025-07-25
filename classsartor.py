"""Class and Archetypes for the Sartor Class"""
from character import Character
import random


class Sartor(Character):
    def __init__(self, name: str, ability_scores : int, level : int, character_race : str, character_class : str, hit_points: int, mods, sanity, grit, prof, hit_dice, spirit_bond=None):
        super().__init__(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice, spirit_bond)



        if self.hit_points == "":
            chosen_hit_dice = max(self.hit_dice[0], min(4, self.hit_dice[1]))
            self.hit_points = chosen_hit_dice + self.mods[2]
            if self.level > 1:
                for i in range(self.level):
                    self.hit_points += random.randint(1, chosen_hit_dice) + self.mods[2]
                

    class_level_features = {
            "sartor": {
                "archetype" : {
                    "cometologist " : {"proficiencies" : ["insight", "will", "astral magic"],
                                "features" : {"Augury" : "Foresee the next three d12 results on random encounter checks.",
                                              "Starlink" : "Choose a comet. Gain +3 to spellcasting. This bonus becomes -3 if out of touch with that comet for more than 24 hours.",
                                              "Starsight" : "See in starlight as bright light.",
                                              "Touch of the Selvedge" : "Gain 1 first level Selven spell.",
                                              "Insightful" : "Gain advantage to insight checks.",
                                              "Well Studied" : "Gain advantage to information checks."
                                            },
                    },
                    "doorlock" : {"proficiencies" : ["intimidation", "deception", "profane magic"],
                                "features" : {"Doorfence" : "Gain the ability to use shields and light armor",
                                              "Lockmaster" : "Gain advantage to lockpicking.",
                                              "Full Cover" : "Gain advantage to hide in urban and dungeon environments when wielding a tower shield.",
                                              "Door Sense" : "Gain advantage to detect secret, false, and trapped doors. You hear perfectly through doors.",
                                              "Sarric" : "Gain one feature from the Sorcerer or Sanctioned Sartor archetypes.",
                                              "Bulwark" : "Tower Shields have -1 load, +2 DUR, and provide +1 to AC.",
                                              "Researcher" : "Magical Research requires half the time and cost.",
                                              "Breacher" : "Breach doors as a free action.",
                                              "Portalology" : "Teleportation spells affect twice as many creatures or have double range.",
                                              "Integrated Mythral" : "Tower shields may be used as a sarric focus, and may be inscribed as a spell tome."
                                            },
                    },
                    "elementalist" : {"proficiencies" : ["elemental magic", "tactics", "sarric lore"],
                                "features" : {"Equipped" : "Gain the ability to wear light armor and helms",
                                              "Martial" : "Gain martial weapon proficiency.",
                                              "Elemental Expert" : "Gain advantage to chosen element.",
                                              "Hearty" : "+6 to HP permanently.",
                                              "Scars of the Sartor Wars" : "+2 vesus magic and its practitioners.",
                                              "Acolyte of the Old Ways" : "Destroy Sarric writings in ritual and learn a Sorcerous spell of the same level."
                                            },
                    },
                    "maester" : {"proficiencies" : ["history", "diplomacy", "apothecary"],
                                "features" : {"Apothecary Rudiment" : "Gain advantage to apothecary checks.",
                                              "Know Thy Surroundings" : "Your party gains INT mod temp HP after resting.",
                                              "Knowledgeable" : "Gain advantage to knowledge checks.",
                                              "Elective Studies" : "Gain the ability to wear medium and light armor.",
                                              "Zealous Readings" : "Gain access to the Selven spell list.",
                                              "Scriptious" : "Scribing scrolls requires half the time and cost.",
                                              "Repulse" : "Turn the Veilish as Zealot",
                                              "Further Readings" : "Gain martial proficiency."
                                            },
                    },
                    "sorcerer" : {"proficiencies" : ["charm", "insalliric magic", "will"],
                                "features" : {"Crystalline Corpse" : "Your unarmored AC is 12 + DEX mod.",
                                              "Sturdy" : "+4 to HP permanently.",
                                              "Ungodly" : "Gain resistance to Selven effects.",
                                              "Repel" : "Gain advantage to resist magic.",
                                              "Reach for the Veil" : "Spend Sanity; attempt to cast a spell not known. Extremely dangerous.",
                                              "Quickcast" : "Choose one spell. It is now cast as a quick action.",
                                              "Veil Accuity" : "Choose a spell, and gain +1 to spellcasting with that spell. You may take this feature multiple times, and the cost increases by 5 EXP every time.",
                                              "Sorcerous Solitude" : "+2 spellcasting with no Followers."
                                            },
                    },
                    "warlock" : {"proficiencies" : ["profane magic", "intimidate", "stealth"],
                                "features" : {"Corporeal Protection" : "Gain the ability to use light armor and helms.",
                                              "Ceremonial Weaponry" : "Gain proficiency in Martial weapons.",
                                              "Intimidating" : "Gain advantage in intimidation checks.",
                                              "Dark Satiation" : "No need to eat.",
                                              "Darksight" : "Gain the ability to see in pitch black as in bright light, but bright light becomes blinding.",
                                              "Sacrifice" : "Deal damage to yourself, and add twice that damage to your next hit.",
                                              "Insatiable Mind" : "No need to sleep, but you still need to rest.",
                                              "Spider Climb" : "Gain the ability to climb any surface.",
                                            },
                    },
                    "sanctioned sartor" : {"proficiencies" : ["diplomacy", "insight", "sarric magic"],
                                "features" : {"Savant" : "Pick +1 cantrip. You may take this feature multiple times.",
                                              "Alchemist" : "Gain advantage to potions checks.",
                                              "Temporal Polarity" : "Choose one spell to become Insalliric or Ansalliric every time you cast it. You may take this feature multiple times.",
                                              "Informed" : "Gain advantage to information checks.",
                                              "Researcher" : "Magical Research requires half the cost and time.",
                                              "Altercation" : "Quick Action; reroll a magical mishap.",
                                              "Dominus Incantamenum" : "Double one spell's area or duration.",
                                              "Decorum" : "Wear a silly hat and gain +2 to spellcasting.",
                                              "Repreperation" : "Prepare your expended spells at 1 turn per spell level without resting.",
                                              "Dominus Nominum" : "Creatures whose True Name you know have disadvantage on spell saves and attack rolls against you."
                                            },
                    },
                            },
                "level_features" : {1 : "Sartor archetype, starting HP,sartor equipment,3 sarric cantrips, sarric spellcasting",
                                    2 : "1/rest raise AC by INT mod, quick action",
                                    3 : "Archetype feature",
                                    4 : "+1 to one ability score",
                                    5 : "1/rest, 10 min to dispel one spell of a level you can cast",
                                    6 : "+1 to one ability score",
                                    7 : "Archetype feature",
                                    8 : "+1 to one ability score",
                                    9 : "Pick one 1st level spell. You have full temporal control, and may cast it level times/rest. Resets after rest.",
                },
                                    },
    }

