import random

# Get the top of the range from the user
top_of_range = int(input("Enter the top of the range: "))

random_number = random.randint(1, top_of_range)
attempts = 0

while True:
    attempts += 1
    user_guess = input("Type a number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess < 1:
            print("Number must be greater than 0")
    else:
        print("Invalid input. Please enter a number.")
        continue    
    
    if user_guess == random_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

print("The number of attempts: " + str(attempts))


    
    