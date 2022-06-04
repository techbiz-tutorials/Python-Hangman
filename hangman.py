# To allow us to import random word from words.py
import random
from words import*
# Randomly selects word from list.py
wordlist = random.choice(words)
# Converts letters in word to items in list.
letterlist = list(wordlist)
# Variable for keeping track of successful guesses.
numberleft = len(letterlist)
# List to display unguessed letters as *'s.
displaylist = []
#Creates a list to displlay with placeholders from each letter of the word.
displaylist = list(wordlist)
# List of letters user has guessed.
guessed = []
# Variable for keeping track of unsuccessful guesses
misses = 0


# Sweet title screen.
print("**************************")
print("*      HANGMAN v0.9      *")
print("**************************")

# For each letter in the word, fill display with a *.
for x in range(len(letterlist)):
    displaylist[x] = "*"

# Variable that takes us into our while loop.
play = input("Play? y or n?")
while play.lower()=="y":
    # Displays letters we have guessed into our guessed list.
    print("Letters guessed:", guessed)
    print(displaylist)
    # Display graphic based on number of misses we have had.
    if misses == 0:
        print(" |---|")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")

    if misses == 1:
        print(" |---|")
        print(" |   O")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")

    if misses == 2:
        print(" |---|")
        print(" |   O")
        print(" |   |")
        print(" |   |")
        print(" |")
        print(" |")
        print("_|_")

    if misses == 3:
        print(" |---|")
        print(" |   O")
        print(" |  -|")
        print(" |   |")
        print(" |")
        print(" |")
        print("_|_")

    if misses == 4:
        print(" |---|")
        print(" |   O")
        print(" |  -|-")
        print(" |   |")
        print(" |")
        print(" |")
        print("_|_")

    if misses == 5:
        print(" |---|")
        print(" |   O")
        print(" |  -|-")
        print(" |   |")
        print(" |  /")
        print(" |")
        print("_|_")
    # Asks user to guess a letter, adds letter to guessed list, if letter is in list already, it deletes duplicate.
    # Then sorts list alphabetically.
    guess = input("Guess a letter.")
    guess = guess.lower()
    if guess in guessed:
        guessed.remove(guess)
    guessed.append(guess)
    guessed.sort()
    # if guess is in list, guess shows up in display and updates number of letters left.
    if guess in letterlist:
        if guess in guessed and guess in displaylist:
            pass
        else:
            for x in range(len(letterlist)):
                if letterlist[x] == guess:
                    displaylist[x] = guess
                    numberleft = numberleft-1
    # If number isn't in list, misses variable is updated.
    else:
        misses = misses+1

    # When you lose, this takes you out of the loop and ends the game.
    if misses >= 6:
        print(displaylist)
        print(" |---|")
        print(" |   O")
        print(" |  -|-")
        print(" |   |")
        print(" |  / \\")
        print(" |")
        print("_|_")
        print("Sorry, you lose.")
        print("The word was:",wordlist)
        play = "n"

    # When you win, this takes you out of the loop and ends the game.
    if numberleft <= 0:
        print("Congratulations! You win!")
        print("The word was:",wordlist)
        play= "n"
# Game over screen outside the loop.
print("Game Over...")



