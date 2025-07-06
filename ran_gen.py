"""Random generation for the individual races."""
#imports
import random
from statcalculation import ability_scores
from statcalculation import character_stats
from statcalculation import character_race
from statcalculation import character_class
from statcalculation import class_hitdice
from die import roll_dsix


# random generation for every race
# humans and bassyrikin identical, not currently able to swap stats.
def random_human():
    """generates human or bassyrikin stats, should allow two numbers to be swapped."""
    strength = 3 * roll_dsix()
    character_stats.insert(1, ability_scores.get(strength))
    # ability modifier is stored in character stats
    dexterity = 3 * roll_dsix()
    character_stats.insert(3, ability_scores.get(dexterity))

    constitution = 3 * roll_dsix()
    character_stats.insert(5, ability_scores.get(constitution))

    wisdom = 3 * roll_dsix()
    character_stats.insert(7, ability_scores.get(wisdom))

    intelligence = 3 * roll_dsix()
    character_stats.insert(9, ability_scores.get(intelligence))

    charisma = 3 * roll_dsix()
    character_stats.insert(11, ability_scores.get(charisma))

    return [strength, constitution, dexterity, wisdom, intelligence, charisma]





def random_fjoran():
    """Generate random stats for a fjoran. 2d6 for all,
    but CON and INT are 13."""
    constitution = 13
    character_stats.insert(5, ability_scores.get(constitution))

    intelligence = 13
    character_stats.insert(9, ability_scores.get(intelligence))

    strength = 2 * roll_dsix() + 3
    character_stats.insert(1, ability_scores.get(strength))

    dexterity = 2 * roll_dsix() + 3
    character_stats.insert(3, ability_scores.get(dexterity))

    wisdom = 2 * roll_dsix() + 3
    character_stats.insert(7, ability_scores.get(wisdom))

    charisma = 2 * roll_dsix() + 3
    character_stats.insert(11, ability_scores.get(charisma))

    return [strength, constitution, dexterity, wisdom, intelligence, charisma]




def random_shaelarae():
    """Generate random stats for a shaelarae. 2d6 for all,
    but DEX and INT are 13."""
    dexterity = 13
    character_stats.insert(3, ability_scores.get(dexterity))

    intelligence = 13
    character_stats.insert(9, ability_scores.get(intelligence))

    strength = 2 * roll_dsix() + 3
    character_stats.insert(1, ability_scores.get(strength))

    constitution = 2 * roll_dsix() + 3
    character_stats.insert(5, ability_scores.get(constitution))

    wisdom = 2 * roll_dsix() + 3
    character_stats.insert(7, ability_scores.get(wisdom))

    charisma = 2 * roll_dsix() + 3
    character_stats.insert(11, ability_scores.get(charisma))

    return [strength, constitution, dexterity, wisdom, intelligence, charisma]



def random_talii():
    """Generate random stats for a talii. 2d6 for all,
    but STR and CON are 13."""
    strength = 13
    character_stats.insert(1, ability_scores.get(strength))

    constitution = 13
    character_stats.insert(5, ability_scores.get(constitution))

    intelligence = 2 * roll_dsix() + 3
    character_stats.insert(9, ability_scores.get(intelligence))

    dexterity = 2 * roll_dsix() + 3
    character_stats.insert(3, ability_scores.get(dexterity))

    wisdom = 2 * roll_dsix() + 3
    character_stats.insert(7, ability_scores.get(wisdom))

    charisma = 2 * roll_dsix() + 3
    character_stats.insert(11, ability_scores.get(charisma))

    return [strength, constitution, dexterity, wisdom, intelligence, charisma]



