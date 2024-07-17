import random

user_scores = 0
computer_scores = 0

options = ['rock', 'paper','scissors']

while True:
    user_choice = input("Enter 'rock', 'paper', or 'scissors' or Q to quit: ").lower()
    if user_choice.lower() == 'q':
        print(f"Final scores: User: {user_scores}, Computer: {computer_scores}")
        break

    if user_choice not in options:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_choice = options[random_number]
    print(f"You chose {user_choice}, Computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
        user_scores += 1
    else:
        print("Computer wins!")
        computer_scores += 1

    print(f"Final scores: User: {user_scores}, Computer: {computer_scores}")

    if user_scores >= 3 or computer_scores >= 3:
        print("Game over!")
        break

    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again!= 'y':
        print("Goodbye!")
        break

print("Goodbye!")