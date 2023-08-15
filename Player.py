from Character import Character # Import the Character class from Character.py
from Race import Races
from Class import Player_Class

player = Character()
race = Races()
player_class = Player_Class()
# Function to create a character
print("Welcome to the D&D Character Creator!")
print("Please enter the following information to create your character.")

# Get the player's name
player_name = input("Please enter your character's name: ")
player.set_name(player_name)
player.get_name()

# Get the player's race
race.display_race()

race.roll_for_stats()

# Get the player's class
# player_class.display_classes()

# print(player.name, race.player.character_race, race.player.character_subrace, player_class.player.character_class, player_class.player.character_subclass)