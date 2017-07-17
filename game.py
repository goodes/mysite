import os
import random

WORD_FILE = os.path.abspath(os.path.join(os.path.split(__file__)[0], "words.txt"))


def choose_word():
    words = open(WORD_FILE).readlines()
    return words[0].strip()

def scramble_word(word):
    word_as_list = list(word)
    random.shuffle(word_as_list)
    scrambled = "".join(word_as_list)

    # make sure that the scrambled word is not the original
    if scrambled != word:
        return scrambled
    else:
        return scramble_word(word)

if __name__ == "__main__":
    word = choose_word()
    scrambled = scramble_word(word)
    print("%s %s" % (word, scrambled))
