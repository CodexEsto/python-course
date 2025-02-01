import random


number = random.randint(0, 100)


prediction = input("Guess the number (between 0 and 100): ")

if prediction == number:
    print("Correct! You've guessed the number.")
elif prediction < number:
    print("Too low.")
else:
    print("Too high.")

print(f"The number was: {number}")
