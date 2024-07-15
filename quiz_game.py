print("Welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Let's start!")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
    print(f"Your current score is: {score}")
else:
    print("Incorrect! The correct answer is Central Processing Unit!")
    
answer2 = input("What is the name of the first computer programmer? ")
if answer2.lower() == "alan turing":
    print("Correct!")
    score += 1
    print(f"Your current score is: {score}")
else:
    print("Incorrect! The correct answer is Alan Turing!")

print(f"Your score is: {score}")
