"""Use of Character sheet stats, and inventory database loading."""

from character import Character
from classwarrior import Warrior
from classrogue import Rogue
from classsartor import Sartor
from classzealot import Zealot
from classdungeoneer import Dungeoneer
import configparser
import os

#decides which class to generate a character with
class CharacterCreator:
    def create_character(self, name: str, ability_scores : int, level : int, character_race : str, character_class : str, hit_points: int, mods, sanity, grit, prof, hit_dice, spirit_bond=None):
        if character_class == "":
            character_class = Character.generate_class(self)
        if character_class.lower() == "warrior":
            return Warrior(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice, spirit_bond)
        elif character_class.lower() == "rogue":
            return Rogue(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice, spirit_bond)
        elif character_class.lower() == "sartor":
            return Sartor(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice, spirit_bond)
        elif character_class.lower() == "zealot":
            return Zealot(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice, spirit_bond)
        elif character_class.lower() == "dungeoneer":
            return Dungeoneer(name, ability_scores, level, character_race, character_class, hit_points, mods, sanity, grit, prof, hit_dice, spirit_bond)
        else:
            raise ValueError(f"Invalid character type: {character_class}")

# creation = CharacterCreator()
# warriorman = creation.create_character("wowio", [], "",  "", "", "", "", "", "", "", "", "")

def load_item_db(config_files):
    """Load item database from config files."""
    item_db = {}
    for file in config_files:
        config = configparser.ConfigParser()
        config.read(file)
        for section in config.sections():
            item_db[section] = dict(config.items(section))
    return item_db

config_files = [
    "configs/config_armor.ini",
    "configs/config_armor_heavy.ini",
    "configs/config_armor_light.ini",
    "configs/config_martial_melee.ini",
    "configs/config_martial_ranged.ini",
    "configs/config_simple_melee.ini",
    "configs/config_simple_ranged.ini"
]
item_db = load_item_db(config_files)
