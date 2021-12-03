import string
import random
from hangman_master import words

def get_v_word(words):

    word=random.choice(words)
    while '-' in word or ' ' in word:
         word=random.choice(words)
    
    return word

def hangman():
    word=get_v_word(words)
    word_letter=set(word)
    alphabet=set(string.ascii_uppercase )
