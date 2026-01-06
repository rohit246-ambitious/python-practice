"""
Create a simple guessing game
The user get 10 chances to guess a number 
If the user guesses the number before 10 chanses, stop asking the number from the user, say congrats and end the game 
if user never guesses the number ask them 10 times and end the game!
"""

import random

num = 1
print("Welcome to the Guessing Number Game!")
print("I have selected a number between 1 and 50.")
print("You have 10 chances to guess the correct number.")
secret_number = random.randint(1, 50)
attempts = 10
is_guess_correct = False

while num <= attempts:
    guess = input(f"Attempt {num}: Please enter your guess: ")
    
    # Validate input
    if not guess.isdigit():
        print("Invalid input. Please enter a number between 1 and 50.")
        continue
    
    guess = int(guess)
    
    if guess < 1 or guess > 50:
        print("Your guess is out of range. Please guess a number between 1 and 50.")
        continue
    
    if guess == secret_number:
        print(f"Congratulations! You've guessed the correct number {secret_number} in {num} attempts!")
        is_guess_correct = True
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    num += 1

if not is_guess_correct:
    print(f"Game over! You've used all your attempts. The correct number was {secret_number}.")