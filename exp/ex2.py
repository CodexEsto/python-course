import random

# Random number between 0 and 100
number = random.randint(0, 100)

while True:
    # User input for the prediction
    predict = int(input("Guess the number (between 0 and 100): "))

    if predict == number:
        print("Correct! You've guessed the number.")
        break
    elif predict < number:
        print("Too low.")
    else:
        print("Too high.")
