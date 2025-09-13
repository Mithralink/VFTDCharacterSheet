"""Class and Archetypes for the Warrior Class"""
from character import Character
import random


class Warrior(Character):
    def __init__(self, name: str, ability_scores : int, level : int, character_race : str, character_class : str, hit_points: int, mods, sanity, grit, prof, hit_dice, archetype, spirit_bond=None):
        super().__init__(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice, archetype, spirit_bond)



        if self.hit_points == "":
            chosen_hit_dice = max(self.hit_dice[0], min(6, self.hit_dice[1]))
            self.hit_points = chosen_hit_dice + self.mods[2]
            if self.level > 1:
                for i in range(self.level):
                    self.hit_points += random.randint(1, chosen_hit_dice) + self.mods[2]



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
        

    class_level_features = {
            "warrior": {
                "archetype" : {
                    "barbarian" : {"proficiencies" : ["intimidation", "endurance", "travel"],
                                "features" : {"Hearty" : "+8 permanent HP.",
                                              "Visceral" : "Melee crit range expands to 19-20.",
                                              "Intimidating" : "Gain advantage to intimidation checks.",
                                              "Swift" : "Gain +10 feet to movement speed.",
                                              "Too Mad To Die" : "Gain +2 Grit.",
                                              "Rage" : "Gain +3 to all damage dealt, -2 AC.",
                                              "Truestrike" : "Gain the ability to strike invulnerable foes."
                                            },
                    },
                    "caestus" : {"proficiencies" : ["intimidation", "deception", "profane magic"],
                                "features" : {"Lightfooted" : "Gain +1 to light armor, and take no movement penalty in light armor.",
                                              "Flurry of Blows" : "Quick Action; make an unarmed attack. +1 to all unarmed attacks.",
                                              "Arcane" : "Learn 1 first level Arcane spell.",
                                              "Seventeenth Sense" : "Auto-detect magic.",
                                              "Blunt" : "+2 to caestus, flails, nunchucks, and quarterstaves. Flails, nunchucks, and quarterstaves count as unarmed for you.",
                                              "Reliant" : "Scrolls you fail to cast are not destroyed half the time.",
                                              "Repulse" : "Turn the Veilish as Zealot.",
                                              "Stunt" : "Gain advantage to all stunts."
                                            },
                    },
                    "fighter" : {"proficiencies" : ["medicine", "engineering", "diplomacy"],
                                "features" : {"Defensive" : "+1 to AC permanently.",
                                              "Warrior Diplomat" : "Gain advantage to diplomacy checks.",
                                              "True Edge" : "+1 damage to all attacks.",
                                              "Second Wind" : "Regain one third of your max HP once per day.",
                                              "Orders" : "Movement; an ally my take an active action. You may issue one order per round.",
                                              "Action Surge" : "Once per day, take two active actions.",
                                              "Reliable Equipment" : "+2 DUR to armor and weapons.",
                                              "Will of the Warrior" : "Gain +2 Grit.",
                                              "Master Warrior" : "Gain any archetype feature from any Warrior archetype.",
                                              "Weapon Specialization" : "Choose one class of weapons and gain +2 to that class, and -1 to all other weapons."
                                            },
                    },
                    "knight" : {"proficiencies" : ["horsemanship", "honor", "inspiration"],
                                "features" : {"Duelist" : "Target an opponent, deal +2 damage in a duel.",
                                              "Cavalry Unit" : "Mounted allies are immune to fear.",
                                              "Dutious Leader" : "Allies gain advantage on morale checks.",
                                              "Skybound" : "Forfeit the use of ranged weapons and gain the ability to train flying mounts of HD equal to your level.",
                                              "Guardian" : "Tank a hit meant for an ally, and take half damage.",
                                              "Visor" : "Gain advantage against illusions and mind control effects.",
                                              "Defensive" : "Gain +1 to AC permanently.",
                                              "In Shining Armor" : "+2 to AC so long as your armor is clean.",
                                              "Diplomat" : "Gain advanatage to diplomacy.",
                                              "Polarizing" : "+2/-2 to reaction rolls of same/opposing spirit bond."
                                            },
                    },
                    "ward" : {"proficiencies" : ["discipline", "leadership", "spirituality"],
                                "features" : {"Undeniable" : "Gain +2 Grit.",
                                              "Demanding Loyalty" : "+4 to max followers.",
                                              "Hirelings" : "Hire mercenaries and henchment at half the cost.",
                                              "Rally" : "Active Action; grant allies your level in temp HP, once per fight.",
                                              "Convinced" : "Mercenaries will follow you into dungeons.",
                                              "Off-hand Claws" : "Quick Action; deal 2d4 damage to enemy that hits you in melee, so long as your off-hand wields a claw weapon.",
                                              "Respected" : "Command complete respect of followers, +2 to allied morale.",
                                              "Orders" : "Movement; an ally my take an active action. You may issue one order per round.",
                                              "Trance of Man and Steel" : "Carry a Teurthan chime; enter a trance for one round and gain +4 to attack and damage rolls, but your grit is set to 0 for the round. Once per turn.",
                                              "Not One Step Back" : "If any allies fail a morale test, you may execute one follower to succeed instead."
                                            },
                    },
                    "pirate" : {"proficiencies" : ["sailing", "intimidation", "acrobatics"],
                                "features" : {"Fish In Water" : "Light armor does not affect swim speed.",
                                              "Captain" : "Command complete respect of followers, may act as ship Captain.",
                                              "Intuition" : "4 in 6 to navigate without instruments.",
                                              "Intimidating" : "Gain advantage to indimidation checks.",
                                              "Boarding" : "Allies gain initiative while boarding, and suffer no boarding penalties.",
                                              "Scallywag" : "Enemies subtact your CHA mod from their morale checks.",
                                              "Panache" : "Style on your opponents and gain +2 to your next hit/damage, or +4 versus stunned enemies.",
                                              "Rope Pull" : "Gain advantage to stunt checks.",
                                              "Sar Diffusion" : "Make a second shot with an arcstria at -4, proficiency times a day.",
                                              "Small Arms" : "+1 to small arms arcstria."
                                            },
                    },
                    "ranger" : {"proficiencies" : ["wilderness", "creatures", "perception"],
                                "features" : {"Conditioned" : "Ignroe weather conditions.",
                                              "Tracker" : "Gain advantage to tracking and hunting.",
                                              "Stable Step" : "Ignore difficult terrain.",
                                              "Monsterologist" : "Gain advantage to monster information checks.",
                                              "Precision" : "Ranged crit range expands to 19-20.",
                                              "Well Rested" : "Only require half of normal sleep and rest.",
                                              "Camouflaged" : "Gain advanatage to stealth checks.",
                                              "Minotauran" : "Cannot become lost.",
                                              "Versed" : "Gain 1 first level Druidic spell.",
                                              "Scrupulous" : "Gain 1 first level Arcanist spell."
                                            },
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
                    },
                    "witcher" : {"proficiencies" : ["monsters", "senses", "alchemy"],
                                "features" : {"Mutant's Eyes" : "Double perception proficiency.",
                                              "Weakness" : "+5 damage to studied monster.",
                                              "Alchemist" : "Gain advantage to alchemy checks.",
                                              "Hunter" : "Gain advantage to track or hunt.",
                                              "Toxicology" : "Craft custom blade oils.",
                                              "Monsterologist" : "Gain advantage to monster information checks.",
                                              "Simple Sartor" : "Gain 1 first level Arcanist spell.",
                                              "Prolification" : "Gain 1 first level Selven spell."
                                            },
                    },
                            },
                "level_features" : {1 : "Warrior archetype, starting HP, warrior equipment",
                                    2 : "Melee counter-attack, quick action, 2 per fight",
                                    3 : "Archetype feature",
                                    4 : "+1 to one ability score, +1 to follower morale",
                                    5 : "Two attacks per active action",
                                    6 : "+1 to one ability score, charging forces Morale check",
                                    7 : "Archetype feature",
                                    8 : "+1 to one ability score, detect unseen foes within 30’",
                                    9 : "3 attacks per active action",
                },
                                    },
    }
