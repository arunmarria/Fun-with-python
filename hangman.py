# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    count = 0;
 
    for i in range(len(secret_word)):
        for element in letters_guessed:
            if(secret_word[i] == element):
                count = count+1
                break
    if(count == len(secret_word)):
        return True
    else:
        return False
            
                
     
                

        


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
   
    l =[];
    for i in range(len(secret_word)):
        for element in letters_guessed:
            if(secret_word[i] == element):
                l.append(element)
                break
                
                
            elif(element == letters_guessed[-1] and secret_word[i] != element) :
                l.append('_ ')
                
                
    return ''.join(l)
                
    
    
    

        
   



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    l=[];
    for letter in string.ascii_lowercase:
        for element in letters_guessed:
            if(element==letter):
                break
            
            elif(element != letter and element == letters_guessed[-1]):
                l.append(letter)
    if(len(letters_guessed)==0):
        return string.ascii_lowercase
    else:
        return ''.join(l)
   
       
    
 ## for printing repeated lines during hangman play
   
def print_repeat(guesses_remaining, letters_guessed,secret_word):
    print(get_guessed_word( secret_word, letters_guessed  ))
    print("-------------")
    print("You have ",str(guesses_remaining)," guesses left.")
    print("Available letters: ", get_available_letters(letters_guessed) )
   


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings_remaining = 3
    guesses_remaining = 6
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ", str(len(secret_word))," letters long.")
    
    print("You have ", str(warnings_remaining), " warnings left.")
    
    
    
    
    while(guesses_remaining >0 and is_word_guessed(secret_word, letters_guessed) ==  False):
        
        print_repeat(guesses_remaining, letters_guessed,secret_word)
        
        guess = input("Please guess a letter: ")
        
        # guessed word already present
        if(guess in letters_guessed):
            ## lower number of warnings left  by 1
            if(warnings_remaining >0):
                warnings_remaining = warnings_remaining -1
                print("Oops! You've already guessed that letter. You have ", warnings_remaining ," warnings left: ")
                continue
            ## lower number of guesses if warnings are alreardy 0   
            else:
                guesses_remaining = guesses_remaining-1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ")
                continue
        
        ## if guess is not an alphabet
        elif(guess not in string.ascii_lowercase or guess == ''):
            if (warnings_remaining >0):
                warnings_remaining = warnings_remaining -1
                print("Oops! That is not a valid letter. You have ", warnings_remaining ," warnings left: ")
                continue
            else:
                guesses_remaining = guesses_remaining-1
                print("Oops! That is not a valid letter. You have You have no warnings left so you lose one guess: ")
                continue
        
        
        ## good guess    
        elif(guess in secret_word and guess not in letters_guessed ):
            letters_guessed.append(guess)
            print("Good guess :")
            continue
        
        
        ## bad guess if guess not in secret word
        elif(guess not in secret_word and guess in get_available_letters(letters_guessed)):
            if(guess in "aeiou"):
                letters_guessed.append(guess)
                guesses_remaining = guesses_remaining - 2
                print("Oops! That letter is not in my word.")
                continue
                
                
            else:
                letters_guessed.append(guess)
                guesses_remaining = guesses_remaining -1
                print("Oops! That letter is not in my word.")
                continue
                
    
    if(is_word_guessed(secret_word, letters_guessed)):
        print(get_guessed_word( secret_word, letters_guessed  ))
        print("-------------")
   
        print("Congratulations, you won!")
        print("Your total score for this game is: ", guesses_remaining * len(set(secret_word)))
    
    if(is_word_guessed(secret_word, letters_guessed)==False and guesses_remaining ==0):
        print(get_guessed_word( secret_word, letters_guessed  ))
        print("-------------")
   
        print("Sorry, you ran out of guesses. The word was ", secret_word)
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
