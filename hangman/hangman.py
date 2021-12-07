import string
import random
from hangman_master import words


def get_v_word(wo):

    word = random.choice(wo)
    while "-" in word or " " in word:
        word = random.choice(wo)

    return word


def hangmann():
    word = get_v_word(words.wordss).upper()
    print(word)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 4

    while len(word_letter) > 0 and lives > 0:
        print(
            "you have ",
            lives,
            " lives and you have used these letters: ",
            " ".join(used_letter),
        )

        word_list = [letter if letter in used_letter else "-" for letter in word]
        print("current word : ", " ".join(word_list))
        user_input = input("guess a letter: ").upper()
        if user_input in alphabet - used_letter:
            used_letter.add(user_input)
            if user_input in word_letter:
                word_letter.remove(user_input)
            else:
                lives -= 1
        elif user_input in used_letter:
            print("you have already used that character. please try again.")

        else:
            print("invalid character, please try again. ")


hangmann()
