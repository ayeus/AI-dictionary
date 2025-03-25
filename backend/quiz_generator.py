from categories import get_category_words
from dictionary_api import get_word_details
import random

def generate_quiz():
    words = get_category_words("easy")[:5]  # Sample 5 words
    quiz = []
    for word in words:
        details = get_word_details(word)
        question = {
            "question": f"What is a synonym for '{word}'?",
            "options": details["synonyms"] + ["wrong1", "wrong2"],
            "answer": details["synonyms"][0]
        }
        random.shuffle(question["options"])
        quiz.append(question)
    return quiz