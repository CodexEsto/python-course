import random

a = random.randint(0, 10)
guess = int(input("Guess the number (between 0 and 10): "))

while a != guess:
    if a > guess:
        print("Too low.")
        guess = int(input("Guess again: "))
    else:
        print("Too high.")
        guess = int(input("Guess again: "))

print("Correct! You've guessed the number.")
