

# import pytest 
import pytest

# import random to pick a word
import random


# recreate the same word list from my game
words = ["coffee", "music", "festival", "gym", "school"]


# test 1: check the random word is from the list
def test_random_word_from_list():
    # this pick a random word
    word = random.choice(words)
    
    # this check that the word is in my list
    assert word in words


# test 2: check correct guess
def test_correct_guess():
    # this set a fixed word
    word = "apple"
    
    # simulate a correct guess
    guess = "a"
    
    # this check that the guess is in the word
    assert guess in word


# test 3: check incorrect guess
def test_incorrect_guess():
    # set a fixed word
    word = "apple"
    
    # simulate a wrong guess
    guess = "z"
    
    # this heck that the guess is NOT in the word
    assert guess not in word
