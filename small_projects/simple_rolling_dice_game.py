import random

print("Welcome to the Rolling Dice Simulator!")

while True:
    choice = input("Press enter to roll the dice or 'q' to quit: ").strip().lower()
    if choice == 'q':
        print("Thank you for playing! Goodbye!")
        break
    elif choice == '':
        number = random.randint(1, 6)
        print(f"You rolled a {number}!")
    else:
        print("Invalid input. Please press enter to roll the dice or 'q' to quit.")

print("Game over.")