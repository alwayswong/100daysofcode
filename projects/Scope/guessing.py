# must define a variable at or above wherever you call a variable
from art import logo
import random

print(logo)
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100")
target = random.randint(1,100)
while True:
    lives = 0
    difficulty = input("Difficulty: Easy or Hard").lower().strip()
    if difficulty == 'easy':
        lives = 5
        break
    elif difficulty == 'hard':
        lives = 10
        break
    else:
        print('Easy or Hard?')
while True:
    guess = int(input("What is your guess?"))
    if guess == target:
        print(f"You win! The answer is {target}")
        print(logo)
        quit()
    elif guess != target:
        lives -= 1
        if lives == 0:
            print(f"You lose, the answer is {target}. Better luck next time!")
            quit()
        if guess < target:
            print("Too low")
            #lives -= 1
            print(f"You have {lives} guess(es) remaining")
        elif guess > target:
            print("Too high")
            #lives -= 1
            print(f"You have {lives} guess(es) remaining")
        else:
            print("Error")
            print(f"You have {lives} guess(es) remaining")
        print("Guess again")


