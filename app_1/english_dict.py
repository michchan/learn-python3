import os
import json
from difflib import get_close_matches

# -------------------- Init --------------------
exit_words = ['\exit', '\cancel', '\quit', '\q']
exit_words_str = ', '.join(exit_words)
# Get dirname
dirname = os.path.dirname(__file__)
# Load JSON data
data = json.load(open(f'{dirname}/data.json'))

# -------------------- Main --------------------
def is_end(word):
    return exit_words.count(word) > 0

def ask_for_input():
    raw_text = input(f'Enter word (enter \"{exit_words_str}\" to exit): ')
    return str(raw_text).strip()

def get_definitions(word):
    # Try lowercase
    if word.lower() in data:
        return data[word.lower()]
    # Try capitalized
    elif word.capitalize() in data:
        return data[word.capitalize()]
    return None

def find_similar_words(word):
    return get_close_matches(word, data.keys(), n = 5)

def display_similar_words(word, similar_words):
    similar_words_str = ', '.join(similar_words)
    print(f'** No word \"{word}\" found. Did you mean any of the following: {similar_words_str} ?')

def display_definitions(word, definitions):
    print('\n'.join(definitions))

def translate(word):
    definitions = get_definitions(word)
    if definitions == None:
        similar_words = find_similar_words(word)
        display_similar_words(word, similar_words)
    else:
        display_definitions(word, definitions)

def main(): 
    while True:
        print('\n')
        word = ask_for_input()
        if is_end(word): break
        translate(word)
        
# Start app
main()