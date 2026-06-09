# 🏆 Raffle Prize Picker
import random

names = []
prizes = []
num_participants = 0

while num_participants < 3:
    try:
        num_participants = int(input("How many people are entering the raffle? (at least 3) "))
        if num_participants < 3:
            print("Please enter at least 3 participants.")
    except ValueError:
        print("Please enter a valid number.")

for _ in range(num_participants):
    name = input("Enter a participant's name: ")
    names.append(name)

# Enter the names of the prizes
print("\nEnter the names of the prizes for this challenge. The third one should be the grand prize!")
for i in range(3):
    prize = input(f"Enter the name of prize {i+1}: ")
    prizes.append(prize)
# 4. Randomly pick 3 different winners from the participant list without repeats.

winners = random.sample(names, 3)

print("\nRaffle Winners")
for i in range(3):
    if i == 2:
        print(f"Grand Prize 🏆: {winners[i]} wins {prizes[i]}!")
    else:
        print(f"{winners[i]} wins {prizes[i]}!")

# Hint: Use loops, lists, and a tool that picks random items without repeats.