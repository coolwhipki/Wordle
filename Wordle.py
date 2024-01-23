# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # initialized English word list dictionary
    wordList = FIVE_LETTER_WORDS

    # pick a word to guess from the word list provided in the WordleDictionary.py
    correctWord = random.choice(wordList).lower()

    def enter_action(s):

        #function that gets the word from the squares and makes it a word
        def createWord():
            # Array that stores the letters in the squares before these letters are combined into a word
            guessArray = []
            #check to see if the word the user entered is a real word (in the word list)
            for guessLetter in range(N_COLS):
                guessArray.append(gw.get_square_letter(gw.get_current_row(), guessLetter))
        
            #combine the array into a word
            word = ''.join(guessArray).lower()
            return word
        
        

        #Calls createWord function to pull user input guess
        guessWord = createWord()

        if guessWord in wordList:
            #Go through letter in the word print to last row
            for letter in range(N_COLS):
                gw.set_square_letter(N_ROWS-1, letter, correctWord[letter].upper())



            # Color the squares based on how close their guess is to the correct word
            # Lists of booleans to keep track of correct and present letters
            correct_letters_matched = [False] * N_COLS
            present_letters_matched = [False] * N_COLS

            # If the user has checked the color blind option it changes the colors for boxes
            colorBlind = True

            #if color blind is true then change the colors that are passed to set_square_color to colorblind safe colors
            if colorBlind == True:
                correct = "#000080"
                present = "#DAA520"
                missing = "#D3D3D3"
            else:
                correct = CORRECT_COLOR
                present = PRESENT_COLOR
                missing = MISSING_COLOR

            # Check if the guess is correct
            # Color the boxes based on correct and present letters
            for square in range(N_COLS):
                # Make words lowercase for correct comparison and iterate through each letter of each word
                guess_letter = guessWord[square].lower()
                correct_letter = correctWord[square].lower()

                # Checks if the guess letter is the correct letter and also checks if that letter in that current position has been 
                #found in the correct position
                if guess_letter == correct_letter and not correct_letters_matched[square]:
                    gw.set_square_color(gw.get_current_row(), square, correct)
                    correct_letters_matched[square] = True

                # Checks if guess letter is in the correct word and checks if letter in current position has already been 
                #found in the correctword
                elif guess_letter in correctWord and not present_letters_matched[square]:
                    gw.set_square_color(gw.get_current_row(), square, present)
                    present_letters_matched[square] = True

                # Not in correct word
                else:
                    gw.set_square_color(gw.get_current_row(), square, missing)

            # If all the squares are green that means it is the correct word so put a congratulatory message
            if all(correct_letters_matched):
                gw.show_message("Congratulations! That is the word.")
            # Didn't guess the right word so moves you down a row and tells you to guess again
            else:
                gw.set_current_row(gw.get_current_row() + 1)
                gw.show_message("Guess again, muchacho")

        # If the word is not in the word list (not an english word) does not run all the checks
        else:
            gw.show_message("Not in word list")



    # Access to the WordleGWindow object in WordleGraphics.py methods
    gw = WordleGWindow()
    
    # adds enter_action to enter_listener so when you press enter it runs logic
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()