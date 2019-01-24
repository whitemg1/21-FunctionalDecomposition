"""
Hangman.

Authors: PUT_YOUR_NAME_HERE and YOUR_PARTNERS_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
import random


def choose_word(min_length):
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        while True:
            r = random.randrange(0, len(words))
            rand_word = words[r]
            if len(rand_word) >= min_length:
                break

        print(' _ ' * len(rand_word))
        print(rand_word)

        return rand_word

class Hangman(object):
    def __init__(self,rand_word, max_errors):
        self.rand_word = rand_word


        self.max_errors = max_errors
        self.number_of_errors = 0

    def check_guess(self, guess):
        str = ''
        count = 0
        for k in range(len(self.rand_word)):
            if self.rand_word[k] == guess:
                str = str + guess
                count = count + 1
            else:
                str = str + ' - '
        if count == 0:
            self.number_of_errors = self.number_of_errors + 1
            guesses_left = self.m
            print('Your guess')






    return string


#choose_word(5)

#start_of_game()



