from groq import Groq

client = Groq(api_key="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")  # Replace with your actual, valid API key

def get_category_words(level):
    try:
        prompt = f"List 5 {level}-level English words suitable for learners (easy: beginner, medium: intermediate, hard: advanced)."
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        content = response.choices[0].message.content
        return [word.strip() for word in content.split('\n') if word.strip()]
    except Exception as e:
        return {"error": f"Failed to fetch category words: {str(e)}"}  # Should return an array or error object