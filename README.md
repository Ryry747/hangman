# Hangman
Milestone 2.py
Milestone 2 has been completed. In this milestone I used VScode to create a documment with a word list within in it. I imported the document to the milestone document and allocated random choice. I then allocated the if and the else to make sure that people recieved a response when they inputted a letter and to make sure that the character that was inputted was recognised.

The code I have written is as follows:
import random
from word_list import word_list

def get_word ():
    word = random.choice(word_list)

guess = input("Enter a letter.")
print(guess)

if len(guess) == 1 and guess.isalpha():
    if guess:
        print("Good guess!")
    else:
        print("Oops!That is not a valid input")