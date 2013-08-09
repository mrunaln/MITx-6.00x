from ps4a import *

#
# Test code
# You don't need to understand how this test code works (but feel free to look it over!)

# To run these tests, simply run this file (open up in IDLE, then run the file as normal)

WORDLIST_FILENAME = "words.txt"

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    wordScore = 0

    if word != "":
        for letter in word:
            value = SCRABBLE_LETTER_VALUES[letter]    
            wordScore += value

        wordScore *= len(word)
        if len(word) == n:
            wordScore += 50
    
    return wordScore

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand_copy = hand.copy()
    for letter in word:
        if hand_copy.get(letter, 0):
            hand_copy[letter] -= 1
    return hand_copy


def isValidWord(word, hand, wordList):
    #print hand
    if word in wordList:
        letter_dict = {}
        for w in word:
            if not letter_dict.get(w,0):
                letter_dict[w] = 1
            else:
                letter_dict[w] += 1
        for w in word:
            #print w
            #print hand
            if w in hand:
                #print "ithe ugach nako yeu!"
                if letter_dict.get(w, 0) > 0:
                    if hand.get(w, 0) < letter_dict.get(w, 0):
                        #return True
                    #else:
                        return False
            else:
                return False
        return True
    else: 
        # word is not in wordList
        return False

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def test_getWordScore():
    """
    Unit test for getWordScore
    """
    failure=False
    # dictionary of words and scores
    words = {("", 7):0, ("it", 7):4, ("was", 7):18, ("scored", 7):54, ("waybill", 7):155, ("outgnaw", 7):127, ("fork", 7):44, ("fork", 4):94}
    for (word, n) in words.keys():
        score = getWordScore(word, n)
        if score != words[(word, n)]:
            print "FAILURE: test_getWordScore()"
            print "\tExpected", words[(word, n)], "points but got '" + str(score) + "' for word '" + word + "', n=" + str(n)
            failure=True
    if not failure:
        print "SUCCESS: test_getWordScore()"

# end of test_getWordScore

def test_updateHand():
    """
    Unit test for updateHand
    """
    # test 1
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'l':1, 'm':1}
    expectedHand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2

        return # exit function
    if handCopy != handOrig:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tOriginal hand was", handOrig
        print "\tbut implementation of updateHand mutated the original hand!"
        print "\tNow the hand looks like this:", handCopy
        
        return # exit function
        
    # test 2
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    handCopy = handOrig.copy()
    word = "evil"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'v':1, 'n':1, 'l':1}
    expectedHand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"        
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2

        return # exit function

    if handCopy != handOrig:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tOriginal hand was", handOrig
        print "\tbut implementation of updateHand mutated the original hand!"
        print "\tNow the hand looks like this:", handCopy
        
        return # exit function

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "hello"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {}
    expectedHand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"                
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2
        
        return # exit function

    if handCopy != handOrig:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tOriginal hand was", handOrig
        print "\tbut implementation of updateHand mutated the original hand!"
        print "\tNow the hand looks like this:", handCopy
        
        return # exit function

    print "SUCCESS: test_updateHand()"

# end of test_updateHand


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def test_isValidWord(wordList):
    """
    Unit test for isValidWord
    """
    failure=False
    # test 1
    word = "hello"
    handOrig = getFrequencyDict(word)
    handCopy = handOrig.copy()
    if not isValidWord(word, handCopy, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected True, but got False for word: '" + word + "' and hand:", handOrig

        failure = True

    # Test a second time to see if wordList or hand has been modified
    if not isValidWord(word, handCopy, wordList):
        print "FAILURE: test_isValidWord()"

        if handCopy != handOrig:
            print "\tTesting word", word, "for a second time - be sure you're not modifying hand."
            print "\tAt this point, hand ought to be", handOrig, "but it is", handCopy

        else:
            print "\tTesting word", word, "for a second time - have you modified wordList?"
            wordInWL = word in wordList
            print "The word", word, "should be in wordList - is it?", wordInWL

        print "\tExpected True, but got False for word: '" + word + "' and hand:", handCopy

        failure = True


    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "rapture"

    if  isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected False, but got True for word: '" + word + "' and hand:", hand

        failure = True        

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected True, but got False for word: '"+ word +"' and hand:", hand

        failure = True                        

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected False, but got True for word: '" + word + "' and hand:", hand
        
        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "evil"
    
    if  not isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected True, but got False for word: '" + word + "' and hand:", hand
        
        failure = True
        
    # test 6
    word = "even"

    if  isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected False, but got True for word: '" + word + "' and hand:", hand
        print "\t(If this is the only failure, make sure isValidWord() isn't mutating its inputs)"        
        
        failure = True        

    if not failure:
        print "SUCCESS: test_isValidWord()"


wordList = loadWords()
print "----------------------------------------------------------------------"
print "Testing getWordScore..."
test_getWordScore()
print "----------------------------------------------------------------------"
print "Testing updateHand..."
test_updateHand()
print "----------------------------------------------------------------------"

print isValidWord('chayote', {'a': 1, 'c': 2, 'u': 2, 't': 2, 'y': 1, 'h': 1, 'z': 1, 'o': 2}, wordList)

print "Testing isValidWord..."
test_isValidWord(wordList)
