import json
import os

def get_word_details(word):
    with open(os.path.join(os.path.dirname(__file__), '../data/dictionary.json'), 'r') as f:
        dictionary = json.load(f)
    return dictionary.get(word.lower(), {"error": "Word not found"})