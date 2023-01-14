import random

print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("What's your guess? "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("You got it! The number was", number)
