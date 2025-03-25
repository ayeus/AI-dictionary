from categories import get_category_words
from dictionary_api import get_word_details
import random

def generate_quiz():
    words = get_category_words("easy")[:3] + get_category_words("medium")[:2]
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

def generate_passage():
    words = get_category_words("easy")[:2]
    return {
        "passage": f"The {words[0]} child smiled at the {words[1]} puppy.",
        "questions": [
            {"question": f"Find a synonym for '{words[0]}'", "answer": get_word_details(words[0])["synonyms"][0]},
            {"question": f"Find an antonym for '{words[1]}'", "answer": get_word_details(words[1])["antonyms"][0]}
        ]
    }

def generate_puzzle():
    words = get_category_words("easy")[:3]
    return {"words": words, "type": "word_search"}