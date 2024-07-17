"""
The user will be prompted to choose own adventurous account
"""

import random

print("Welcome to the Adventure Game!")
name = input("Enter your name: ")
account = input(f"Choose a unique adventurous account name for {name}: ")

treasure = 100
gold = 250

""" The player's character and other characters will be created with attributes such as health, strength, and defense """

health = 100
goblin_defense = 10
dragon_defense = 10
strength = 10
defense = 5


print("Choose your starting location:")
print("1. Forest")
print("2. Mountain")
starting_location = int(input("Enter your choice (1 or 2): "))

if starting_location not in [1, 2]:
    print("Invalid choice. Starting in the forest. Enter 1 or 2 to start")
    starting_location = 1

if starting_location == 1:
    print("You find yourself in a beautiful forest.")
    forest_encounter = random.randint(1, 10)
    if forest_encounter <= 5:
        print("You encountered a goblin!")
        goblin_health = 50
        while True:
            player_attack = random.randint(1, strength)
            goblin_health -= player_attack
            print(f"{name} attacks the goblin, dealing {player_attack} damage!")
            if goblin_health <= 0:
                print("You defeated the goblin!")
                break
            goblin_attack = random.randint(1, goblin_defense)
            health -= goblin_attack
            print(f"The goblin attacks {name}, dealing {goblin_attack} damage!")
            if health <= 0:
                print("You died!")
                break
    else:
        print("You found a treasure chest!")
        open_chest = input("Do you want to open a chest? (yes/no): ")
        if open_chest.lower() == "yes":
            treasure += random.randint(50, 150)
            print(f"You found {treasure} treasure!")
        elif open_chest.lower() == "no":
            print("You decide to stay in the mountain.")


elif starting_location == 2:
    print("You found yourself in a steep mountain")
    mountain_encounter = random.randint(1, 10)
    if mountain_encounter <= 5:
        print("You meet a dragon")
        dragon_health = 150
        while True:
            player_attack = random.randint(1, strength)
            dragon_health -= player_attack
            print(f"{name} attacks the dragon, dealing {player_attack} damage!")
            if dragon_health <= 0:
                print("You killed dragon")
                break
            dragon_attack = random.randint(1, dragon_defense)
            health -= dragon_attack
            print(f"The dragon attacks {name}, dealing {dragon_attack} damage!")
            if health <= 0:
                print("You died!")
                break
    else:
        print("You found a powerful artifact!")
        artifact_value = random.randint(100, 1000)
        print(f"You found an artifact worth {artifact_value} gold!")
        gold += artifact_value


#### This can be improved...