"""Main ability score calulations."""
# Lay out stat table and modifier.
# Choose race, which guarantees certain stats and proficiencies.
# Roll remaining stats in order.
# Display character stats.

from die import roll_dsix


ability_scores = {18 : +4,
                 17: +3, 16: +3,
                 15: +2, 14: +2,
                 13: +1, 12: +1,
                 11: +0, 10: +0, 9: +0,
                 8:  -1, 7:  -1, 
                 6:  -2, 5:  -2,
                 4:  -3, 3:  -3,
                 2:  -4, 1:  -4,}

class_hitdice = {"warrior" : 8,
                   "rogue" : 4,
                   "zealot" : 6,
                   "sartor" : 4,
                   "dungeoneer" : 6}



character_stats = ["STR =", "DEX =", "CON =", "WIS =", "INT =", "CHA ="]

character_class = ["warrior", "rogue", "zealot", "sartor", "dungeoneer"]

character_race = ["bassyrikin", "human", "fjoran", "shaelarae", "talii"]



def manual_abilities():
    """Manual inputs for all ability scores. Must input numbers between 1 and 18."""
    while True:
        race_choice = input("Choose character race "
        "(Bassyrikin, Human, Fjoran, Shaelarae, Talii): ").lower()
        if race_choice in character_race:
            break
        else:
            print("Please try again.")
            # input strength
    while True:

        if race_choice == "talii":
            STR = 13
            break

        STR = int(input("Enter your Strength ability score: "))
        if STR in range(1, 19):
            character_stats.insert(9, ability_scores.get(STR))
            print(f"Intelligence score and modifier: {STR}: {ability_scores.get(STR)}")
            break
        else:
            print("Enter a number between 1 and 18.")

            # input dexterity
    while True:

        if race_choice == "shaelarae":
            DEX = 13
            break

        DEX = int(input("Enter your Dexterity ability score: "))
        if DEX in range(1, 19):
            character_stats.insert(9, ability_scores.get(DEX))
            print(f"Intelligence score and modifier: {DEX}: {ability_scores.get(DEX)}")
            break
        else:
            print("Enter a number between 1 and 18.")

            # input constitution
    while True:

        if race_choice == "fjoran" or race_choice == "talii":
            CON = 13
            break

        CON = int(input("Enter your Constitution ability score: "))
        if CON in range(1, 19):
            character_stats.insert(9, ability_scores.get(CON))
            print(f"Intelligence score and modifier: {CON}: {ability_scores.get(CON)}")
            break
        else:
            print("Enter a number between 1 and 18.")

            # input wisdom
    while True:
        WIS = int(input("Enter your Wisdom ability score: "))
        if WIS in range(1, 19):
            character_stats.insert(7, ability_scores.get(WIS))
            print(f"Wisdom score and modifier: {WIS}: {ability_scores.get(WIS)}")
            break
        else:
            print("Enter a number between 1 and 18.")

            # input intelligence
    while True:

        if race_choice == "shaelarae" or race_choice == "fjoran":
            INT = 13
            break

        INT = int(input("Enter your Intelligence ability score: "))
        if INT in range(1, 19):
            character_stats.insert(9, ability_scores.get(INT))
            print(f"Intelligence score and modifier: {INT}: {ability_scores.get(INT)}")
            break
        else:
            print("Enter a number between 1 and 18.")

            # input charisma
    while True:
        CHA = int(input("Enter your Charisma ability score: "))
        if CHA in range(1, 19):
            character_stats.insert(11, ability_scores.get(CHA))
            print(f"Charisma score and modifier: {CHA}: {ability_scores.get(CHA)}")
            break
        else:
            print("Enter a number between 1 and 18.")

    return [STR, CON, DEX, WIS, INT, CHA, race_choice]



def manual_character_sheet():
    """Print the character sheet with stats generated after ability score inputs."""
    while True:
        level = int(input("Enter your character's level: "))
        if level > 0:
            break
        else: print("Please enter a number.")
    while True:
        class_choice = input("Choose character class "
        "(Dungeoneer, Rogue, Warrior, Sartor, Zealot): ").lower()
        if class_choice in character_class:
            break
        else:
            print("Please try again.")


    manual_stats = manual_abilities()

    race_choice = manual_stats[6]
    strength = manual_stats[0]
    constitution = manual_stats[1]
    dexterity = manual_stats[2]
    wisdom = manual_stats[3]
    intelligence = manual_stats[4]
    charisma = manual_stats[5]

    hit_dice_amount = level
    starting_gold = (3 * roll_dsix()) * 10

    hit_dice = class_hitdice.get(class_choice)
    if class_choice == ["sartor", "rogue"] and race_choice == ["talii", "fjoran"] and hit_dice < 6:
        hit_dice = 6
    if class_choice == "warrior" and race_choice =="shaelarae":
        hit_dice = 6

    max_load = strength

    proficiency = round(level / 4) + 1
    if proficiency > 5:
        proficiency = 5

    grit = ability_scores.get(constitution) + proficiency

    sanity = ability_scores.get(intelligence) + 3
    if sanity < 1:
        sanity = 1

    print(f"You're a {race_choice} {class_choice}!")
    print(f"You are level {level} and have {hit_dice_amount}d{hit_dice} Hit Dice!")
    print(f"You have {starting_gold} Gold Pieces")
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
