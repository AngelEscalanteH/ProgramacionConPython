from words import words
from leter import get_leter
import random

def get_valid_word(words):
    word = random.choice(words)

    while not word.isalpha():
        word = random.choice(words)

    return word.upper()

word = get_valid_word(words)
wordLeters = set(list(word))
foundLeters = set()


def search_in_word(guess):
    global wordLeters

    for leter in wordLeters:
        if leter == guess:
            return True

    return False


def print_found_leters():
    global word, foundLeters

    foundWord = [" " + letter + " " if letter in foundLeters else " _ " for letter in word]

    print("-------------")
    print(' '.join(foundWord))


def hangman():
    global wordLeters, foundLeters
    lives = 6

    print(" _ " * len(wordLeters))

    while lives > 0 and len(foundLeters) < len(wordLeters):
        print(f"You have {lives} lives") # [f] Put variables in the string
        guess = get_leter(foundLeters)

        if search_in_word(guess) == False:
            lives -= 1
        else:
            foundLeters.add(guess)
            print_found_leters()

    if lives > 0:
        print(f"Congratulations!! You won with {lives} extra lives")
    else:
        print(f"You lost, the word was: {word}")

hangman()