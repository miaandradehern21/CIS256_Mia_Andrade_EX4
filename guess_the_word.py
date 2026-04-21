


# import random to pick a word
import random

# simple list of words
words = ["coffee", "music", "festival", "gym", "school"]

# mode to pick one random word
word = random.choice(words)

# guessed letters
guessed = []

# et attempts
attempts = 6

print("Guess the word! :0")

# game loop
while attempts > 0:

    # show the word with _ and guessed letters
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    
    print("Word:", display)
    print("Attempts left:", attempts)

    # if no "_" left, user won
    if "_" not in display:
        print("You guessed it!")
        break

    # ask for a letter
    guess = input("Enter a letter: ").lower()

    # simple validation
    if len(guess) != 1:
        print("Only one letter")
        continue

    # if already guessed
    if guess in guessed:
        print("Already tried that")
        continue

    # save the guess
    guessed.append(guess)

    # check if correct
    if guess in word:
        print("Correct!")
    else:
        print("Wrong!")
        attempts -= 1

# if user loses
if attempts == 0:
    print("You lost... try again dont worry.")
    print("The word was:", word)
