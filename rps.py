import random

print("Welcome to Rock, Paper, Scissors!")

while True:
    print("Enter 1 for rock, 2 for paper, or 3 for scissors.")
    player = int(input("Your choice: "))
    computer = random.randint(1, 3)

    if player == 1:
        if computer == 1:
            print("Tie! You both picked rock.")
        elif computer == 2:
            print("You lose! Computer picked paper.")
        else:
            print("You win! Computer picked scissors.")
    elif player == 2:
        if computer == 1:
            print("You win! Computer picked rock.")
        elif computer == 2:
            print("Tie! You both picked paper.")
        else:
            print("You lose! Computer picked scissors.")
    elif player == 3:
        if computer == 1:
            print("You lose! Computer picked rock.")
        elif computer == 2:
            print("You win! Computer picked paper.")
        else:
            print("Tie! You both picked scissors.")
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

    if input("Do you want to play again? (y/n) ") == "n":
        break

print("Thanks for playing!")
