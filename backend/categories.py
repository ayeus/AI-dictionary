def get_category_words(level):
    categories = {
        "easy": ["happy", "sad", "big"],
        "medium": ["joyful", "melancholy", "enormous"],
        "hard": ["euphoria", "lugubrious", "gargantuan"]
    }
    return categories.get(level, [])