def random_character_sheet():
    """Full random character creation function."""

    strength = 0
    constitution = 0
    dexterity = 0
    wisdom = 0
    intelligence = 0
    charisma = 0

    level = int(input("Please choose your level: "))


    while True:
        random_race = input("Would you like a random race? (Y/N) ").upper()
        if random_race == "N" or random_race == "Y":
            break
        else:
            print("Please enter either Y or N.")

    if random_race == "Y":
        race_choice = random.choice(character_race)

    else:
        while True:
            race_choice = input("Choose character race "
            "(Bassyrikin, Human, Fjoran, Shaelarae, Talii): ").lower()
            if race_choice in character_race:
                break
            else:
                print("Please try again.")

    if race_choice == "bassyrikin":
        random_human()
        strength = random_human()[0]
        constitution = random_human()[1]
        dexterity = random_human()[2]
        wisdom = random_human()[3]
        intelligence = random_human()[4]
        charisma = random_human()[5]


    if race_choice == "human":
        random_human()
        strength = random_human()[0]
        constitution = random_human()[1]
        dexterity = random_human()[2]
        wisdom = random_human()[3]
        intelligence = random_human()[4]
        charisma = random_human()[5]


    if race_choice == "fjoran":
        random_fjoran()
        strength = random_fjoran()[0]
        constitution = random_fjoran()[1]
        dexterity = random_fjoran()[2]
        wisdom = random_fjoran()[3]
        intelligence = random_fjoran()[4]
        charisma = random_fjoran()[5]


    if race_choice == "shaelarae":
        random_shaelarae()
        strength = random_shaelarae()[0]
        constitution = random_shaelarae()[1]
        dexterity = random_shaelarae()[2]
        wisdom = random_shaelarae()[3]
        intelligence = random_shaelarae()[4]
        charisma = random_shaelarae()[5]


    if race_choice == "talii":
        random_talii()
        strength = random_talii()[0]
        constitution = random_talii()[1]
        dexterity = random_talii()[2]
        wisdom = random_talii()[3]
        intelligence = random_talii()[4]
        charisma = random_talii()[5]



    while True:
        random_class = input("Would you like a random class? (Y/N): ").upper()
        if random_class == "N" or random_class == "Y":
            break
        else:
            print("Please enter either Y or N.")

    while True:
        if random_class == "N":
            class_choice = input("Choose character class "
            "(Dungeoneer, Rogue, Warrior, Sartor, Zealot): ")
            if class_choice in character_class:
                break
            else:
                print("Please try again.")

        else:
            class_choice = random.choice(character_class)
            break



    hit_dice = class_hitdice.get(class_choice)
    if class_choice == ["sartor", "rogue"] and race_choice == ["talii", "fjoran"] and hit_dice < 6:
        hit_dice = 6
    if class_choice == "warrior" and race_choice =="shaelarae":
        hit_dice = 6

    max_load = strength

    hit_dice_amount = level

    proficiency = round(level / 4) + 1
    if proficiency > 5:
        proficiency = 5

    grit = ability_scores.get(constitution) + proficiency

    sanity = ability_scores.get(intelligence) + 3
    if sanity < 1:
        sanity = 1

    print(f"You're a {race_choice} {class_choice}!")
    print(f"You are level {level} and have {hit_dice_amount}d{hit_dice} Hit Dice!")
    print("------------------------------")
    print("--------ABILITY SCORES--------")
    print("------------------------------")
    print("Ability     Ability Score     Modifier")
    print(f"STR:             {strength}              {ability_scores.get(int(strength))}")
    print(f"DEX:             {dexterity}              {ability_scores.get(dexterity)}")
    print(f"CON:             {constitution}              {ability_scores.get(constitution)}")
    print(f"WIS:             {wisdom}              {ability_scores.get(wisdom)}")
    print(f"INT:             {intelligence}              {ability_scores.get(intelligence)}")
    print(f"CHA:             {charisma}              {ability_scores.get(charisma)}")
    print(f"Proficiency Bonus:  + {proficiency}")
    print(f"Grit: {grit}")
    print(f"Sanity: {sanity}")
    print(f"Max Load: {max_load}")
