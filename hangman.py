import random

def play_hangman():
    word_list = ["python", "javascript", "computer", "programming", "code"]
    word = random.choice(word_list)
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    word_guessed = set()

    tries = 6
    print("Welcome to Hangman! You have", tries, "tries to guess the word.")

    while len(word_letters) > 0 and tries > 0:
        print("You used the following letters:", " ".join(used_letters))
        print("You have already guessed the following letters:", " ".join(word_guessed))
        print("Guess a letter:")
        guess = input().lower()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_guessed.add(guess)
                word_letters.discard(guess)
                print("Correct! The word contains the letter:", guess)
            else:
                tries -= 1
                print("Incorrect! The word does not contain the letter:", guess)
                print("You have", tries, "tries left.")
        elif guess in used_letters:
            print("You already used that letter, try again.")
        else:
            print("Invalid input, try again.")
        
        if len(word_letters) == 0:
            print("Congratulations! You guessed the word:", word)
        elif tries == 0:
            print("Sorry, you were unable to guess the word. The word was", word)

play_hangman()
