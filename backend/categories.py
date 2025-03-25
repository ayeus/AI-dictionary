from dictionary_api import get_word_details

def get_category_words(level):
    categories = {
        "easy": ["happy", "sad", "big"],
        "medium": ["joyful", "melancholy", "enormous"],
        "hard": ["euphoria", "lugubrious", "gargantuan"]
    }
    return categories.get(level, [])