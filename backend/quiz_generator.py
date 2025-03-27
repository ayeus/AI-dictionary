from groq import Groq
from categories import get_category_words
import random

client = Groq(api_key="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")  # Replace with your actual, valid API key

def generate_quiz():
    try:
        words = get_category_words("easy")[:3] + get_category_words("medium")[:2]
        quiz = []
        for word in words:
            prompt = f"Generate a clean quiz question asking for a synonym of '{word}'. Provide the question, 4 options (one correct), and the correct answer in this format:\nQuestion: What is a synonym for '{word}'?\nOptions: option1, option2, option3, option4\nAnswer: option1"
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200
            )
            content = response.choices[0].message.content.strip()
            lines = content.split('\n')
            question = {
                "question": next((line.split(': ')[1] for line in lines if line.startswith("Question")), f"What is a synonym for '{word}'?"),
                "options": next((line.split(': ')[1].split(', ') for line in lines if line.startswith("Options")), ["option1", "option2", "option3", "option4"]),
                "answer": next((line.split(': ')[1] for line in lines if line.startswith("Answer")), "option1")
            }
            quiz.append(question)
        return quiz  # Should always return an array if successful
    except Exception as e:
        return {"error": f"Failed to generate quiz: {str(e)}"}  # Returns an object on error

def generate_passage():
    try:
        words = get_category_words("easy")[:2]
        prompt = f"Generate a short passage using '{words[0]}' and '{words[1]}', followed by two clean questions:\n1. A synonym question for '{words[0]}'\n2. An antonym question for '{words[1]}'\nFormat:\nPassage: [text]\nQuestion 1: What is a synonym for '{words[0]}'?\nAnswer 1: [answer]\nQuestion 2: What is an antonym for '{words[1]}'?\nAnswer 2: [answer]"
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        content = response.choices[0].message.content.strip()
        lines = content.split('\n')
        return {
            "passage": next((line.split(': ')[1] for line in lines if line.startswith("Passage")), "Default passage"),
            "questions": [
                {"question": next((line.split(': ')[1] for line in lines if line.startswith("Question 1")), "Default Q1"), "answer": next((line.split(': ')[1] for line in lines if line.startswith("Answer 1")), "Default A1")},
                {"question": next((line.split(': ')[1] for line in lines if line.startswith("Question 2")), "Default Q2"), "answer": next((line.split(': ')[1] for line in lines if line.startswith("Answer 2")), "Default A2")}
            ]
        }
    except Exception as e:
        return {"error": f"Failed to generate passage: {str(e)}"}

def generate_puzzle():
    try:
        words = get_category_words("easy")[:3]
        return {"words": words, "type": "word_search"}
    except Exception as e:
        return {"error": f"Failed to generate puzzle: {str(e)}"}