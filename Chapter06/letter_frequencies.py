from collections import Counter
from collections import defaultdict
import string


def letter_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


num_items = 0


def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])


d = defaultdict(tuple_counter)


def counter_letter_frequency(sentence):
    return Counter(sentence)


CHARACTERS = list(string.ascii_letters) + [" "]


def list_letter_frequency(sentence):
    frequencies = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1] + 1)
    return frequencies
