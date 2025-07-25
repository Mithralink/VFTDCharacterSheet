"""Class and Archetypes for the Rogue Class"""
from character import Character
import random


class Rogue(Character):
    def __init__(self, name: str, ability_scores : int, level : int, character_race : str, character_class : str, hit_points: int, mods, sanity, grit, prof, hit_dice, spirit_bond=None):
        super().__init__(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice, spirit_bond)


        if self.hit_points == "":
            chosen_hit_dice = max(self.hit_dice[0], min(4, self.hit_dice[1]))
            self.hit_points = chosen_hit_dice + self.mods[2]
            if self.level > 1:
                for i in range(self.level):
                    self.hit_points += random.randint(1, chosen_hit_dice) + self.mods[2]


    class_proficiencies = ["stealth", "deception", "senses", "tools"]


    class_level_features = {
            "rogue": {
                "archetype" : {
                    "acrobat" : {"proficiencies" : ["balancing", "acrobatics", "athletics"],
                                "features" : {"Cat's Grace" : "Ignore first 10 feet of falling damage.",
                                                "Tumbling Attack" : "Win a contested DEX check and deal double damage.",
                                                "Balanced" : "Tightrope walk at full speed.",
                                                "Silent Steps" : "Advantage on stealth checks that require silence.",
                                                "Fleet" : "Automatically disengage from melee attacks when moving away.",
                                                "Nimble Wrists" : "+2 to light blades and staff weapons.",
                                                "Footwork" : "+10 feet to movement speed.",
                                                "Climber" : "Gain a natural climbing speed."},
                                "level_titles" : ["Apprentice", "Tumbler", "Jumper", "Gymnast", "Vaulter", "Leaper", "Aerialist", "Acrobat", "Master Acrobat"]
                    },
                    "assassin" : {"proficiencies" : ["intimidation", "insight", "tracking "],
                                "features" : {"Poisoner" : "Gain the ability to craft custom poisons.",
                                                "Anatomical Precision" : "Stealth crit widens to 18-20.",
                                                "Silent Killer" : "Gain advantage on stealth checks.",
                                                "Disguiser" : "Gain advantage on disguise checks.",
                                                "Viper's Recoil" : "Hide immediatley after a successful attack from stealth.",
                                                "Tracker" : "Gain advantage on tracking a known target.",
                                                "Godsunder" : "Gain the ability to assassinate superheroic types.",
                                                "Sneak Attack" : "Once per fight, add 2d6 damage to a successful attack from stealth."
                                                },
                                "level_titles" : ["Bravo", "Rutterskin", "Waghalter", "Murderer", "Thug", "Killer", "Cutthroat", "Executioner", "Assassin"]
                    },
                    "bandit" : {"proficiencies" : ["intimidation", "barter", "tactics"],
                                "features" : {"Cheap Shot" : "Ranged crit widens to 19-20.",
                                              "Wound Licker" : "+4 HP",
                                              "Barker" : "Gain advantage to intimidation checks.",
                                              "Bamboozle" : "Gain advantage to trick authorities.",
                                              "Ambush" : "You win initiative on 3-6 for the first round of combat.",
                                              "How Do You Do, Fellow Monsters?" : "+2 to reaction rolls for 'Monsters'.",
                                              "I Took It From That Guy" : "You may wear chain and plate armor.",
                                              "Silver Tongue" : "Gain advantage to charm checks."
                                              }, 
                                "level_titles" : ["Outlaw", "Pickpocket", "Brigand", "Bandit", "Raider", "Pillager", "Marauder", "Plunderer", "Bandit Lord"]
                    },
                    "pirate" : {"proficiencies" : ["sailing", "intimidation", "acrobatics"],
                                "features" : {"Nimble Swimmer" : "Light armor does not affect swimming speed.",
                                              "Captain Of The People" : "Command complete respect of followers, may act as ship Captain.",
                                              "Star's Intuition" : "Navigate without instruments.",
                                              "Swill And Parlay" : "Gain advantage on intimidation checks.",
                                              "Boarding Orders" : "Allies gain initiative while boarding, and suffer no boarding penalties.",
                                              "Dastard Presence" : "Enemies subtract your CHA mod from their morale checks."
                                            },
                                "level_titles" : ["Swabbie", "Seaman", "Privateer", "Buccaneer", "Swashbuckler", "Vandal", "Marauder", "Plunderer", "Pirate Lord"]
                    },
                    "thief" : {"proficiencies" : ["infiltration", "athletics", "investigation"],
                                "features" : {"Appraisal" : "Always know the value of an item.",
                                              "Locksmith" : "Advantage to lockpicking.",
                                              "Climber" : "Gain a natural climbing speed.",
                                              "Tripster" : "Advantage versus traps.",
                                              "Lifter" : "+4 max load",
                                              "Lightfoot" : "Stealth at full speed.",
                                              "Uncanny Dodge" : "Quick Action; trap and area damage is halved.",
                                              "Scriptolirist" : "Real all mundane text",
                                              "Specialization" : "+3 to three checks of your choice.",
                                              "I Can Read That" : "Gain use of spell scrolls."
                                            },
                                "level_titles" : ["Cutpurse", "Pickpocket", "Sneak", "Burglar", "Robber", "Looter", "Lootmaster", "Master Thief", "Thief Lord"]
                    },
                    "scarsan" : {"proficiencies" : ["esoterica", "sleight of hand", "sarric knowledge"],
                                "features" : {"Negation" : "1 in 10 chance to negate any magic effect.",
                                              "Exploit Vulnerability" : "Quick Action; make esoterica check against your target of DC 10 + target's hit dice. If successful, target is vulnerable to your neck attack. Proficiency uses per fight.",
                                              "Sartor Slayer" : "+5 damage to sartors while using rounded weapons.",
                                              "Scarsan's Skin" : "Auto-detect magic.",
                                              "Studied" : "Gain advantage on esoterica checks.",
                                              "Delicate Archivist" : "Scrolls you fail to cast are not destroyed half the time.",
                                              "The Enemy's Weapon" : "Learn 1 first level Arcanist spell.",
                                              "Talisman" : "Mimic ability of a slain creature by crafting a talisman. You may have your proficiency number of talismans."
                                            },
                                "level_titles" : ["Scarless", "Trickcast", "Scourger", "Ringbleid", "Gembane", "Siphon", "Mythbreaker", "Scarsan", "Peerless Scarsan"]
                    },
}
            },

                "level_features" : {1 : "Rogue archetype, Backstab, starting HP, rogue equipment",
                                    2 : "Stealth attempt as quick action",
                                    3 : "Archetype feature",
                                    4 : "+1 to one ability score, read language 80%",
                                    5 : "Quick action, halve damage from one hit",
                                    6 : "+1 to one ability score",
                                    7 : "Archetype feature",
                                    8 : "+1 to one ability score",
                                    9 : "Prof. bonus doubled for archetype checks",
            }
                                    },

