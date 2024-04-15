def get_valid_guess():
    """Repeatedly prompt the user for a guess until they enter a valid guess:
    - must be exactly 5 letters
    - must be letters only
    - "must be a word" ... we won't do this part
    """
    while True: # infinite loop
        # 1. get input from user
        guess = input('What is your guess? ').upper()
        # 2. ensure length is 5
        if len(guess) != 5:
            print('Supposed to be 5 letters!')
        # 3. ensure only letters
        elif not guess.isalpha():
            print('Non-letter found!')
        # 4. return the valid guess
        else:
            return guess


def check_letters(user_guess, word):
    """Compare user's guess to the word and identify exact and inexact matches."""
    response_str = ''

    for index, letter in enumerate(user_guess): # 10
        if letter == word[index]: # 11
            # exact match based on position
            response_str += letter # str-based solution for 12
        elif letter in word: # 13 , inexact match
            response_str += '?'
        else:
            response_str += '-'

    return response_str


import random
import wordlist

secret_word = random.choice(wordlist.word_list).upper() # good catch, Joanna

print('WORDLE: I picked a 5-letter word and you should guess it.') # 2
guess_count = 0 # 2a

while guess_count < 6: # 3
    guess = get_valid_guess() # 5
    guess_count += 1

    if guess == secret_word:
        print(f'You got it in {guess_count} guesses!')
        break # out of the while loop cuz we're done

    print(check_letters(guess, secret_word))

else: # the code in here (this else clause) is only run if we DID NOT BREAK out of the loop
    print('The word was', secret_word)
