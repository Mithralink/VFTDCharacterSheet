"""Class and Archetypes for the Zealot Class"""
from character import Character
import random


class Zealot(Character):
    def __init__(self, name: str, ability_scores : int, level : int, character_race : str, character_class : str, hit_points: int, mods, sanity, grit, prof, hit_dice, spirit_bond=None):
        super().__init__(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice, spirit_bond)



        if self.hit_points == "":
            chosen_hit_dice = max(self.hit_dice[0], min(6, self.hit_dice[1]))
            self.hit_points = chosen_hit_dice + self.mods[2]
            if self.level > 1:
                for i in range(self.level):
                    self.hit_points += random.randint(1, chosen_hit_dice) + self.mods[2]



    class_level_features = {
            "zealot": {
                "archetype" : {
                    "silean" : {"proficiencies" : ["healing", "politics", "selven magic"],
                                "features" : {"Healer" : "Healing grants +2 HP",
                                              "Anathema" : "+4 damage vesus Bassyric types.",
                                              "Forinthry" : "Allies gain advantage vesus injury.",
                                              "Golden Bludgeon" : "Forfeit use of edged weapons, gain +2 spellcasting.",
                                              "Bless" : "Quick Action; grant an ally +2 on their next physical check.",
                                              "Guardian" : "Quick Action; Take a hit meant ofr an ally, take half damage.",
                                              "Smite" : "Quick Action; mark a target as a heretic. You may add your healing d6s to damage rolls against that target.",
                                              "Corporeal Sartorcraft" : "Gain access to the Necromancy spell list."
                                            },
                    },
                    "crusader" : {"proficiencies" : ["tactics", "strategy", "politics"],
                                "features" : {"Settler" : "Construct strongholds for half the price.",
                                              "Martial" : "Gain martial weapon proficiency.",
                                              "Founder" : "Gain 5d6 + CHA utterly loyal troops once a stronghold has finished contruction.",
                                              "Defensive" : "Permanent +1 to AC.",
                                              "Leader" : "+4 max followers.",
                                              "Beacon of Zeal" : "Banners and shields with the emblem of your faith can glow as Continual Light, dispelling darkness and granting disadvantage on enemy ranged attacks and advantage to allied morale checks.",
                                            },
                    },
                    "bassyric" : {"proficiencies" : ["profane magic", "eldrich lore", "intimidation"],
                                "features" : {"Indimidating" : "Gain advantage to indimidation checks.",
                                              "Corporeal Anathema" : "+4 damage vesus Silean types.",
                                              "Synaptic Link" : "Once per week, choose a creature to link minds with completely. Make an INT check vesus unwilling creatures of DC 10 + hit dice. Allows control both ways.",
                                              "Sacrifice" : "Deal damage to yourself. Your next hit deals twice that amount.",
                                              "Darksight" : "See normally in complete darkness. Bright light becomes blinding.",
                                              "Stable Mind" : "Gain advantage to sanity checks.",
                                              "Sane" : "+2 sanity.",
                                              "Perpetual Consciousness" : "No need to sleep, though you still need to rest."
                                            },
                    },
                    "desert fean" : {"proficiencies" : ["wilderness", "creatures", "druidic magic"],
                                "features" : {"Whisper of the Dune" : "Speak with the sands.",
                                              "Traceless" : "Leave no trail.",
                                              "Antivenom" : "Immune to poisons.",
                                              "Sunwalker" : "No need to eat.",
                                              "Temporal Control" : "While wearing no armor, you gain temporal control over cantrips, and one leveled spell per day.",
                                              "Wild" : "Gain advantage to wilderness checks.",
                                              "Submerge" : "Always succeed hiding in sand.",
                                              "Sandwalker" : "Gain resistance to heat.",
                                              "Dunes of the Comet" : "Gain access to the Arcanist spell list.",
                                              "Dunes of Starlight" : "Gain access to the Necromancy spell list.",
                                              "Dunes of Gold" : "Gain access to the Selven spell list as Zealot.",
                                              "Dunes of Flame" : "Gain access to the Fire Elementalist spell list."
                                            },
                    },
                    "vulkjoran" : {"proficiencies" : ["persuasion", "insight", "crafting"],
                                "features" : {"Repulse" : "Roll 3d6 for Turn Veilish, and take the best two.",
                                              "Healer" : "Action; heal an ally for 1d6 + WIS mod HP.",
                                              "Craftsman" : "Gain advantage to crafting checks.",
                                              "Design Refinement" : "All of your equipment gains +2 DUR.",
                                              "Wise Words" : "Your party gains your WIS mod temp HP after resting.",
                                              "Efficient Crafter" : "You may craft items at half cost and time.",
                                              "Mythralcraft" : "You may craft sartor crystals from raw Mythral.",
                                              "Verbose" : "Gain advantage to diplomacy checks.",
                                              "Changebringer" : "Choose one weapon at dawn. This weapon becomes engulfed in flame until the sun sets.",
                                              "Ritual of Change" : "1 Turn ritual; choose one item of Load < Level. Convert this item to any mundane item of the same load. Can restore DUR. Once per day.",
                                            },
                    },
                    "lost akathian" : {"proficiencies" : ["politics", "nature", "pagan magic"],
                                "features" : {"Witchdoctor" : "Gain advantage to folk magic",
                                              "Rustic Tools" : "+1 to axes of all types.",
                                              "Signs" : "Read omens.",
                                              "Warding" : "Gain advantage to resist magic.",
                                              "Ancestral Fury" : "Invoke an ancestor by name and gain +2 to your next check.",
                                              "Barbaric" : "Choose one Barbarian feature.",
                                              "Zealous Strikes" : "Gain a second attack per active action."
                                            },
                    },
                    "oracle" : {"proficiencies" : ["divination", "charm", "diplomacy"],
                                "features" : {"Augury" : "Foresee the next three d12 results on random encounter checks.",
                                              "Unarmored" : "Unarmored AC is 12 + WIS mod.",
                                              "Doomwyrd" : "Learn your Doomwyrd, the phrase that immediately precedes your doom.",
                                              "Divine Intervention" : "Learn one sixth level Arcanist spell to cast once per month.",
                                              "Walking Stick" : "+2 to staves.",
                                              "Charmer" : "Add Charm Person to your spell list."
                                            },
                    },
                    "apostle of korvyre" : {"proficiencies" : ["death", "scripture", "intimidation"],
                                "features" : {"Lirist" : "Read all mundane text.",
                                              "Scribe" : "Scribing time and cost is halved.",
                                              "Way of the Quill" : "+1 to morningstars.",
                                              "The Magic Words" : "Read Magic is always active.",
                                              "Relics of Insulation" : "Wear 500g of copper jewelry and rings and gain +1 to resist spells. You may take this feature up to three times, each time requiring 1000g more in copper jewelry to gain the benefit again.",
                                              "Dictation" : "Detail in writing a recent death while resting and gain +2 to checks and saves for the rest of the day."
                                            },
                    },
                            },
                "level_features" : {1 : "Zealot archetype, starting HP, Turn the Veilish, 3 Selven cantrips, zealot equipment",
                                    2 : "Selven spellcasting; heal 1d6/level once per rest, touch, active action",
                                    3 : "Archetype feature",
                                    4 : "+1 to one ability score",
                                    5 : "Innately sense creatures of chosen spirit bond",
                                    6 : "+1 to one ability score",
                                    7 : "Archetype feature",
                                    8 : "+1 to one ability score",
                                    9 : "Enemies roll morale at disadvantage",
                },
                                    },
    }
