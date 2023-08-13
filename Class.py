from Character import Character

class Player_Class(Character):

    player = Character()
    
    # List of classes
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]   
    # List of subclasses
    barbarian_subclasses = ["Path of the Berserker", "Path of the Totem Warrior"]
    bard_subclasses = ["College of Lore", "College of Valor"]
    cleric_subclasses = ["Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Tempest Domain", "Trickery Domain", "War Domain"]
    druid_subclasses = ["Circle of the Land", "Circle of the Moon"]
    fighter_subclasses = ["Champion", "Battle Master", "Eldritch Knight"]
    monk_subclasses = ["Way of the Open Hand", "Way of Shadow", "Way of the Four Elements"]
    paladin_subclasses = ["Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance"]
    ranger_subclasses = ["Hunter", "Beast Master"]
    rogue_subclasses = ["Thief", "Assassin", "Arcane Trickster"]
    sorcerer_subclasses = ["Draconic Bloodline", "Wild Magic"]
    warlock_subclasses = ["The Archfey", "The Fiend", "The Great Old One"]
    wizard_subclasses = ["School of Abjuration", "School of Conjuration", "School of Divination", "School of Enchantment", "School of Evocation", "School of Illusion", "School of Necromancy", "School of Transmutation"]

    # Constructor
    def __init__(self) -> None:
        super().__init__()
    
    # Function to display the list of classes
    def display_classes(self):
        print("-------------------Class-------------------\n1. Barbarian\n2. Bard\n3. Cleric\n4. Druid\n5. Fighter\n6. Monk\n7. Paladin\n8. Ranger\n9. Rogue\n10. Sorcerer\n11. Warlock\n12. Wizard\n--------------------------------------------")
        player_class = input("Please enter your character's class: ")
        Player_Class.player.set_character_class(player_class)
        Player_Class.player.get_character_class()
        while player_class not in Player_Class.classes:
            print("Invalid input. Please try again.")
            player_class = input("Please enter your character's class: ")
        else:
            match player_class:
                case "Barbarian":
                    print("-----------------Subclass-----------------\n1. Path of the Berserker\n2. Path of the Totem Warrior\n--------------------------------------------")
                    player_subclass = input("Please enter your character's subclass: ")
                    while player_subclass not in Player_Class.barbarian_subclasses:
                        print("Invalid input. Please try again.")
                        player_subclass = input("Please enter your character's subclass: ")
                    else:
                        Player_Class.player.set_character_subclass(player_subclass)
                        Player_Class.player.get_character_subclass()
                case "Bard":
                    print("-----------------Subclass-----------------\n1. College of Lore\n2. College of Valor\n--------------------------------------------")
                    player_subclass = input("Please enter your character's subclass: ")
                    while player_subclass not in Player_Class.bard_subclasses:
                        print("Invalid input. Please try again.")
                        player_subclass = input("Please enter your character's subclass: ")
                    else:
                        Player_Class.player.set_character_subclass(player_subclass)
                        Player_Class.player.get_character_subclass()
                case "Cleric":
                    print("-----------------Subclass-----------------\n1. Knowledge Domain\n2. Life Domain\n3. Light Domain\n4. Nature Domain\n5. Tempest Domain\n6. Trickery Domain\n7. War Domain\n--------------------------------------------")
                    player_subclass = input("Please enter your character's subclass: ")
                    while player_subclass not in Player_Class.cleric_subclasses:
                        print("Invalid input. Please try again.")
                        player_subclass = input("Please enter your character's subclass: ")
                    else:
                        Player_Class.player.set_character_subclass(player_subclass)
                        Player_Class.player.get_character_subclass()
                case "Druid":
                    print("-----------------Subclass-----------------\n1. Circle of the Land\n2. Circle of the Moon\n--------------------------------------------")
                    player_subclass = input("Please enter your character's subclass: ")
                    while player_subclass not in Player_Class.druid_subclasses:
                        print("Invalid input. Please try again.")
                        player_subclass = input("Please enter your character's subclass: ")
                    else:
                        Player_Class.player.set_character_subclass(player_subclass)
                        Player_Class.player.get_character_subclass()
                case "Fighter":
                    print("-----------------Subclass-----------------\n1. Champion\n2. Battle Master\n3. Eldritch Knight\n--------------------------------------------")
                    player_subclass = input("Please enter your character's subclass: ")
                    while player_subclass not in Player_Class.fighter_subclasses:
                        print("Invalid input. Please try again.")
                        player_subclass = input("Please enter your character's subclass: ")
                    else:
                        Player_Class.player.set_character_subclass(player_subclass)
                        Player_Class.player.get_character_subclass()
                case "Monk":
                    print("-----------------Subclass-----------------\n1. Way of the Open Hand\n2. Way of Shadow\n3. Way of the Four Elements\n--------------------------------------------")
                    player_subclass = input("Please enter your character's subclass: ")
                    while player_subclass not in Player_Class.monk_subclasses:
                        print("Invalid input. Please try again.")
                        player_subclass = input("Please enter your character's subclass: ")
                    else:
                        Player_Class.player.set_character_subclass(player_subclass)
                        Player_Class.player.get_character_subclass()
                case "Paladin":
                    print("-----------------Subclass-----------------\n1. Oath of Devotion\n2. Oath of the Ancients\n3. Oath of Vengeance\n--------------------------------------------")
                    player_subclass = input("Please enter your character's subclass: ")
                    while player_subclass not in Player_Class.paladin_subclasses:
                        print("Invalid input. Please try again.")
                        player_subclass = input("Please enter your character's subclass: ")
                    else:
                        Player_Class.player.set_character_subclass(player_subclass)
                        Player_Class.player.get_character_subclass()
                case "Ranger":
                    print("-----------------Subclass-----------------\n1. Hunter\n2. Beast Master\n--------------------------------------------")
                    player_subclass = input("Please enter your character's subclass: ")
                    while player_subclass not in Player_Class.ranger_subclasses:
                        print("Invalid input. Please try again.")
                        player_subclass = input("Please enter your character's subclass: ")
                    else:
                        Player_Class.player.set_character_subclass(player_subclass)
                        Player_Class.player.get_character_subclass()
                case "Rogue":
                    print("-----------------Subclass-----------------\n1. Thief\n2. Assassin\n3. Arcane Trickster\n--------------------------------------------")
                    player_subclass = input("Please enter your character's subclass: ")
                    while player_subclass not in Player_Class.rogue_subclasses:
                        print("Invalid input. Please try again.")
                        player_subclass = input("Please enter your character's subclass: ")
                    else:
                        Player_Class.player.set_character_subclass(player_subclass)
                        Player_Class.player.get_character_subclass()
                case "Sorcerer":
                    print("-----------------Subclass-----------------\n1. Draconic Bloodline\n2. Wild Magic\n--------------------------------------------")
                    player_subclass = input("Please enter your character's subclass: ")
                    while player_subclass not in Player_Class.sorcerer_subclasses:
                        print("Invalid input. Please try again.")
                        player_subclass = input("Please enter your character's subclass: ")
                    else:
                        Player_Class.player.set_character_subclass(player_subclass)
                        Player_Class.player.get_character_subclass()
                case "Warlock":
                    print("-----------------Subclass-----------------\n1. The Archfey\n2. The Fiend\n3. The Great Old One\n--------------------------------------------")
                    player_subclass = input("Please enter your character's subclass: ")
                    while player_subclass not in Player_Class.warlock_subclasses:
                        print("Invalid input. Please try again.")
                        player_subclass = input("Please enter your character's subclass: ")
                    else:
                        Player_Class.player.set_character_subclass(player_subclass)
                        Player_Class.player.get_character_subclass()
                case "Wizard":
                    print("-----------------Subclass-----------------\n1. School of Abjuration\n2. School of Conjuration\n3. School of Divination\n4. School of Enchantment\n5. School of Evocation\n6. School of Illusion\n7. School of Necromancy\n8. School of Transmutation\n--------------------------------------------")
                    player_subclass = input("Please enter your character's subclass: ")
                    while player_subclass not in Player_Class.wizard_subclasses:
                        print("Invalid input. Please try again.")
                        player_subclass = input("Please enter your character's subclass: ")
                    else:
                        Player_Class.player.set_character_subclass(player_subclass)
                        Player_Class.player.get_character_subclass()
                case _:
                    print("Invalid input. Please try again.")