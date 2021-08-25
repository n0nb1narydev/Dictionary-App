import json
from difflib import SequenceMatcher

# creates a python dictionary from the json file
data = json.load(open("data.json"))


def get_definition(w):
    """Takes in a word and returns the value if it exists in the data file."""
    if w in data:
        return data[w]
    else:
        return f"The word {w} does not exist. Please try again."


def get_word():
    word = input("What word would you like to define? ").casefold()
    return word


def check_word(w):
    """Uses the SequenceMatcher to determine if a word that is entered is similar to any other words in the data file."""
    SequenceMatcher(w,)


print(get_definition(get_word()))