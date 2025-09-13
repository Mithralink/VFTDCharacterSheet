"""Class and Archetypes for the Dungeoneer Class"""
from character import Character
import random


class Dungeoneer(Character):
    def __init__(self, name: str, ability_scores : int, level : int, character_race : str, character_class : str, hit_points: int, mods, sanity, grit, prof, hit_dice, archetype, spirit_bond=None):
        super().__init__(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice, archetype, spirit_bond)



        if self.hit_points == "":
            chosen_hit_dice = max(self.hit_dice[0], min(6, self.hit_dice[1]))
            self.hit_points = chosen_hit_dice + self.mods[2]
            if self.level > 1:
                for i in range(self.level):
                    self.hit_points += random.randint(1, chosen_hit_dice) + self.mods[2]


    class_proficiencies = ["traps", "senses", "tools", "engineering", "archetype"]


    class_level_features = {
            "Dungeoneer": {
                "archetype" : {
                    "censerer" : {"proficiencies" : ["senses", "medicine", "healing magic"],
                                "features" : {  "Secret Doors" : "Auto detect secret doors with censer.",
                                                "Medicine" : "Advantage to medical practice.",
                                                "Perception" : "Advantage to perception checks.",
                                                "1st level Selven spell" : "Gain a 1st level Selven spell.",
                                                "Ally Morale" : "Allies have advantage to morale when you censer burns.",
                                                "Censer Healing" : "Healing is doubled when near your burning censer.",
                                                "Turn the Veilish" : "Turn the Veilish as Zealot.",
                                                "Use Spell Scrolls" : "Use spell scrolls."},
                                "level_titles" : ["Smudge", "Wafter", "Smokeologist", "Empiric", "Plaguebreaker", "Incenser", "Smokesight", "Aeromantic", "Scentinal"]
                    },
                    "alchemist" : {"proficiencies" : ["alchemy", "botany", "crafting"],
                                    "features" : {"Potion Crafter" : "Craft potions at half cost and time.",
                                                "Use Spell Scrolls" : "Use spell scrolls using your wisdom.",
                                                "Potion Stowing" : "Stow 10 potions in 1 load slot instead of the standard 5.",
                                                "Alchemical Mastery" : "Gain advantage to alchemy checks.",
                                                "Potion Identification" : "Identify potions by scent instead of taste or touch."},
                                    "level_titles" : ["Mixer", "Brewer", "Distiller", "Fermenter", "Concocter", "Elixirist", "Alchemist", "Grand Alchemist"]
                    },
                    "archaeologist" : {"proficiencies" : ["history", "culture", "investigation"],
                                "features" : {"Identification" : "Identify cursed or enchanted treasure: 1 turn per load.",
                                                "Memorize Pages" : "Perfectly memorize your level in pages of info for your proficiency number of months.",
                                                "Knowledgeable" : "Advantage to knowledge checks.",
                                                "Researcher" : "Research in half the time and cost.",
                                                "Linguist" : "Know INT mod languages.",
                                                "Trap Familiarity" : "Advantage to disable traps.",
                                                "Whip Mastery" : "Expertise in whip and grappling hook use."},
                                "level_titles" : ["Shovel-bum", "Amatur", "Ghouler", "Treasure-hunter", "Curator", "Antiquarian", "Archaeologist", "Doctor of Archaeology", " Professor of Archaeology"]
                    },
                    "barber surgeon" : {"proficiencies" : ["medicine", "finesse", "apothecary"],
                                "features" : {"First Aid" : "Action; use med kit to heal 1d6 + WIS mod HP.",
                                                "Surgeon" : "Advantage to medical practice.",
                                                "Recovery" : "use med kit to recover 1d6 stat points from an Injury.",
                                                "Field Infirmary" : "Set up a med tent, can recover addition 1d6 per level HP each rest.",
                                                "Triage" : "Action; undo all damage taken by an ally last round, 2 med kit charges.",
                                                "Ol' Sawbones" : "When an ally rolls a 1 on Injury table, amputate one limb instead."},
                                "level_titles" : ["Bloodletter", "Barber", "Apothecary", "Leecher", "Practitioner", "Dentist", "Doctor", "Surgeon", "Surgeon General"]
                    },
                    "engineer" : {"proficiencies" : ["excavation", "construction", "demolition"],
                                "features" : {"Reinforcement" : "+2 DUR to party equipment.",
                                                "Make-shifter" : "Advantage to jurry-rigging.",
                                                "Loyalty" : "+2 follower loyalty.",
                                                "Project Management" : "Fortify or excavate an area at double speed.",
                                                "Investigator" : "Advantage to room traps or secrets.",
                                                "Repairer" : "Advantge to repairs.",
                                                "Practical Weaponry" : "Proficient using tools as weapons.",
                                                "You Go First" : "Grant an ally 1d6 temp HP one at a time if they're ahead of you."},
                                "level_titles" : ["Miner", "Tunneler", "Surveyor", "Machinist", "Foreman", "Architect", "Tombcracker", "Cryptraider", "Dungeoneer"]
                    },
                    "expeditioner" : {"proficiencies" : ["tactics", "coordination", "will"],
                                "features" : {"Martial Training" : "Gain martial weapon proficiency.",
                                                "Armored" : "Gain proficiency in plate armor.",
                                                "Breacher" : "Breach doors as a free action",
                                                "Defensive" : "+1 to AC permanently.",
                                                "Efficient Repairs" : "Repair equipment at half cost and time.",
                                                "Hearty" : "+2 Grit Points",
                                                "Martial Training" : "Gain any 1 Warrior archetype feature.",
                                                "Perceptive" : "+4 to perception checks."},
                                "level_titles" : ["Breacher", "Pointman", "Ghouler", "Charger", "Sapper", "Saboteur", "Tombcracker", "Cryptraider", "Expeditioner"]
                    },
                    "explorer" : {"proficiencies" : ["cartography", "wayfinding", "pioneering "],
                                "features" : {"Climber" : "You have a natural climbing speed.",
                                                "Surefooted" : "Ignore difficult terrain,",
                                                "Camouflaged" : "Gain proficiency in stealth,",
                                                "Minotauran Mind" : "Can not become lost",
                                                "Swift" : "Gain +10 ft to movement speed.",
                                                "Veilish Talisman" : "Cast Pass Veilish once a day.",
                                                "Bassyric Ward" : "Cast Protection from Bassyric once a day.",
                                                "Monsterologist" : "Gain advantage to monster knowledge checks.",
                                                "Natural Arcana" : "Gain 1 first level Druidic spell."},
                                "level_titles" : ["Cartographer", "Pioneer", "Scout", "Caver", "Spelunker", "Guide", "Pathfinder", "Explorer", "Wayfinder"]
                    },
                    "field researcher" : {"proficiencies" : ["history", "nature", "investigation"],
                                "features" : {"Necronomicological Understudy" : "Expend sanity to gain 10 to any mental check.",
                                                "Memorization" : "Perfectly memorize your level in pages of info for your proficiency number of months.",
                                                "Knowledgeable" : "Advantage to knowledge checks.",
                                                "Researcher" : "Research in half the time and cost.",
                                                "Linguist" : "Know INT mod languages.",
                                                "Specialist" : "+3 to three fields of research.",
                                                "Diplomat" : "Advantage to diplomacy checks.",
                                                "Good With Instructions" : "Use spell scrolls."},
                                "level_titles" : ["Writ", "Study", "Surveyor", "Supervisor", "Foreman", "Architect", "Document Lead", "Research Lead", "Headmaester"]
                    },
                    "scarsan" : {"proficiencies" : ["history", "sarric knowledge", "sar"],
                                "features" : {"Body Or Mind" : "Expending grit permanently raises sanity max by the amount spent.",
                                                "Seventeenth Sense" : "Auto-detect magic",
                                                "Sarric Patterns" : "Know local Insallir and Ansallir pattern.",
                                                "Insulation" : "Magic items have proficiency less attunement cost.",
                                                "Linguist" : "Know INT mod languages.",
                                                "Antisarric Design" : "+1 to curved weapons.",
                                                "Pang of Mythral" : "Once a day, locate a specific magic effect within hex.",
                                                "Study of Scripts" : "Use spell scrolls."},
                                "level_titles" : ["Scarred", "Oil Wick", "Salt-stabber", "Arch-bleid", "Spell-pick", "Curvedge", "Sartor Sapper", "Scarsan", "Peerless Scarsan"]
                    },
                            },
                "level_features" : {1 : "Dungeoneer archetype, starting HP, dungeoneer equipment,detect and disable treasure traps, hear through doors, pick locks, detect construction tricks, detect room traps.",
                                    2 : "Use tool/consumable as quick action, duration is doubled",
                                    3 : "Archetype feature",
                                    4 : "+1 to one ability score, carry +5 load in inventory",
                                    5 : "Gain one Archetype feature from any Warrior, Rogue, or Dungeoneer archetype",
                                    6 : "+1 to one ability score",
                                    7 : "Archetype feature",
                                    8 : "+1 to one ability score",
                                    9 : "Reliable Talent for class skills",
                },
                                    },
    }
