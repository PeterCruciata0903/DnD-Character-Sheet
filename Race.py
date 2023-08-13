from Character import Character

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