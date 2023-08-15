from Character import Character
import random
class Races(Character):

    player  = Character()
    
    # List of races
    races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]
    #List of subraces
    dragon_subraces = ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White", "Hill"]
    dwarf_subraces = ["Hill", "Mountain"] 
    elvish_subraces = ["High", "Wood", "Drow"]
    gnome_subraces = ["Forest", "Rock"]
    halfling_subraces = ["Lightfoot", "Stout"]
    tiefling_subraces = ["Asmodeus", "Baalzebul", "Dispater", "Fierna", "Glasya", "Levistus", "Mammon", "Mephistopheles", "Zariel"] 

    # Constructor
    def __init__(self) -> None:
        super().__init__()
        
    # Functionality for displaying races
    def display_race(self):
        print("-------------------Races-------------------\n1. Dragonborn\n2. Dwarf\n3. Elf\n4. Gnome\n5. Half-Elf\n6. Halfling\n7. Half-Orc\n8. Human\n9. Tiefling\n-------------------------------------------")
        player_race = input("Please enter your character's race: ")
        player_strength = 0
        player_dexterity = 0
        player_constitution = 0
        player_intelligence = 0
        player_wisdom = 0
        player_charisma = 0  
        Races.player.set_character_race(player_race)
        Races.player.get_character_race()
        while player_race not in Races.races:
            print("Invalid input. Please try again.")
            player_race = input("Please enter your character's race: ")
            Races.player.set_character_race(player_race)
            Races.player.get_character_race()
        else:
            match player_race:
                case "Dragonborn":
                    print("-----------------Sub-Races----------------\n1. Black\n2. Blue\n3. Brass\n4. Bronze\n5. Copper\n6. Gold\n7. Green\n8. Red\n9. Silver\n10. White\n-------------------------------------------")
                    character_subrace = input("Please enter your character's subrace: ")
                    while character_subrace not in Races.dragon_subraces:
                        print("Invalid input. Please try again.")
                        character_subrace = input("Please enter your character's subrace: ")
                    else:
                        Races.player.set_character_subrace(character_subrace)
                        Races.player.get_character_subrace()
                case "Dwarf":
                    print("-----------------Sub-Races----------------\n1. Hill\n2. Mountain\n-------------------------------------------")
                    character_subrace = input("Please enter your character's subrace: ")
                    while character_subrace not in Races.dwarf_subraces:
                        print("Invalid input. Please try again.")
                        character_subrace = input("Please enter your character's subrace: ")
                    else:
                        Races.player.set_character_subrace(character_subrace)
                        Races.player.get_character_subrace()
                case "Elf":
                    print("-----------------Sub-Races----------------\n1. High\n2. Wood\n3. Drow\n-------------------------------------------")
                    character_subrace = input("Please enter your character's subrace: ")
                    while character_subrace not in Races.elvish_subraces:
                        print("Invalid input. Please try again.")
                        character_subrace = input("Please enter your character's subrace: ")
                    else:
                        Races.player.set_character_subrace(character_subrace)
                        Races.player.get_character_subrace()            
                case "Gnome":
                    print("-----------------Sub-Races----------------\n1. Forest\n2. Rock\n-------------------------------------------")
                    character_subrace = input("Please enter your character's subrace: ")
                    while character_subrace not in Races.gnome_subraces:
                        print("Invalid input. Please try again.")
                        character_subrace = input("Please enter your character's subrace: ")
                    else:
                        Races.player.set_character_subrace(character_subrace)
                        Races.player.get_character_subrace()  
                case "Half-Elf":
                    print("-----------------Sub-Races----------------\n1. High\n2. Wood\n3. Drow\n-------------------------------------------")
                    character_subrace = input("Please enter your character's subrace: ")
                    while character_subrace not in Races.elvish_subraces:
                        print("Invalid input. Please try again.")
                        character_subrace = input("Please enter your character's subrace: ")
                    else:
                        Races.player.set_character_subrace(character_subrace)
                        Races.player.get_character_subrace()  
                case "Halfling":
                    print("-----------------Sub-Races----------------\n1. Lightfoot\n2. Stout\n-------------------------------------------")
                    while character_subrace not in Races.halfling_subraces:
                        print("Invalid input. Please try again.")
                        character_subrace = input("Please enter your character's subrace: ")
                    else:
                        Races.player.set_character_subrace(character_subrace)
                        Races.player.get_character_subrace()                 
                case "Half-Orc":
                    pass
                case "Human":
                    pass
                case "Tiefling":
                    print("-----------------Sub-Races----------------\n1. Asmodeus\n2. Baalzebul\n3. Dispater\n4. Fierna\n5. Glasya\n6. Levistus\n7. Mammon\n8. Mephistopheles\n9. Zariel\n-------------------------------------------")
                    while character_subrace not in Races.tiefling_subraces:
                        print("Invalid input. Please try again.")
                        character_subrace = input("Please enter your character's subrace: ")
                    else:
                        Races.player.set_character_subrace(character_subrace)
                        Races.player.get_character_subrace()           
                case _:
                    print("Invalid selection. Please try again.")

    def roll_for_stats(self):
        set1_roll1 = random.randrange(1,6)
        set1_roll2 = random.randrange(1,6)
        set1_roll3 = random.randrange(1,6)
        set1_roll4 = random.randrange(1,6)

        set2_roll1 = random.randrange(1,6)
        set2_roll2 = random.randrange(1,6)
        set2_roll3 = random.randrange(1,6)
        set2_roll4 = random.randrange(1,6)

        set3_roll1 = random.randrange(1,6)
        set3_roll2 = random.randrange(1,6)
        set3_roll3 = random.randrange(1,6)
        set3_roll4 = random.randrange(1,6)

        set4_roll1 = random.randrange(1,6)
        set4_roll2 = random.randrange(1,6)
        set4_roll3 = random.randrange(1,6)
        set4_roll4 = random.randrange(1,6)

        set5_roll1 = random.randrange(1,6)
        set5_roll2 = random.randrange(1,6)
        set5_roll3 = random.randrange(1,6)
        set5_roll4 = random.randrange(1,6)

        set6_roll1 = random.randrange(1,6)
        set6_roll2 = random.randrange(1,6)
        set6_roll3 = random.randrange(1,6)
        set6_roll4 = random.randrange(1,6)

        ability_score1 = [set1_roll1,set1_roll2,set1_roll3,set1_roll4]
        print(ability_score1)
        ability_score1.sort(reverse=True)
        sum_abilityscore1 = sum(ability_score1[:3])

        ability_score2 = [set2_roll1,set2_roll2,set2_roll3,set2_roll4]
        print(ability_score2)
        ability_score2.sort(reverse=True)
        sum_abilityscore2 = sum(ability_score2[:3])
        
        ability_score3 = [set3_roll1,set3_roll2,set3_roll3,set3_roll4]
        print(ability_score3)
        ability_score3.sort(reverse=True)
        sum_abilityscore3 = sum(ability_score3[:3])

        ability_score4 = [set4_roll1,set4_roll2,set4_roll3,set4_roll4]
        print(ability_score4)
        ability_score4.sort(reverse=True)
        sum_abilityscore4 = sum(ability_score4[:3])

        ability_score5 = [set5_roll1,set5_roll2,set5_roll3,set5_roll4]
        print(ability_score5)
        ability_score5.sort(reverse=True)
        sum_abilityscore5 = sum(ability_score5[:3])

        ability_score6 = [set6_roll1,set6_roll2,set6_roll3,set6_roll4]
        print(ability_score6)
        ability_score6.sort(reverse=True)
        sum_abilityscore6 = sum(ability_score6[:3])

        list_of_rolls = [sum_abilityscore1,sum_abilityscore2,sum_abilityscore3,sum_abilityscore4,sum_abilityscore5,sum_abilityscore6]
        list_of_rolls = [int(i) for i in list_of_rolls]
        print(list_of_rolls)

        print('Time to assign your ability score.')
        player_strength = input('Assign a score to your strength: ')
        player_strength = int(player_strength)
        while player_strength not in list_of_rolls:
            print('Not a valid input. Pick a number from the list of rolls')
            print(list_of_rolls)
            player_strength = input()
        else:
            Races.player.set_strength(player_strength)
            Races.player.get_strength()

        list_of_rolls.remove(player_strength)
        print(list_of_rolls)     
