# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for d in lettersGuessed:
        if secretWord.find(d) != -1:
            count += 1
    if count == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    arr = list(secretWord)
    ans = []
    l = len(secretWord)
    while l > 0:
     ans.append('_ ')
     l -= 1 
    idx = -1
    for d in arr:
        if d in lettersGuessed:
            idx = arr.index(d)
            arr[idx] = '-1'
            ans[idx] = d
    
    return ''.join(ans)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    guessed = list(lettersGuessed)
    allletters = list(string.ascii_lowercase)
    
    filtered = []
    for c in allletters:
        if c not in guessed:
            filtered.append(c)
    return ''.join(filtered)

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer’s word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    #randomWord = chooseWord(wordList)
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    mistakesMade = 0
    guesses = 8
    lettersGuessed = ""
    returnedValues = []

    #initialize previousValue and currentValue by "_ _ ..."
    previousValue = ""
    currentValue = ""
    
    while( mistakesMade < guesses ):
        print "-------------"
        print "You have " + str(guesses - mistakesMade) + " guesses left."
        availableLetters = getAvailableLetters(lettersGuessed)
        print "Available letters: " + availableLetters
        guess = raw_input("Please guess a letter: ")
        guessInLowerCase = guess.lower()
        #if guessInLowerCase not in lettersGuessed:
        
        if guess not in availableLetters:
            print "Oops! You've already guessed that letter: " + currentValue
        else:
            currentValue = getGuessedWord(secretWord, lettersGuessed)
            if currentValue == previousValue:
                lettersGuessed += guessInLowerCase
                print "Oops! That letter is not in my word: " + previousValue
                mistakesMade += 1
            else:
                previousValue = currentValue
                if mistakesMade == 0:
                    firstCheck = ""
                    for i in range(0, len(secretWord)):
                        firstCheck += "_ "
                    if currentValue == firstCheck:
                        lettersGuessed += guessInLowerCase
                        print "Oops! That letter is not in my word: " + currentValue
                        mistakesMade += 1
                    else:
                        print "Good guess: " + currentValue
                        
                else:
                    print "Good guess: " + currentValue
        print "Letters Guessed: " + lettersGuessed
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
            break

    if mistakesMade == guesses:
        print "Sorry, you ran out of guesses. The word was "  + secretWord + "."


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

print "Welcome to the game, Hangman!"
#secretWord = chooseWord(wordlist).lower()
secretWord = "mrunallll"
hangman(secretWord)
