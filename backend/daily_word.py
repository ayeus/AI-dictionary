import random
from categories import get_category_words

def get_daily_word():
    all_words = get_category_words("easy") + get_category_words("medium") + get_category_words("hard")
    return random.choice(all_words)