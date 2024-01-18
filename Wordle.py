# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        #function that gets the word from the squares and makes it a word
        def createWord():
            # Array that stores the letters in the squares before these letters are combined into a word
            guessArray = []
            #check to see if the word the user entered is a real word (in the word list)
            for guessLetter in range(N_COLS):
                guessArray.append(gw.get_square_letter(0, guessLetter))
        
            #combine the array into a word
            word = ''.join(guessArray).lower()
            return word
        
        

        # initialized English word list dictionary
        wordList = FIVE_LETTER_WORDS

        # pick a word to guess from the word list provided in the WordleDictionary.py
        correctWord = random.choice(wordList).upper()

        #Calls createWord function to pull user input guess
        guessWord = createWord()

        #Go through letter in the word 
        for letter in range(N_COLS):
            gw.set_square_letter(N_ROWS-1, letter, correctWord[letter])

        # Check to see if
        if guessWord in wordList:
            gw.show_message("Slay thats a word")
        else:
            gw.show_message("Not in word list")




    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()